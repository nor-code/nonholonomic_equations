import time

from sympy import diff
from definitions.generic_coordinates import *
from definitions.coefficient_for_resolve import *
from definitions.constants import *
from utils.sympy_expression import parse_2_sympy_expression
import sys

from utils.to_sympy_expression import transform_to_simpy

sys.setrecursionlimit(100000)

BEGIN = time.time()

u, v, p, q, r, h = symbols("u, v, p, q, r, h")  # x y x1 x2 x3 x5
m, p1, q1, r1 = symbols("m, p1, q1, r1") # x4, x6, x7, x8

eq1 = a_1 * u**2 + a_2 * u*v + a_3 * u*p + a_4 * u*q + a_5 * u*r + a_6 * u*h + a_7 * v**2 + a_8 * v*p + a_9 * v*q + a_10 * v*r\
+ a_11 * v*h + a_12 * p**2 + a_13 * p*q + a_14 * p*r + a_15 * p*h + a_16 * q**2 + a_17 * q*r + a_18 * q*h + a_19 * r**2 + a_20 * r*h + a_21 * h**2 + free_1

eq2 = b_1 * u**2 + b_2 * u*v + b_3 * u*p + b_4 * u*q + b_5 * u*r + b_6 * u*h + b_7 * v**2 + b_8 * v*p + b_9 * v*q + b_10 * v*r\
+ b_11 * v*h + b_12 * p**2 + b_13 * p*q + b_14 * p*r + b_15 * p*h + b_16 * q**2 + b_17 * q*r + b_18 * q*h + b_19 * r**2 + b_20 * r*h + b_21 * h**2 + free_2

eq3 = c_1 * u**2 + c_2 * u*v + c_3 * u*p + c_4 * u*q + c_5 * u*r + c_6 * u*h + c_7 * v**2 + c_8 * v*p + c_9 * v*q + c_10 * v*r\
+ c_11 * v*h + c_12 * p**2 + c_13 * p*q + c_14 * p*r + c_15 * p*h + c_16 * q**2 + c_17 * q*r + c_18 * q*h + c_19 * r**2 + c_20 * r*h + c_21 * h**2 + free_3

eq4 = d_1 * u**2 + d_2 * u*v + d_3 * u*p + d_4 * u*q + d_5 * u*r + d_6 * u*h + d_7 * v**2 + d_8 * v*p + d_9 * v*q + d_10 * v*r\
+ d_11 * v*h + d_12 * p**2 + d_13 * p*q + d_14 * p*r + d_15 * p*h + d_16 * q**2 + d_17 * q*r + d_18 * q*h + d_19 * r**2 + d_20 * r*h + d_21 * h**2 + free_4

eq5 = e_1 * u**2 + e_2 * u*v + e_3 * u*p + e_4 * u*q + e_5 * u*r + e_6 * u*h + e_7 * v**2 + e_8 * v*p + e_9 * v*q + e_10 * v*r\
+ e_11 * v*h + e_12 * p**2 + e_13 * p*q + e_14 * p*r + e_15 * p*h + e_16 * q**2 + e_17 * q*r + e_18 * q*h + e_19 * r**2 + e_20 * r*h + e_21 * h**2 + free_5

eq6 = f_1 * u**2 + f_2 * u*v + f_3 * u*p + f_4 * u*q + f_5 * u*r + f_6 * u*h + f_7 * v**2 + f_8 * v*p + f_9 * v*q + f_10 * v*r\
+ f_11 * v*h + f_12 * p**2 + f_13 * p*q + f_14 * p*r + f_15 * p*h + f_16 * q**2 + f_17 * q*r + f_18 * q*h + f_19 * r**2 + f_20 * r*h + f_21 * h**2 + free_7


param_dict = {
    C_mz: 0.081 - 0.026,
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

det = parse_2_sympy_expression(open("../../resolve_second_diff/part2/component_det.txt").readline()).subs(param_dict)
with open("eqns/det.txt", "w") as out:
    out.write(transform_to_simpy(str(det)))
print("init determinant expression")


