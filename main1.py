# import Dynamics
# if __name__ == "__main__":
#     Dynamics.print_equations_for_Wolfram_Mathematica()
from numba import jit
# x_raw = input().split(" ")
# y_raw = input().split(" ")
#
# x = list(float(x_i) for x_i in x_raw)
# y = list(float(y_i) for y_i in y_raw)
#
# mean_x = sum(x) / float(len(x))
# mean_y = sum(y) / float(len(y))
#
# var_x, var_y = sum((x_i - mean_x) ** 2 for x_i in x) / float(len(x)),\
#                sum((y_i - mean_y) ** 2 for y_i in y) / float(len(y))
#
# covar_xy = sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y)) / float(len(x))
#
# a = covar_xy / var_x
# b = mean_y - a * mean_x
#
# print(a)
# print(b)

from sympy import *
from sympy.core.numbers import Zero

from definitions.constants import *
from definitions.generic_coordinates import *
from utils.common import *
from sympy.solvers.solveset import linsolve
from utils.to_sympy_expression import *
from definitions.coefficient_for_resolve import *
import symengine as se
import sys
sys.setrecursionlimit(100000)
import tqdm
#
# x, y, z = symbols('x, y, z')
# t = Symbol('t')
# x1 = Function('α')(t)
# x2 = Function('β')(t)
# x3 = Function('w')(t)
# solution = linsolve([x + y + z - diff(x1, t) + sin(x3)*diff(x3, t), x + y + 2 * z - 3 * x1 - diff(x2, t)],
#              (diff(x1, t), diff(x2, t))
# )
#
# print("x'1 = ", solution.args[0][0])
# print("x'1 = ", diff(solution.args[0][0], t))
#
# eq1 = diff(diff(x1, t), t) + sin(x1) * diff(x1, t) + x1*22
# print("\neq1 = ", eq1)
#
# eq1 = eq1.subs(diff(diff(x1, t), t), diff(solution.args[0][0], t))
# print("after subs1 eq1 = ", eq1)
#
# eq1 = eq1.subs(diff(x1, t), solution.args[0][0])
# print("after subs2 eq1 = ", eq1)
from utils.sympy_expression import parse_2_sympy_expression
from multiprocessing import Process
import redis

# expr = parse_2_sympy_expression(open('./resolve_second_diff/part2/component_det.txt').readline())
#
# expr = expr.subs({
#     C_mz: 0.081 - 0.026,
#     R: 0.081,
#     r: 0.026,
#     m: 0.11,
#     M: 0.138,
#     M_p: 0.6,
#     J_px: 1,
#     J_py: 1,
#     J_pz: 1,
#     J_wx: 1,
#     J_wy: 1,
#     J_wz: 1
# })
# print(transform_to_simpy(str(expr)))

client = redis.Redis(host='localhost', port=6379, db=0)
client.set("a", 1)
# expr = -a_4*m31 - b_4*m32 - c_4*m33 - d_4*m34 - e_4*m35
expr = -a_4*m11 - b_4*m12 - c_4*m13 - d_4*m14 - e_4*m15


t1 = time.time()
dict_var = {a_4: parse_2_sympy_expression(open(
        "./collect_parallel/eq1/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
     b_4: parse_2_sympy_expression(open(
         "./collect_parallel/eq2/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
     c_4: parse_2_sympy_expression(open(
        "./collect_parallel/eq3/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
     d_4: parse_2_sympy_expression(open(
        "./collect_parallel/eq4/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
     e_4: parse_2_sympy_expression(open(
        "./collect_parallel/eq5/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),

     m11: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m11.txt").readline()),
     m12: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m12.txt").readline()),
     m13: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m13.txt").readline()),
     m14: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m14.txt").readline()),
     m15: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m15.txt").readline()),
    #  m31: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m31.txt").readline()),
    #  m32: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m32.txt").readline()),
    #  m33: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m33.txt").readline()),
    #  m34: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m34.txt").readline()),
    #  m35: parse_2_sympy_expression(open("./resolve_second_diff/part2/component_m35.txt").readline())
     }
t2 = time.time()
print("------------------", ((t2-t1)/60), "------------------")

result = 0
for term in expr.args:
    expr = term.subs(dict_var)
    top, bot = fraction(expr)

    t1 = time.time()
    expanded_top = se.expand(se.sympify(top))
    with open('./' + str(term) + '.txt', 'w') as out:
        out.write(str(expanded_top))
    del top
    t2 = time.time()
    print("expanded. term = %s. len(term) = %d, total = %.2f [s]" % (term, len(expanded_top.args), (t2 - t1)))

    if expanded_top == 0:
        continue
    t1 = time.time()
    new_top = Zero()

    def sub_task(main_term, terms, sub_number, _client):
        print("begin subtask #%d size = %d" % (sub_number, len(terms)))
        simpl_expr = 0
        t_1 = time.time()
        for _term_ in terms:
            simpl_term = remove_third_and_above_smallness_from_one_term(parse_2_sympy_expression(str(_term_)))
            simpl_expr = simpl_expr + simpl_term
        t_2 = time.time()
        print("end subtask #%d size = %d. time execution = %.2f [m]" % (sub_number, len(new_top.args), (t_2 - t_1)/60))

        _client.set(str(main_term) + str(sub_number), transform_to_simpy(str(new_top)))
        print("result was sended to redis for subtask # %d " % sub_number)

    sub_task_len = int(len(expanded_top.args) / 30)
    tasks = []
    total = 0
    print("len of expanded top = ", len(expanded_top.args))
    for i in range(30):
        if i == 29:
            sub_arr = expanded_top.args[i * sub_task_len:]
        else:
            sub_arr = expanded_top.args[i * sub_task_len: (i + 1) * sub_task_len]
        task = Process(
            target=sub_task,
            args=(term, sub_arr, i, client)
        )
        total += len(sub_arr)
        task.start()
        tasks.append(task)

    print("total = ", total)
    for task in tasks:
        task.join()

    res = 0
    for i in range(30):
        res = res + parse_2_sympy_expression(client.get(str(term) + str(i)).decode('utf-8'))

    print("finished. len = ", len(res.args))

    with open('./' + str(term) + "_simpl" + '.txt', 'w') as out:
        out.write(str(res))
    print(
        "simplified. total time = %.2f [s]\n" % ((t2 - t1) / 60)
    )

print(result)