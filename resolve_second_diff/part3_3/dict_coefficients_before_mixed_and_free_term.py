from definitions.generic_coordinates import *
from utils.sympy_expression import parse_2_sympy_expression
from definitions.symengine_var import *
from definitions.coefficient_for_resolve import free_1, free_2, free_3, free_4, free_5

mixed_coeff_var = {
    a_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    a_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_t__d_δ_t_.txt").readline()).coeff(diff(x, t) * diff(x6, t)),
    a_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    a_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_y_t__d_δ_t_.txt").readline()).coeff(diff(y, t) * diff(x6, t)),
    a_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    a_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    a_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_α_t__d_δ_t_.txt").readline()).coeff(diff(x1, t) * diff(x6, t)),
    a_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_β_t__d_δ_t_.txt").readline()).coeff(diff(x2, t) * diff(x6, t)),
    a_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_δ_2.txt").readline()).coeff(diff(x6, t) ** 2),

    b_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    b_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_x_t__d_δ_t_.txt").readline()).coeff(diff(x, t) * diff(x6, t)),
    b_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    b_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_y_t__d_δ_t_.txt").readline()).coeff(diff(y, t) * diff(x6, t)),
    b_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    b_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    b_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_α_t__d_δ_t_.txt").readline()).coeff(diff(x1, t) * diff(x6, t)),
    b_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_β_t__d_δ_t_.txt").readline()).coeff(diff(x2, t) * diff(x6, t)),
    b_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_δ_2.txt").readline()).coeff(diff(x6, t) ** 2),

    c_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    c_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_x_t__d_δ_t_.txt").readline()).coeff(diff(x, t) * diff(x6, t)),
    c_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    c_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_y_t__d_δ_t_.txt").readline()).coeff(diff(y, t) * diff(x6, t)),
    c_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    c_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    c_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_α_t__d_δ_t_.txt").readline()).coeff(diff(x1, t) * diff(x6, t)),
    c_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_β_t__d_δ_t_.txt").readline()).coeff(diff(x2, t) * diff(x6, t)),
    c_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_δ_2.txt").readline()).coeff(diff(x6, t) ** 2),

    d_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    d_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_x_t__d_δ_t_.txt").readline()).coeff(diff(x, t) * diff(x6, t)),
    d_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    d_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_y_t__d_δ_t_.txt").readline()).coeff(diff(y, t) * diff(x6, t)),
    d_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    d_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    d_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_α_t__d_δ_t_.txt").readline()).coeff(diff(x1, t) * diff(x6, t)),
    d_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_β_t__d_δ_t_.txt").readline()).coeff(diff(x2, t) * diff(x6, t)),
    d_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_δ_2.txt").readline()).coeff(diff(x6, t) ** 2),

    e_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    e_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_x_t__d_δ_t_.txt").readline()).coeff(diff(x, t) * diff(x6, t)),
    e_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    e_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_y_t__d_δ_t_.txt").readline()).coeff(diff(y, t) * diff(x6, t)),
    e_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    e_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    e_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_α_t__d_δ_t_.txt").readline()).coeff(diff(x1, t) * diff(x6, t)),
    e_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_β_t__d_δ_t_.txt").readline()).coeff(diff(x2, t) * diff(x6, t)),
    e_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_δ_2.txt").readline()).coeff(diff(x6, t) ** 2),

}
print("initialized dict. of mixed coordinates")

dict_free_term_equations = {
    free_1: parse_2_sympy_expression(open("../../collect_parallel/eq3/free_term.txt").readline()),
    free_2: parse_2_sympy_expression(open("../../collect_parallel/eq6/free_term.txt").readline()),
    free_3: parse_2_sympy_expression(open("../../collect_parallel/eq8/free_term.txt").readline()),
    free_4: parse_2_sympy_expression(open("../../collect_parallel/eq9/free_term.txt").readline()),
    free_5: parse_2_sympy_expression(open("../../collect_parallel/eq10/free_term.txt").readline())
}
print("initialized dict. of free term equations (contains control moments and generic forces of gravity)")


