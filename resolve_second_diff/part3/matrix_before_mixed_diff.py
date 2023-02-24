import time

from sympy.core.numbers import Zero

from definitions.coefficient_for_resolve import *
from sympy import Matrix, expand, fraction, together
from multiprocessing import Process
import symengine as se
import tqdm
import sys

from definitions.moments import M_φ, M_ψ
from utils.sympy_expression import parse_2_sympy_expression

sys.setrecursionlimit(1000000)

from utils.common import remove_third_and_above_smallness_from_expression, \
    remove_third_and_above_smallness_from_one_term, remove_required_and_above_smallness_from_expression, \
    remove_current_and_above_smallness_from_one_term
from utils.to_sympy_expression import transform_to_simpy
from dict_coefficients_before_mixed_and_free_term import mixed_coeff_var, dict_free_term_equations
from dict_inverse_matrix_of_second_diff import inverse_coeff_matrix
import redis
from definitions.symengine_var import *

client = redis.Redis(host='localhost', port=6379, db=0)

Inverse_matrix_before_second_diff = Matrix(
    [[m11, m12, m13, m14, m15],
     [m21, m22, m23, m24, m25],
     [m31, m32, m33, m34, m35],
     [m41, m42, m43, m44, m45],
     [m51, m52, m53, m54, m55]]
)

B_matrix = - Matrix([
    [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12, a_13, a_14, a_15, a_16, a_17, a_18, a_19, a_20, a_21],
    [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_10, b_11, b_12, b_13, b_14, b_15, b_16, b_17, b_18, b_19, b_20, b_21],
    [c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14, c_15, c_16, c_17, c_18, c_19, c_20, c_21],
    [d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_11, d_12, d_13, d_14, d_15, d_16, d_17, d_18, d_19, d_20, d_21],
    [e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9, e_10, e_11, e_12, e_13, e_14, e_15, e_16, e_17, e_18, e_19, e_20, e_21]
])

Free_and_control_matrix = - Matrix([
    [free_1],
    [free_2],
    [free_3],
    [free_4],
    [free_5]
])

print("multiplication start")
Mixed_matrix = Inverse_matrix_before_second_diff * B_matrix
Free_matrix = Inverse_matrix_before_second_diff * Free_and_control_matrix
print("multiplication end")


# TODO домножить на 1/det !!!
def simplify_and_expand_component(name, component, dict_var):
    result = 0
    begin = time.time()
    print("component = ", component, " \n")
    for term in component.args:
        expr = term.subs(dict_var)
        top, bot = fraction(expr)

        t1 = time.time()
        expanded_top = se.expand(se.sympify(top))
        del top
        t2 = time.time()
        print("expanded. term = %s. len(term) = %d, total = %.2f [s]" % (term, len(expanded_top.args), (t2 - t1)))

        t1 = time.time()
        new_top = Zero()
        for term_ in expanded_top.args:
            top = remove_current_and_above_smallness_from_one_term(parse_2_sympy_expression(str(term_)))
            new_top = new_top + top
        t2 = time.time()
        print("simplified. term = %s. len(new_top) = %d, total time = %.2f [s]\n" % (term, len(new_top.args), (t2 - t1)/60))
        result = result + new_top/bot

    end = time.time()
    print("FINISHED. component: %s. time of execution = %.2f [m] \n" % (str(component), ((end - begin)/60)))

    with open('' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


def sub_task(main_term, terms, sub_number, _client):
    print("begin subtask #%d size = %d" % (sub_number, len(terms)))
    simpl_expr = 0
    t_1 = time.time()
    for _term_ in tqdm.tqdm(terms):
        simpl_term =  remove_current_and_above_smallness_from_one_term(
            # parse_2_sympy_expression(transform_to_simpy(str(_term_)))
            _term_
        )
        print("subtask #", sub_number, " ", simpl_term)
        simpl_expr = simpl_expr + simpl_term
    t_2 = time.time()

    print(
        "end subtask #%d size = %d. time execution = %.2f [m]" %
        (sub_number, len(simpl_expr.args), (t_2 - t_1) / 60)
    )

    _client.set(str(main_term) + str(sub_number), transform_to_simpy(str(simpl_expr)))
    print("result was sended to redis for subtask # %d \n" % sub_number)


def simplify_and_expand_component_v_2(name, component, dict_var, redis_client):
    print("TODO")
    result = 0
    for term in component.args:
        BEGIN = time.time()

        expr = term.subs(dict_var)
        #TODO удалить подстановку M_psi и M_phi
        expr = expr.subs({M_ψ: 0, M_φ: 0})

        top, bot = fraction(expr)

        expanded_top = expand(top) #se.expand(se.sympify(top))
        del top
        print("1expanded. term = %s. len(expanded_top) = %d" % (term, len(expanded_top.args)))

        if expanded_top == 0:
            continue

        sub_task_len = int(len(expanded_top.args) / 3)
        tasks = []
        for i in range(3):
            if i == 2:
                sub_arr = expanded_top.args[i * sub_task_len:]
            else:
                sub_arr = expanded_top.args[i * sub_task_len: (i + 1) * sub_task_len]
            task = Process(target=sub_task, args=(term, sub_arr, i, redis_client))
            task.start()
            tasks.append(task)

        for task in tasks:
            task.join()

        res_of_expanded_term = 0
        for i in range(3):
            decode = client.get(str(term) + str(i)).decode('utf-8')
            res_of_expanded_term += parse_2_sympy_expression(decode)
            print("rres = ", transform_to_simpy(str(decode)))

        END = time.time()
        print("finished. len = %d, term = %s, total_time = %.2f [m]" % (len(res_of_expanded_term.args), str(term), (END - BEGIN)/60))
        result += res_of_expanded_term / bot

    with open('' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))



tasks = []
begin = time.time()
final_dict = mixed_coeff_var | dict_free_term_equations | inverse_coeff_matrix
print("size dict = ", len(final_dict.keys()))
#
# for row in [0, 1]:
#     for col in range(21):
#         task = Process(
#             target=simplify_and_expand_component,
#             args=("matrix_" + str(row) + "_" + str(col), Mixed_matrix.row(row)[col], final_dict)
#         )
#         task.start()
#         tasks.append(task)
#
# for task in tasks:
#     task.join()
#
# print("finished parallel multiplication 0 and 1 rows matrix")

# for row in [2]:  # [2, 3]
#     for col in [3, 8, 15, 16]:  # 8, 15, 16]:  # range(21):
#         task = Process(
#             target=simplify_and_expand_component_v_2,
#             args=("matrix_" + str(row) + "_" + str(col), Mixed_matrix.row(row)[col], final_dict, client)
#         )
#         task.start()
#         tasks.append(task)
#
# for task in tasks:
#     task.join()
# print("finished parallel multiplication 2 and 3 rows matrix")

#
# for row in [4]:
#     for col in [3, 8, 9, 12, 13, 15, 16]:  # range(21):
#         task = Process(
#             target=simplify_and_expand_component,
#             args=("matrix_" + str(row) + "_" + str(col), Mixed_matrix.row(row)[col], final_dict)
#         )
#         task.start()
#         tasks.append(task)
#
# for task in tasks:
#     task.join()
# print("finished parallel multiplication 5 row matrix")


for row in range(5):
    for col in range(1):
        task = Process(
            target=simplify_and_expand_component_v_2,
            args=("free_" + str(row) + "_" + str(col), Free_matrix.row(row)[col], final_dict, client)
        )
        task.start()
        tasks.append(task)

for task in tasks:
    task.join()

print("finished parallel multiplication free matrix")
end = time.time()

print("total time = %.2f [m]" % ((end - begin)/60))

