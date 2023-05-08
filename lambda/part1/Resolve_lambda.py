from sympy import linear_eq_to_matrix, together, fraction

from utils.common import *
from utils.to_sympy_expression import transform_to_simpy
from utils.sympy_expression import parse_2_sympy_expression
from multiprocessing import Process

ORDER = 2

print("решение системы { Eq6, Eq8, Eq9, Eq10 } относительно λ1, λ2, λ3, λ4")

Eq1 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq1.txt").readline())  # open("../../dynamic/eq6.txt")
Eq2 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq2.txt").readline())  # open("../../dynamic/eq6.txt")
Eq4 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq4.txt").readline())  # open("../../dynamic/eq6.txt")
Eq5 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq5.txt").readline())  # open("../../dynamic/eq6.txt")

t1 = time.time()

print("Eq6 ", Eq1)
print("Eq8 ", Eq2)
print("Eq9 ", Eq4)
print("Eq5 ", Eq5)

(A, b) = linear_eq_to_matrix([Eq1, Eq2, Eq4, Eq5], [λ_1, λ_2, λ_3, λ_4])
a1, a2, a3, a4 = A.row(0)[0], A.row(0)[1], A.row(0)[2], A.row(0)[3]
b1, b2, b3, b4 = A.row(1)[0], A.row(1)[1], A.row(1)[2], A.row(1)[3]
c1, c2, c3, c4 = A.row(2)[0], A.row(2)[1], A.row(2)[2], A.row(2)[3]
d1, d2, d3, d4 = A.row(3)[0], A.row(3)[1], A.row(3)[2], A.row(3)[3]

# before order was = 5
m11 = remove_required_and_above_smallness_from_expression(-b4*c3*d2 + b3*c4*d2 + b4*c2*d3 - b2*c4*d3 - b3*c2*d4 + b2*c3*d4, order=ORDER)
m11 = remove_required_and_above_smallness_from_expression(m11, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m11 ...", m11)
m12 = remove_required_and_above_smallness_from_expression(a4*c3*d2 - a3*c4*d2 - a4*c2*d3 + a2*c4*d3 + a3*c2*d4 - a2*c3*d4, order=ORDER)
m12 = remove_required_and_above_smallness_from_expression(m12, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m12 ...", m12)
m13 = remove_required_and_above_smallness_from_expression(-a4*b3*d2 + a3*b4*d2 + a4*b2*d3 - a2*b4*d3 - a3*b2*d4 + a2*b3*d4, order=ORDER)
m13 = remove_required_and_above_smallness_from_expression(m13, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m13 ...", m13)
m14 = remove_required_and_above_smallness_from_expression(a4*b3*c2 - a3*b4*c2 - a4*b2*c3 + a2*b4*c3 + a3*b2*c4 - a2*b3*c4, order=ORDER)
m14 = remove_required_and_above_smallness_from_expression(m14, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m14 ...", m14)

m21 = remove_required_and_above_smallness_from_expression(b4*c3*d1 - b3*c4*d1 - b4*c1*d3 + b1*c4*d3 + b3*c1*d4 - b1*c3*d4, order=ORDER)
m21 = remove_required_and_above_smallness_from_expression(m21, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m21 ...", m21)
m22 = remove_required_and_above_smallness_from_expression(-a4*c3*d1 + a3*c4*d1 + a4*c1*d3 - a1*c4*d3 - a3*c1*d4 + a1*c3*d4, order=ORDER)
m22 = remove_required_and_above_smallness_from_expression(m22, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m22 ...", m22)
m23 = remove_required_and_above_smallness_from_expression(a4*b3*d1 - a3*b4*d1 - a4*b1*d3 + a1*b4*d3 + a3*b1*d4 - a1*b3*d4, order=ORDER)
m23 = remove_required_and_above_smallness_from_expression(m23, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m23 ...", m23)
m24 = remove_required_and_above_smallness_from_expression(-a4*b3*c1 + a3*b4*c1 + a4*b1*c3 - a1*b4*c3 - a3*b1*c4 + a1*b3*c4, order=ORDER)
m24 = remove_required_and_above_smallness_from_expression(m24, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m24 ...", m24)

m31 = remove_required_and_above_smallness_from_expression(-b4*c2*d1 + b2*c4*d1 + b4*c1*d2 - b1*c4*d2 - b2*c1*d4 + b1*c2*d4, order=ORDER)
m31 = remove_required_and_above_smallness_from_expression(m31, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m31 ...", m31)
m32 = remove_required_and_above_smallness_from_expression(a4*c2*d1 - a2*c4*d1 - a4*c1*d2 + a1*c4*d2 + a2*c1*d4 - a1*c2*d4, order=ORDER)
m32 = remove_required_and_above_smallness_from_expression(m32, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m32 ...", m32)
m33 = remove_required_and_above_smallness_from_expression(-a4*b2*d1 + a2*b4*d1 + a4*b1*d2 - a1*b4*d2 - a2*b1*d4 + a1*b2*d4, order=ORDER)
m33 = remove_required_and_above_smallness_from_expression(m33, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m33 ...", m33)
m34 = remove_required_and_above_smallness_from_expression(a4*b2*c1 - a2*b4*c1 - a4*b1*c2 + a1*b4*c2 + a2*b1*c4 - a1*b2*c4, order=ORDER)
m34 = remove_required_and_above_smallness_from_expression(m34, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m34 ...", m34)

m41 = remove_required_and_above_smallness_from_expression(b3*c2*d1 - b2*c3*d1 - b3*c1*d2 + b1*c3*d2 + b2*c1*d3 - b1*c2*d3, order=ORDER)
m41 = remove_required_and_above_smallness_from_expression(m41, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m41 ...", m41)
m42 = remove_required_and_above_smallness_from_expression(-a3*c2*d1 + a2*c3*d1 + a3*c1*d2 - a1*c3*d2 - a2*c1*d3 + a1*c2*d3, order=ORDER)
m42 = remove_required_and_above_smallness_from_expression(m42, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m42 ...", m42)
m43 = remove_required_and_above_smallness_from_expression(a3*b2*d1 - a2*b3*d1 - a3*b1*d2 + a1*b3*d2 + a2*b1*d3 - a1*b2*d3, order=ORDER)
m43 = remove_required_and_above_smallness_from_expression(m43, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m43 ...", m43)
m44 = remove_required_and_above_smallness_from_expression(-a3*b2*c1 + a2*b3*c1 + a3*b1*c2 - a1*b3*c2 - a2*b1*c3 + a1*b2*c3, order=ORDER)
m44 = remove_required_and_above_smallness_from_expression(m44, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... m44 ...", m44)

det = a4*b3*c2*d1 - a3*b4*c2*d1 - a4*b2*c3*d1 + a2*b4*c3*d1 + a3*b2*c4*d1 - a2*b3*c4*d1 - a4*b3*c1*d2 + a3*b4*c1*d2 \
      + a4*b1*c3*d2 - a1*b4*c3*d2 - a3*b1*c4*d2 + a1*b3*c4*d2 + a4*b2*c1*d3 - a2*b4*c1*d3 - a4*b1*c2*d3 + a1*b4*c2*d3 \
      + a2*b1*c4*d3 - a1*b2*c4*d3 - a3*b2*c1*d4 + a2*b3*c1*d4 + a3*b1*c2*d4 - a1*b3*c2*d4 - a2*b1*c3*d4 + a1*b2*c3*d4
det = remove_required_and_above_smallness_from_expression(det, order=ORDER)
det = remove_required_and_above_smallness_from_expression(det, order=ORDER, small_params=[x20, x30, C_Mx, C_My, C_Mz])
print("... det ...", det)

A_inv = simplify(
    (1/det) * Matrix([[m11, m12, m13, m14],
                      [m21, m22, m23, m24],
                      [m31, m32, m33, m34],
                      [m41, m42, m43, m44]])
)
print("inv A = ", A_inv)

solution = A_inv * b
lambda1 = solution.row(0)[0]
lambda2 = solution.row(1)[0]
lambda3 = solution.row(2)[0]
lambda4 = solution.row(3)[0]


def solve_transform_and_write_to_file(lambda_i, i):
    global ORDER
    λ_i_top, λ_i_bottom = fraction(together(lambda_i))

    bottom = simplify(
        remove_required_and_above_smallness_from_expression(
            expand(λ_i_bottom, deep=True),
            order=ORDER
        )
    )

    simplified_top_i = 0
    for term_i in expand(λ_i_top, deep=True).args:
        if not is_remove_small_term_with_velocities(term_i):
            simplified_top_i += term_i
    top = expand_and_collect_term_before_derivatives_and_lambda(
        simplified_top_i
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
