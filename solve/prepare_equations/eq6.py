from main_file import *

mixed_coeff_eq6 = {
    f_1: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_2.txt").readline()).coeff(diff(x, t) ** 2).subs(param_dict),
    f_2: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_y_t_.txt").readline()).coeff(diff(x, t) * diff(y, t)).subs(param_dict),
    f_3: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_α_t_.txt").readline()).coeff(diff(x, t) * diff(x1, t)).subs(param_dict),
    f_4: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_β_t_.txt").readline()).coeff(diff(x, t) * diff(x2, t)).subs(param_dict),
    f_5: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_γ_t_.txt").readline()).coeff(diff(x, t) * diff(x3, t)).subs(param_dict),
    f_6: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_x_t__d_ψ_t_.txt").readline()).coeff(diff(x, t) * diff(x5, t)).subs(param_dict),
    f_7: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_2.txt").readline()).coeff(diff(y, t) ** 2).subs(param_dict),
    f_8: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_α_t_.txt").readline()).coeff(diff(y, t) * diff(x1, t)).subs(param_dict),
    f_9: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_β_t_.txt").readline()).coeff(diff(y, t) * diff(x2, t)).subs(param_dict),
    f_10: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_γ_t_.txt").readline()).coeff(diff(y, t) * diff(x3, t)).subs(param_dict),
    f_11: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_y_t__d_ψ_t_.txt").readline()).coeff(diff(y, t) * diff(x5, t)).subs(param_dict),
    f_12: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_2.txt").readline()).coeff(diff(x1, t) ** 2).subs(param_dict),
    f_13: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_t__d_β_t_.txt").readline()).coeff(diff(x1, t) * diff(x2, t)).subs(param_dict),
    f_14: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_t__d_γ_t_.txt").readline()).coeff(diff(x1, t) * diff(x3, t)).subs(param_dict),
    f_15: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_α_t__d_ψ_t_.txt").readline()).coeff(diff(x1, t) * diff(x5, t)).subs(param_dict),
    f_16: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_β_2.txt").readline()).coeff(diff(x2, t) ** 2).subs(param_dict),
    f_17: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_β_t__d_γ_t_.txt").readline()).coeff(diff(x2, t) * diff(x3, t)).subs(param_dict),
    f_18: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_β_t__d_ψ_t_.txt").readline()).coeff(diff(x2, t) * diff(x5, t)).subs(param_dict),
    f_19: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_γ_2.txt").readline()).coeff(diff(x3, t) ** 2).subs(param_dict),
    f_20: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_γ_t__d_ψ_t_.txt").readline()).coeff(diff(x3, t) * diff(x5, t)).subs(param_dict),
    f_21: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq7/d_ψ_2.txt").readline()).coeff(diff(x5, t) ** 2).subs(param_dict),
    free_7: 0
}
eq6 = eq6.subs(mixed_coeff_eq6)
with open("eqns/eq6.txt", "w") as out:
    out.write(transform_to_simpy(str(eq6)))
print("prepared eq6")
