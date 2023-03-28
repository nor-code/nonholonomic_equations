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

Free_and_control_matrix = - Matrix([
    [free_1],
    [free_2],
    [free_3],
    [free_4],
    [free_5]
])

print("multiplication start")
# Mixed_matrix = Inverse_matrix_before_second_diff * B_matrix
Free_matrix = Inverse_matrix_before_second_diff * Free_and_control_matrix
print("multiplication end")


# TODO домножить на 1/det !!!
def simplify_and_expand_component(name, component, dict_var, is_free):
    result = 0
    begin = time.time()
    print("component = ", component, " \n")
    for term in component.args:
        expr = term.subs(dict_var)
        top = remove_current_and_above_smallness_from_one_term(expand(expr), order=2)
        result = result + top

    end = time.time()
    print("FINISHED. component: %s. time of execution = %.2f [m] \n" % (str(component), ((end - begin)/60)))

    # if is_free:
    #     result = simplify_free_term(result)

    with open('' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
begin = time.time()
final_dict = mixed_coeff_var | dict_free_term_equations | inverse_coeff_matrix
print("size dict = ", len(final_dict.keys()))


for row in range(5):
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
