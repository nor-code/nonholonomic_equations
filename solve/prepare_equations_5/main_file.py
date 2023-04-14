import time

from sympy import diff, sin, cos
from definitions.generic_coordinates import *
from definitions.coefficient_for_resolve import *
from definitions.constants import *
from definitions.moments import M_φ, M_ψ
from utils.sympy_expression import parse_2_sympy_expression
import sys

from utils.to_sympy_expression import transform_to_simpy


BEGIN = time.time()

u, v, p, q, s1, w1 = symbols("u, v, p, q, s1, w1")  # скорости x y x1 x4 x5 x6  (x, y, α, φ, ψ, δ)

p1, n, q1, r1 = symbols("p1, n, q1, r1")  # скорости x2, x3, x7, x8 (β, γ, ε, τ) выражаются через неголономные связи

eq1 = free_1  # x

eq2 = free_2  # y

eq3 = free_3  # alpha

eq4 = free_4  # phi

eq5 = free_7  # delta

eq6 = free_5  # psi


x20_value = 0.207
x30_value = 0.21

x70_value = 0.207
x80_value = 0.21

inertia = {
    J_px: M_p * R_p ** 2 / 4 + M_p * C_Mz ** 2,
    J_py: M_p * R_p ** 2 / 4 + M_p * C_Mz ** 2,
    J_pz: M_p * R_p ** 2 / 4,
    J_wx: m * r ** 2 / 4 + m * C_mz ** 2,
    J_wy: m * r ** 2 / 2 + m * C_mz ** 2,
    J_wz: m * r ** 2 / 4
}

param_dict = {
    C_mz: (0.081 - 0.026),
    C_Mz: 0.01,
    C_Mx: 0.003,
    C_My: 0.0005,

    g: 10,
    R: 0.081,
    r: 0.026,
    m: 0.05,
    M: 0.137,
    M_p: 0.65,
    R_p: 0.08,

    sin_x20: sin(x20_value),
    sin_x30: sin(x30_value),
    sin_x70: sin(x70_value),
    sin_x80: sin(x80_value),

    cos_x20: cos(x20_value),
    cos_x30: cos(x30_value),
    cos_x70: cos(x70_value),
    cos_x80: cos(x80_value),

    x20: x20_value,
    x30: x30_value,

    M_φ: 0,
    M_ψ: 0
}

det = parse_2_sympy_expression(open("../../resolve_second_diff/part2_5/component_det.txt").readline()).subs(inertia).subs(param_dict)
with open("eqns/det.txt", "w") as out:
    out.write(transform_to_simpy(str(det)))
print("init determinant expression")


