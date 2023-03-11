import time

from sympy import diff
from definitions.generic_coordinates import *
from definitions.coefficient_for_resolve import *
from definitions.constants import *
from utils.sympy_expression import parse_2_sympy_expression
import sys

from utils.to_sympy_expression import transform_to_simpy


BEGIN = time.time()

u, v, p, q = symbols("u, v, p, q")  # скорости x y x2 x5 (x, y, β, ψ)
p1, n, q1, r1 = symbols("p1, n, q1, r1")  # скорости x3, x4, x7, x8 (γ, φ, ε, τ) выражаются через неголономные связи

eq1 = free_1

eq2 = free_2

eq3 = free_3

eq4 = free_7

param_dict = {
    C_mz: 0.081 - 0.026,
    C_Mz: 0.01,
    R: 0.081,
    r: 0.026,
    m: 0.11,
    M: 0.138,
    M_p: 0.6,
    J_px: 1,
    J_py: 1,
    J_pz: 1,
    J_wx: 1,
    J_wy: 1,
    J_wz: 1
}

det = parse_2_sympy_expression(open("../../resolve_second_diff/part2_2/component_det.txt").readline()).subs(param_dict)
with open("eqns/det.txt", "w") as out:
    out.write(transform_to_simpy(str(det)))
print("init determinant expression")


