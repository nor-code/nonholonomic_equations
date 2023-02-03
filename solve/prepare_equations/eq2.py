from main_file import *

mixed_coeff_eq2 = {
    b_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_0.txt").readline()).subs(param_dict),
    b_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_1.txt").readline()).subs(param_dict),
    b_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_2.txt").readline()).subs(param_dict),
    b_4: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_3.txt").readline()).subs(param_dict),
    b_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_4.txt").readline()).subs(param_dict),
    b_6: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_5.txt").readline()).subs(param_dict),
    b_7: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_6.txt").readline()).subs(param_dict),
    b_8: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_7.txt").readline()).subs(param_dict),
    b_9: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_8.txt").readline()).subs(param_dict),
    b_10: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_9.txt").readline()).subs(param_dict),
    b_11: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_10.txt").readline()).subs(param_dict),
    b_12: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_11.txt").readline()).subs(param_dict),
    b_13: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_12.txt").readline()).subs(param_dict),
    b_14: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_13.txt").readline()).subs(param_dict),
    b_15: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_14.txt").readline()).subs(param_dict),
    b_16: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_15.txt").readline()).subs(param_dict),
    b_17: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_16.txt").readline()).subs(param_dict),
    b_18: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_17.txt").readline()).subs(param_dict),
    b_19: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_18.txt").readline()).subs(param_dict),
    b_20: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_19.txt").readline()).subs(param_dict),
    b_21: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_1_20.txt").readline()).subs(param_dict),
    free_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3/free_1_0.txt").readline()).subs(param_dict)
}
eq2 = eq2.subs(mixed_coeff_eq2)
with open("eqns/eq2.txt", "w") as out:
    out.write(transform_to_simpy(str(eq2)))
print("prepared eq2")
