from sympy import linear_eq_to_matrix, together, fraction

from utils.common import *
from utils.to_sympy_expression import transform_to_simpy
from utils.sympy_expression import parse_2_sympy_expression
from multiprocessing import Process

print("решение системы { Eq6, Eq8, Eq9, Eq10 } относительно λ1, λ2, λ3, λ4")

Eq6 = parse_2_sympy_expression(open("../../dynamic/eq6.txt").readline())
Eq8 = parse_2_sympy_expression(open("../../dynamic/eq8.txt").readline())
Eq9 = parse_2_sympy_expression(open("../../dynamic/eq9.txt").readline())
Eq10 = parse_2_sympy_expression(open("../../dynamic/eq10.txt").readline())

t1 = time.time()

Eq6 = expand_and_collect_term_before_derivatives_and_lambda(Eq6)
Eq8 = expand_and_collect_term_before_derivatives_and_lambda(Eq8)
Eq9 = expand_and_collect_term_before_derivatives_and_lambda(Eq9)
Eq10 = expand_and_collect_term_before_derivatives_and_lambda(Eq10)

print("Eq6 ", Eq6)
print("Eq8 ", Eq8)
print("Eq9 ", Eq9)
print("Eq10 ", Eq10)

(A, b) = linear_eq_to_matrix([Eq6, Eq8, Eq9, Eq10], [λ_1, λ_2, λ_3, λ_4])

A_inv = A.inv()
print("inv A = ", A_inv)

solution = A_inv * b
lambda1 = solution.row(0)[0]
lambda2 = solution.row(1)[0]
lambda3 = solution.row(2)[0]
lambda4 = solution.row(3)[0]


def solve_transform_and_write_to_file(lambda_i, i):
    λ_i_top, λ_i_bottom = fraction(together(lambda_i))
    top = expand_and_collect_term_before_derivatives_and_lambda(λ_i_top)
    bottom = simplify(
        simplification_expression(
            expand(λ_i_bottom)
        )
    )
    result = top / bottom
    with open('../../lambda/part1/lambda_' + str(i + 1) + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
solutions = [lambda1, lambda2, lambda3, lambda4]
for i in range(len(solutions)):
    task = Process(target=solve_transform_and_write_to_file, args=(solutions[i], i))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()
print("total time = %.2f [m]" % ((t2-t1) / 60))
