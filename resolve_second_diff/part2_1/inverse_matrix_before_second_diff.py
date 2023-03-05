import time
from multiprocessing import Process

from sympy import Matrix, expand
from definitions.coefficient_for_resolve import *
from utils.common import remove_third_and_above_smallness_from_expression
from utils.to_sympy_expression import replace_space_to_multiplication_sym, transform_to_simpy
import tqdm
from definitions.generic_coordinates import *
from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *
from coefficient_dict import main_var_subs
from utils.common import remove_required_and_above_smallness_from_expression

a1 = parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t))
a2 = parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t))
a3 = parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t))
a4 = parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t))
a5 = parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_d_γ_t__2__.txt").readline()).coeff(diff(diff(x3, t), t))
a7 = parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_d_ψ_t__2__.txt").readline()).coeff(diff(diff(x5, t), t))

b1 = parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t))
b2 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq2/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t))
b3 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq2/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t))
b4 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq2/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t))
b5 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq2/d_d_γ_t__2__.txt").readline()).coeff(diff(diff(x3, t), t))
b7 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq2/d_d_ψ_t__2__.txt").readline()).coeff(diff(diff(x5, t), t))

c1 = parse_2_sympy_expression(open(
     "../../collect_parallel/eq3/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t))
c2 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq3/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t))
c3 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq3/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t))
c4 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq3/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t))
c5 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq3/d_d_γ_t__2__.txt").readline()).coeff(diff(diff(x3, t), t))
c7 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq3/d_d_ψ_t__2__.txt").readline()).coeff(diff(diff(x5, t), t))

d1 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq4/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t))
d2 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq4/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t))
d3 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq4/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t))
d4 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq4/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t))
d5 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq4/d_d_γ_t__2__.txt").readline()).coeff(diff(diff(x3, t), t))
d7 = parse_2_sympy_expression(open(
    "../../collect_parallel/eq4/d_d_ψ_t__2__.txt").readline()).coeff(diff(diff(x5, t), t))

m11 = remove_required_and_above_smallness_from_expression(-b4*c3*d2 + b3*c4*d2 + b4*c2*d3 - b2*c4*d3 - b3*c2*d4 + b2*c3*d4, order=2)
print("... m11 ...", m11)
with open('component_' + "m11" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m11)))

m12 = remove_required_and_above_smallness_from_expression(a4*c3*d2 - a3*c4*d2 - a4*c2*d3 + a2*c4*d3 + a3*c2*d4 - a2*c3*d4, order=2)
print("... m12 ...", m12)
with open('component_' + "m12" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m12)))

m13 = remove_required_and_above_smallness_from_expression(-a4*b3*d2 + a3*b4*d2 + a4*b2*d3 - a2*b4*d3 - a3*b2*d4 + a2*b3*d4, order=2)
print("... m13 ...", m13)
with open('component_' + "m13" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m13)))

m14 = remove_required_and_above_smallness_from_expression(a4*b3*c2 - a3*b4*c2 - a4*b2*c3 + a2*b4*c3 + a3*b2*c4 - a2*b3*c4, order=2)
print("... m14 ...", m14)
with open('component_' + "m14" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m14)))

m21 = remove_required_and_above_smallness_from_expression(b4*c3*d1 - b3*c4*d1 - b4*c1*d3 + b1*c4*d3 + b3*c1*d4 - b1*c3*d4, order=2)
print("... m21 ...", m21)
with open('component_' + "m21" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m21)))

m22 = remove_required_and_above_smallness_from_expression(-a4*c3*d1 + a3*c4*d1 + a4*c1*d3 - a1*c4*d3 - a3*c1*d4 + a1*c3*d4, order=2)
print("... m22 ...", m22)
with open('component_' + "m22" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m22)))

m23 = remove_required_and_above_smallness_from_expression(a4*b3*d1 - a3*b4*d1 - a4*b1*d3 + a1*b4*d3 + a3*b1*d4 - a1*b3*d4, order=2)
print("... m23 ...", m23)
with open('component_' + "m23" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m23)))

m24 = remove_required_and_above_smallness_from_expression(-a4*b3*c1 + a3*b4*c1 + a4*b1*c3 - a1*b4*c3 - a3*b1*c4 + a1*b3*c4, order=2)
print("... m24 ...", m24)
with open('component_' + "m24" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m24)))

m31 = remove_required_and_above_smallness_from_expression(-b4*c2*d1 + b2*c4*d1 + b4*c1*d2 - b1*c4*d2 - b2*c1*d4 + b1*c2*d4, order=2)
print("... m31 ...", m31)
with open('component_' + "m31" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m31)))

m32 = remove_required_and_above_smallness_from_expression(a4*c2*d1 - a2*c4*d1 - a4*c1*d2 + a1*c4*d2 + a2*c1*d4 - a1*c2*d4, order=2)
print("... m32 ...", m32)
with open('component_' + "m32" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m32)))

m33 = remove_required_and_above_smallness_from_expression(-a4*b2*d1 + a2*b4*d1 + a4*b1*d2 - a1*b4*d2 - a2*b1*d4 + a1*b2*d4, order=2)
print("... m33 ...", m33)
with open('component_' + "m33" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m33)))

m34 = remove_required_and_above_smallness_from_expression(a4*b2*c1 - a2*b4*c1 - a4*b1*c2 + a1*b4*c2 + a2*b1*c4 - a1*b2*c4, order=2)
print("... m34 ...", m34)
with open('component_' + "m34" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m34)))

m41 = remove_required_and_above_smallness_from_expression(b3*c2*d1 - b2*c3*d1 - b3*c1*d2 + b1*c3*d2 + b2*c1*d3 - b1*c2*d3, order=2)
print("... m41 ...", m41)
with open('component_' + "m41" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m41)))

m42 = remove_required_and_above_smallness_from_expression(-a3*c2*d1 + a2*c3*d1 + a3*c1*d2 - a1*c3*d2 - a2*c1*d3 + a1*c2*d3, order=2)
print("... m42 ...", m42)
with open('component_' + "m42" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m42)))

m43 = remove_required_and_above_smallness_from_expression(a3*b2*d1 - a2*b3*d1 - a3*b1*d2 + a1*b3*d2 + a2*b1*d3 - a1*b2*d3, order=2)
print("... m43 ...", m43)
with open('component_' + "m43" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m43)))

m44 = remove_required_and_above_smallness_from_expression(-a3*b2*c1 + a2*b3*c1 + a3*b1*c2 - a1*b3*c2 - a2*b1*c3 + a1*b2*c3, order=2)
print("... m44 ...", m44)
with open('component_' + "m44" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m44)))

det = a4*b3*c2*d1 - a3*b4*c2*d1 - a4*b2*c3*d1 + a2*b4*c3*d1 + a3*b2*c4*d1 - a2*b3*c4*d1 - a4*b3*c1*d2 + a3*b4*c1*d2 \
      + a4*b1*c3*d2 - a1*b4*c3*d2 - a3*b1*c4*d2 + a1*b3*c4*d2 + a4*b2*c1*d3 - a2*b4*c1*d3 - a4*b1*c2*d3 + a1*b4*c2*d3 \
      + a2*b1*c4*d3 - a1*b2*c4*d3 - a3*b2*c1*d4 + a2*b3*c1*d4 + a3*b1*c2*d4 - a1*b3*c2*d4 - a2*b1*c3*d4 + a1*b2*c3*d4
det = remove_required_and_above_smallness_from_expression(det, order=2)
print("... det ...", det)
with open('component_' + "det" + '.txt', 'w') as out:
    out.write(transform_to_simpy(str(m11)))

A_semi_inv = Matrix([
    [m11, m12, m13, m14],
    [m21, m22, m23, m24],
    [m31, m32, m33, m34],
    [m41, m42, m43, m44]]
)
print("inv A = ", A_semi_inv)