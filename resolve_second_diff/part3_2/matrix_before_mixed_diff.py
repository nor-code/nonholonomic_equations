import time

from sympy.core.numbers import Zero

from definitions.coefficient_for_resolve import *
from sympy import Matrix, expand, collect, simplify, Mul
from multiprocessing import Process
import sys

from definitions.constants import C_Mx, C_My, C_Mz
from definitions.generic_coordinates import *
from utils.latex_converter import print_in_latex
from utils.sympy_expression import parse_2_sympy_expression

sys.setrecursionlimit(1000000)

from utils.common import remove_third_and_above_smallness_from_expression, \
    remove_third_and_above_smallness_from_one_term, remove_required_and_above_smallness_from_expression, \
    remove_current_and_above_smallness_from_one_term, simplify_determinant, simplify_free_term
from utils.to_sympy_expression import transform_to_simpy
from dict_coefficients_before_mixed_and_free_term import mixed_coeff_var, dict_free_term_equations
from dict_inverse_matrix_of_second_diff import inverse_coeff_matrix
import redis

ORDER=2
client = redis.Redis(host='localhost', port=6379, db=0)

Inverse_matrix_before_second_diff = Matrix(
    [[m11, m12, m13],
     [m21, m22, m23],
     [m31, m32, m33]]
)

B_matrix = - Matrix([
    [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10],
    [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_10],
    [c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10],
])

Free_and_control_matrix = - Matrix([
    [free_1],
    [free_2],
    [free_3]
])

print("multiplication start")
Mixed_matrix = Inverse_matrix_before_second_diff * B_matrix
Free_matrix = Inverse_matrix_before_second_diff * Free_and_control_matrix
print("multiplication end")


# TODO домножить на 1/det !!!
def simplify_and_expand_component(name, component, dict_var, is_free):
    global ORDER
    begin = time.time()
    print("component = ", component, " \n")

    result = expand(component.subs(dict_var), deep=True)
    result = remove_required_and_above_smallness_from_expression(result, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])

    end = time.time()
    print("FINISHED. component: %s. time of execution = %.2f [m] \n" % (str(component), ((end - begin)/60)))

    if is_free:
        final_res = 0
        for free_var in [x1, x2, x3, x4, x5, x6, x7, x8]:
            coefficient_free_var = collect(result, free_var).coeff(free_var)
            result = result - expand(Mul(coefficient_free_var, free_var))
            final_res += Mul(simplify_determinant(coefficient_free_var), free_var)

        final_res += simplify_determinant(result)  # добавляем оставшийся свободный член
        print(component, " = ", print_in_latex(final_res))
        result = final_res

    with open('' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
begin = time.time()
final_dict = mixed_coeff_var | dict_free_term_equations | inverse_coeff_matrix
print("size dict = ", len(final_dict.keys()))


for row in range(3):
    for col in range(1):
        task = Process(
            target=simplify_and_expand_component,
            args=("free_" + str(row) + "_" + str(col), Free_matrix.row(row)[col], final_dict, True)
        )
        task.start()
        tasks.append(task)

for task in tasks:
    task.join()


print("finished parallel multiplication [0, 1, 2, 3] rows matrix")
end = time.time()

print("total time = %.2f [m]" % ((end - begin)/60))
