from sympy import sin, cos

from definitions.constants import *
from definitions.generic_coordinates import *
from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *

x20 = 1.04
x30 = 0.61

x70 = 1.04
x80 = 0.61

inertia = {
    # J_px: M_p * R_p ** 2 / 4 + M_p * C_Mz ** 2,
    # J_py: M_p * R_p ** 2 / 4 + M_p * C_Mz ** 2,
    # J_pz: M_p * R_p ** 2 / 4,
    # J_wx: m * r ** 2 / 4 + m * C_mz ** 2,
    # J_wy: m * r ** 2 / 2 + m * C_mz ** 2,
    # J_wz: m * r ** 2 / 4
}

dict_for_subs = {
    # C_mz: (0.081 - 0.026),
    # C_Mz: 0.01,
    # C_Mx: 0.01,
    # C_My: 0.01,
    #
    # R: 0.081,
    # R_p: 0.08,
    # r: 0.026,
    # m: 0.05,
    # M: 0.137,
    # M_p: 0.65,

    # sin_x20: sin(x20),
    # sin_x30: sin(x30),
    # sin_x70: sin(x70),
    # sin_x80: sin(x80),
    #
    # cos_x20: cos(x20),
    # cos_x30: cos(x30),
    # cos_x70: cos(x70),
    # cos_x80: cos(x80),

}

main_vars_subs = {
    a1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    a2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    a3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    a4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_φ_t__2__.txt").readline()).coeff(diff(diff(x4, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    a5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),

    b1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    b2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    b3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    b4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_φ_t__2__.txt").readline()).coeff(diff(diff(x4, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    b5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),

    c1: parse_2_sympy_expression(open(
         "../../collect_parallel/eq8/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    c2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    c3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    c4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_φ_t__2__.txt").readline()).coeff(diff(diff(x4, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    c5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),

    d1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    d2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    d3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    d4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_φ_t__2__.txt").readline()).coeff(diff(diff(x4, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    d5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),

    e1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    e2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    e3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    e4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_φ_t__2__.txt").readline()).coeff(diff(diff(x4, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
    e5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)).subs(inertia).subs(dict_for_subs, simultaneous=True),
}

other_vars_subs = {


}

