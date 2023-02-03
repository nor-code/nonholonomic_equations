from main_file import *

mixed_coeff_eq5 = {
    e_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_0.txt").readline()).subs(param_dict),
    e_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_1.txt").readline()).subs(param_dict),
    e_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_2.txt").readline()).subs(param_dict),
    e_4: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_3.txt").readline()).subs(param_dict),
    e_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_4.txt").readline()).subs(param_dict),
    e_6: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_5.txt").readline()).subs(param_dict),
    e_7: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_6.txt").readline()).subs(param_dict),
    e_8: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_7.txt").readline()).subs(param_dict),
    e_9: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_8.txt").readline()).subs(param_dict),
    e_10: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_9.txt").readline()).subs(param_dict),
    e_11: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_10.txt").readline()).subs(param_dict),
    e_12: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_11.txt").readline()).subs(param_dict),
    e_13: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_12.txt").readline()).subs(param_dict),
    e_14: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_13.txt").readline()).subs(param_dict),
    e_15: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_14.txt").readline()).subs(param_dict),
    e_16: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_15.txt").readline()).subs(param_dict),
    e_17: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_16.txt").readline()).subs(param_dict),
    e_18: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_17.txt").readline()).subs(param_dict),
    e_19: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_18.txt").readline()).subs(param_dict),
    e_20: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_19.txt").readline()).subs(param_dict),
    e_21: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_4_20.txt").readline()).subs(param_dict),
    free_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3/free_4_0.txt").readline()).subs(param_dict)
}
eq5 = eq5.subs(mixed_coeff_eq5)
with open("eqns/eq5.txt", "w") as out:
    out.write(transform_to_simpy(str(eq5)))
print("prepared eq5")
