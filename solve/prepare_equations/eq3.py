from main_file import *

mixed_coeff_eq3 = {
    c_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_0.txt").readline()).subs(param_dict),
    c_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_1.txt").readline()).subs(param_dict),
    c_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_2.txt").readline()).subs(param_dict),
    c_4: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_3.txt").readline()).subs(param_dict),
    c_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_4.txt").readline()).subs(param_dict),
    c_6: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_5.txt").readline()).subs(param_dict),
    c_7: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_6.txt").readline()).subs(param_dict),
    c_8: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_7.txt").readline()).subs(param_dict),
    c_9: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_8.txt").readline()).subs(param_dict),
    c_10: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_9.txt").readline()).subs(param_dict),
    c_11: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_10.txt").readline()).subs(param_dict),
    c_12: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_11.txt").readline()).subs(param_dict),
    c_13: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_12.txt").readline()).subs(param_dict),
    c_14: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_13.txt").readline()).subs(param_dict),
    c_15: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_14.txt").readline()).subs(param_dict),
    c_16: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_15.txt").readline()).subs(param_dict),
    c_17: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_16.txt").readline()).subs(param_dict),
    c_18: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_17.txt").readline()).subs(param_dict),
    c_19: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_18.txt").readline()).subs(param_dict),
    c_20: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_19.txt").readline()).subs(param_dict),
    c_21: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_2_20.txt").readline()).subs(param_dict),
    free_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3/free_2_0.txt").readline()).subs(param_dict)
}
eq3 = eq3.subs(mixed_coeff_eq3)
with open("eqns/eq3.txt", "w") as out:
    out.write(transform_to_simpy(str(eq3)))
print("prepared eq3")