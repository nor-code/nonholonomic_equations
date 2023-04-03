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

u, v, p, q, s1, w1 = symbols("u, v, p, q, s1, w1")  # скорости x y x2 x5  x1 x6  (x, y, β, ψ,    α, δ)

p1, n, q1, r1 = symbols("p1, n, q1, r1")  # скорости x3, x4, x7, x8 (γ, φ, ε, τ) выражаются через неголономные связи

eq1 = free_1

eq2 = free_2

eq3 = free_3

eq4 = free_4

eq5 = free_5

eq7 = free_7


x20 = 0.207
x30 = 0.21

x70 = 0.207
x80 = 0.21

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

    sin_x20: sin(x20),
    sin_x30: sin(x30),
    sin_x70: sin(x70),
    sin_x80: sin(x80),

    cos_x20: cos(x20),
    cos_x30: cos(x30),
    cos_x70: cos(x70),
    cos_x80: cos(x80),

    M_φ: 0,
    M_ψ: 0
}

det = parse_2_sympy_expression(open("../../resolve_second_diff/part2_3/component_det.txt").readline()).subs(inertia).subs(param_dict)
with open("eqns/det.txt", "w") as out:
    out.write(transform_to_simpy(str(det)))
print("init determinant expression")


