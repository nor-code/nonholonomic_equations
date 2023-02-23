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
a1, a2, a3, a4 = A.row(0)[0], A.row(0)[1], A.row(0)[2], A.row(0)[3]
b1, b2, b3, b4 = A.row(1)[0], A.row(1)[1], A.row(1)[2], A.row(1)[3]
c1, c2, c3, c4 = A.row(2)[0], A.row(2)[1], A.row(2)[2], A.row(2)[3]
d1, d2, d3, d4 = A.row(3)[0], A.row(3)[1], A.row(3)[2], A.row(3)[3]

m11 = remove_required_and_above_smallness_from_expression(-b4*c3*d2 + b3*c4*d2 + b4*c2*d3 - b2*c4*d3 - b3*c2*d4 + b2*c3*d4, order=5)
print("... m11 ...", m11)
m12 = remove_required_and_above_smallness_from_expression(a4*c3*d2 - a3*c4*d2 - a4*c2*d3 + a2*c4*d3 + a3*c2*d4 - a2*c3*d4, order=5)
print("... m12 ...", m12)
m13 = remove_required_and_above_smallness_from_expression(-a4*b3*d2 + a3*b4*d2 + a4*b2*d3 - a2*b4*d3 - a3*b2*d4 + a2*b3*d4, order=5)
print("... m13 ...", m13)
m14 = remove_required_and_above_smallness_from_expression(a4*b3*c2 - a3*b4*c2 - a4*b2*c3 + a2*b4*c3 + a3*b2*c4 - a2*b3*c4, order=5)
print("... m14 ...", m14)

m21 = remove_required_and_above_smallness_from_expression(b4*c3*d1 - b3*c4*d1 - b4*c1*d3 + b1*c4*d3 + b3*c1*d4 - b1*c3*d4, order=5)
print("... m21 ...", m21)
m22 = remove_required_and_above_smallness_from_expression(-a4*c3*d1 + a3*c4*d1 + a4*c1*d3 - a1*c4*d3 - a3*c1*d4 + a1*c3*d4, order=5)
print("... m22 ...", m22)
m23 = remove_required_and_above_smallness_from_expression(a4*b3*d1 - a3*b4*d1 - a4*b1*d3 + a1*b4*d3 + a3*b1*d4 - a1*b3*d4, order=5)
print("... m23 ...", m23)
m24 = remove_required_and_above_smallness_from_expression(-a4*b3*c1 + a3*b4*c1 + a4*b1*c3 - a1*b4*c3 - a3*b1*c4 + a1*b3*c4, order=5)
print("... m24 ...", m24)

m31 = remove_required_and_above_smallness_from_expression(-b4*c2*d1 + b2*c4*d1 + b4*c1*d2 - b1*c4*d2 - b2*c1*d4 + b1*c2*d4, order=5)
print("... m31 ...", m31)
m32 = remove_required_and_above_smallness_from_expression(a4*c2*d1 - a2*c4*d1 - a4*c1*d2 + a1*c4*d2 + a2*c1*d4 - a1*c2*d4, order=5)
print("... m32 ...", m32)
m33 = remove_required_and_above_smallness_from_expression(-a4*b2*d1 + a2*b4*d1 + a4*b1*d2 - a1*b4*d2 - a2*b1*d4 + a1*b2*d4, order=5)
print("... m33 ...", m33)
m34 = remove_required_and_above_smallness_from_expression(a4*b2*c1 - a2*b4*c1 - a4*b1*c2 + a1*b4*c2 + a2*b1*c4 - a1*b2*c4, order=5)
print("... m34 ...", m34)

m41 = remove_required_and_above_smallness_from_expression(b3*c2*d1 - b2*c3*d1 - b3*c1*d2 + b1*c3*d2 + b2*c1*d3 - b1*c2*d3, order=5)
print("... m41 ...", m41)
m42 = remove_required_and_above_smallness_from_expression(-a3*c2*d1 + a2*c3*d1 + a3*c1*d2 - a1*c3*d2 - a2*c1*d3 + a1*c2*d3, order=5)
print("... m42 ...", m42)
m43 = remove_required_and_above_smallness_from_expression(a3*b2*d1 - a2*b3*d1 - a3*b1*d2 + a1*b3*d2 + a2*b1*d3 - a1*b2*d3, order=5)
print("... m43 ...", m43)
m44 = remove_required_and_above_smallness_from_expression(-a3*b2*c1 + a2*b3*c1 + a3*b1*c2 - a1*b3*c2 - a2*b1*c3 + a1*b2*c3, order=5)
print("... m44 ...", m44)

det = a4*b3*c2*d1 - a3*b4*c2*d1 - a4*b2*c3*d1 + a2*b4*c3*d1 + a3*b2*c4*d1 - a2*b3*c4*d1 - a4*b3*c1*d2 + a3*b4*c1*d2 \
      + a4*b1*c3*d2 - a1*b4*c3*d2 - a3*b1*c4*d2 + a1*b3*c4*d2 + a4*b2*c1*d3 - a2*b4*c1*d3 - a4*b1*c2*d3 + a1*b4*c2*d3 \
      + a2*b1*c4*d3 - a1*b2*c4*d3 - a3*b2*c1*d4 + a2*b3*c1*d4 + a3*b1*c2*d4 - a1*b3*c2*d4 - a2*b1*c3*d4 + a1*b2*c3*d4
det = remove_required_and_above_smallness_from_expression(det, order=5)
print("... det ...", det)

A_semi_inv = Matrix([[m11, m12, m13, m14],
                [m21, m22, m23, m24],
                [m31, m32, m33, m34],
                [m41, m42, m43, m44]])
print("inv A = ", A_semi_inv)

solution = (1/det) * A_semi_inv * b
lambda1 = solution.row(0)[0]
lambda2 = solution.row(1)[0]
lambda3 = solution.row(2)[0]
lambda4 = solution.row(3)[0]


def solve_transform_and_write_to_file(lambda_i, i):
    λ_i_top, λ_i_bottom = fraction(together(lambda_i))

    top = expand_and_collect_term_before_derivatives_and_lambda(
        remove_required_and_above_smallness_from_expression(
            λ_i_top, order=5
        )
    )

    bottom = remove_required_and_above_smallness_from_expression(
        expand(λ_i_bottom, deep=True),
        order=5
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
