from main_file import *

mixed_coeff_eq1 = {
    a_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_0.txt").readline()).subs(param_dict),
    a_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_1.txt").readline()).subs(param_dict),
    a_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_2.txt").readline()).subs(param_dict),
    a_4: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_3.txt").readline()).subs(param_dict),
    a_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_4.txt").readline()).subs(param_dict),
    a_6: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_5.txt").readline()).subs(param_dict),
    a_7: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_6.txt").readline()).subs(param_dict),
    a_8: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_7.txt").readline()).subs(param_dict),
    a_9: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_8.txt").readline()).subs(param_dict),
    a_10: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_9.txt").readline()).subs(param_dict),
    a_11: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_10.txt").readline()).subs(param_dict),
    a_12: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_11.txt").readline()).subs(param_dict),
    a_13: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_12.txt").readline()).subs(param_dict),
    a_14: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_13.txt").readline()).subs(param_dict),
    a_15: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_14.txt").readline()).subs(param_dict),
    a_16: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_15.txt").readline()).subs(param_dict),
    a_17: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_16.txt").readline()).subs(param_dict),
    a_18: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_17.txt").readline()).subs(param_dict),
    a_19: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_18.txt").readline()).subs(param_dict),
    a_20: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_19.txt").readline()).subs(param_dict),
    a_21: parse_2_sympy_expression(open("../../resolve_second_diff/part3/matrix_0_20.txt").readline()).subs(param_dict),
    free_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3/free_0_0.txt").readline()).subs(param_dict)
}

eq1 = eq1.subs(mixed_coeff_eq1)
with open("eqns/eq1.txt", "w") as out:
    out.write(transform_to_simpy(str(eq1)))
print("prepared eq1")