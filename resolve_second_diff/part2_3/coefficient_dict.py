from definitions.generic_coordinates import *
from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *

main_vars_subs = {
    a1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    a2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    a3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    a4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t)),
    a5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),

    b1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    b2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    b3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    b4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t)),
    b5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),

    c1: parse_2_sympy_expression(open(
         "../../collect_parallel/eq8/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    c2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    c3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    c4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t)),
    c5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),

    d1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    d2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    d3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    d4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t)),
    d5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),

    e1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    e2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    e3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    e4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t)),
    e5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),
}

other_vars_subs = {


}

