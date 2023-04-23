from definitions.generic_coordinates import *
from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *

mixed_coeff_var = {
    # a_1: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    # a_2: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    # a_3: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    # a_4: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    # a_5: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    # a_6: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    # a_7: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    # a_8: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    # a_9: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    # a_10: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq6/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),
    #
    # b_1: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    # b_2: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    # b_3: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    # b_4: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    # b_5: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    # b_6: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    # b_7: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    # b_8: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    # b_9: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    # b_10: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq9/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),
    #
    # c_1: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    # c_2: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    # c_3: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    # c_4: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    # c_5: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    # c_6: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    # c_7: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    # c_8: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    # c_9: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    # c_10: parse_2_sympy_expression(open(
    #     "../../collect_parallel/eq10/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),
}
print("initialized dict. of mixed coordinates")

dict_free_term_equations = {
    free_1: parse_2_sympy_expression(open("../../collect_parallel/eq3/free_term.txt").readline()),
    free_2: parse_2_sympy_expression(open("../../collect_parallel/eq9/free_term.txt").readline()),
    free_3: parse_2_sympy_expression(open("../../collect_parallel/eq10/free_term.txt").readline())
}
print("initialized dict. of free term equations (contains control moments and generic forces of gravity)")


