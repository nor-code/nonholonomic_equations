from definitions.generic_coordinates import *
from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *

mixed_coeff_var = {
    a_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    a_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    a_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_x_t__d_α_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    a_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    a_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_x_t__d_γ_t_.txt").readline()).coeff(diff(x, t) * diff(x3, t)),
    a_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    a_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    a_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    a_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    a_10: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_y_t__d_γ_t_.txt").readline()).coeff(diff(y, t) * diff(x3, t)),
    a_11: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    a_12: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    a_13: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    a_14: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_α_t__d_γ_t_.txt").readline()).coeff(diff(x1, t) * diff(x3, t)),
    a_15: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_α_t__d_ψ_t_.txt").readline()).coeff(diff(x1, t) * diff(x5, t)),
    a_16: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    a_17: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_β_t__d_γ_t_.txt").readline()).coeff(diff(x2, t) * diff(x3, t)),
    a_18: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    a_19: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_γ_2.txt").readline()).coeff(diff(x3, t) ** 2),
    a_20: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_γ_t__d_ψ_t_.txt").readline()).coeff(diff(x3, t) * diff(x5, t)),
    a_21: parse_2_sympy_expression(open(
        "../../collect_parallel/eq1/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),

    b_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    b_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    b_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_x_t__d_α_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    b_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    b_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_x_t__d_γ_t_.txt").readline()).coeff(diff(x, t) * diff(x3, t)),
    b_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    b_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    b_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    b_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    b_10: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_y_t__d_γ_t_.txt").readline()).coeff(diff(y, t) * diff(x3, t)),
    b_11: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    b_12: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    b_13: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    b_14: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_α_t__d_γ_t_.txt").readline()).coeff(diff(x1, t) * diff(x3, t)),
    b_15: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_α_t__d_ψ_t_.txt").readline()).coeff(diff(x1, t) * diff(x5, t)),
    b_16: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    b_17: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_β_t__d_γ_t_.txt").readline()).coeff(diff(x2, t) * diff(x3, t)),
    b_18: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    b_19: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_γ_2.txt").readline()).coeff(diff(x3, t) ** 2),
    b_20: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_γ_t__d_ψ_t_.txt").readline()).coeff(diff(x3, t) * diff(x5, t)),
    b_21: parse_2_sympy_expression(open(
        "../../collect_parallel/eq2/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),

    c_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    c_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    c_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_t__d_α_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    c_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    c_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_t__d_γ_t_.txt").readline()).coeff(diff(x, t) * diff(x3, t)),
    c_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    c_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    c_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    c_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    c_10: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_y_t__d_γ_t_.txt").readline()).coeff(diff(y, t) * diff(x3, t)),
    c_11: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    c_12: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    c_13: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    c_14: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_α_t__d_γ_t_.txt").readline()).coeff(diff(x1, t) * diff(x3, t)),
    c_15: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_α_t__d_ψ_t_.txt").readline()).coeff(diff(x1, t) * diff(x5, t)),
    c_16: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    c_17: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_β_t__d_γ_t_.txt").readline()).coeff(diff(x2, t) * diff(x3, t)),
    c_18: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    c_19: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_γ_2.txt").readline()).coeff(diff(x3, t) ** 2),
    c_20: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_γ_t__d_ψ_t_.txt").readline()).coeff(diff(x3, t) * diff(x5, t)),
    c_21: parse_2_sympy_expression(open(
        "../../collect_parallel/eq3/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),

    d_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    d_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    d_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_x_t__d_α_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    d_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    d_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_x_t__d_γ_t_.txt").readline()).coeff(diff(x, t) * diff(x3, t)),
    d_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    d_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    d_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    d_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    d_10: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_y_t__d_γ_t_.txt").readline()).coeff(diff(y, t) * diff(x3, t)),
    d_11: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    d_12: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    d_13: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    d_14: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_α_t__d_γ_t_.txt").readline()).coeff(diff(x1, t) * diff(x3, t)),
    d_15: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_α_t__d_ψ_t_.txt").readline()).coeff(diff(x1, t) * diff(x5, t)),
    d_16: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    d_17: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_β_t__d_γ_t_.txt").readline()).coeff(diff(x2, t) * diff(x3, t)),
    d_18: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    d_19: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_γ_2.txt").readline()).coeff(diff(x3, t) ** 2),
    d_20: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_γ_t__d_ψ_t_.txt").readline()).coeff(diff(x3, t) * diff(x5, t)),
    d_21: parse_2_sympy_expression(open(
        "../../collect_parallel/eq4/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),

    e_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    e_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    e_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_x_t__d_α_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    e_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    e_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_x_t__d_γ_t_.txt").readline()).coeff(diff(x, t) * diff(x3, t)),
    e_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    e_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    e_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    e_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    e_10: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_y_t__d_γ_t_.txt").readline()).coeff(diff(y, t) * diff(x3, t)),
    e_11: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    e_12: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    e_13: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    e_14: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_α_t__d_γ_t_.txt").readline()).coeff(diff(x1, t) * diff(x3, t)),
    e_15: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_α_t__d_ψ_t_.txt").readline()).coeff(diff(x1, t) * diff(x5, t)),
    e_16: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    e_17: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_β_t__d_γ_t_.txt").readline()).coeff(diff(x2, t) * diff(x3, t)),
    e_18: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    e_19: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_γ_2.txt").readline()).coeff(diff(x3, t) ** 2),
    e_20: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_γ_t__d_ψ_t_.txt").readline()).coeff(diff(x3, t) * diff(x5, t)),
    e_21: parse_2_sympy_expression(open(
        "../../collect_parallel/eq5/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),

    f_1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_2.txt").readline()).coeff(diff(x, t) ** 2),
    f_2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)),
    f_3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_α_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)),
    f_4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)),
    f_5: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_γ_t_.txt").readline()).coeff(diff(x, t) * diff(x3, t)),
    f_6: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)),
    f_7: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_2.txt").readline()).coeff(diff(y, t) ** 2),
    f_8: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)),
    f_9: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)),
    f_10: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_γ_t_.txt").readline()).coeff(diff(y, t) * diff(x3, t)),
    f_11: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)),
    f_12: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2),
    f_13: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)),
    f_14: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_t__d_γ_t_.txt").readline()).coeff(diff(x1, t) * diff(x3, t)),
    f_15: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_t__d_ψ_t_.txt").readline()).coeff(diff(x1, t) * diff(x5, t)),
    f_16: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2),
    f_17: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_β_t__d_γ_t_.txt").readline()).coeff(diff(x2, t) * diff(x3, t)),
    f_18: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)),
    f_19: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_γ_2.txt").readline()).coeff(diff(x3, t) ** 2),
    f_20: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_γ_t__d_ψ_t_.txt").readline()).coeff(diff(x3, t) * diff(x5, t)),
    f_21: parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2),
}
print("initialized dict. of mixed coordinates")

dict_free_term_equations = {
    free_1: parse_2_sympy_expression(open("../../collect_parallel/eq1/free_term.txt").readline()),
    free_2: parse_2_sympy_expression(open("../../collect_parallel/eq2/free_term.txt").readline()),
    free_3: parse_2_sympy_expression(open("../../collect_parallel/eq3/free_term.txt").readline()),
    free_4: parse_2_sympy_expression(open("../../collect_parallel/eq4/free_term.txt").readline()),
    free_5: parse_2_sympy_expression(open("../../collect_parallel/eq5/free_term.txt").readline()),
    free_7: parse_2_sympy_expression(open("../../collect_parallel/eq7/free_term.txt").readline()),
}
print("initialized dict. of free term equations (contains control moments and generic forces of gravity)")


