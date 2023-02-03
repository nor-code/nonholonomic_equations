from main_file import *

mixed_coeff_eq4 = {
    d_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_0.txt").readline()).subs(param_dict),
    d_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_1.txt").readline()).subs(param_dict),
    d_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_2.txt").readline()).subs(param_dict),
    d_4: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_3.txt").readline()).subs(param_dict),
    d_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_4.txt").readline()).subs(param_dict),
    d_6: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_5.txt").readline()).subs(param_dict),
    d_7: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_6.txt").readline()).subs(param_dict),
    d_8: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_7.txt").readline()).subs(param_dict),
    d_9: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_8.txt").readline()).subs(param_dict),
    d_10: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_9.txt").readline()).subs(param_dict),
    d_11: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_10.txt").readline()).subs(param_dict),
    d_12: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_11.txt").readline()).subs(param_dict),
    d_13: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_12.txt").readline()).subs(param_dict),
    d_14: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_13.txt").readline()).subs(param_dict),
    d_15: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_14.txt").readline()).subs(param_dict),
    d_16: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_15.txt").readline()).subs(param_dict),
    d_17: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_16.txt").readline()).subs(param_dict),
    d_18: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_17.txt").readline()).subs(param_dict),
    d_19: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_18.txt").readline()).subs(param_dict),
    d_20: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_19.txt").readline()).subs(param_dict),
    d_21: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_3_20.txt").readline()).subs(param_dict),
    free_4: parse_2_sympy_expression(open("../../resolve_second_diff/part3/free_3_0.txt").readline()).subs(param_dict)
}
eq4 = eq4.subs(mixed_coeff_eq4)
with open("eqns/eq4.txt", "w") as out:
    out.write(transform_to_simpy(str(eq4)))
print("prepared eq4")