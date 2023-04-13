from main_file import *
import sys
sys.setrecursionlimit(10000000)

mixed_coeff_eq3 = {
    c_1: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_0.txt").readline()).subs(inertia).subs(param_dict),
    c_2: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_1.txt").readline()).subs(inertia).subs(param_dict),
    c_3: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_2.txt").readline()).subs(inertia).subs(param_dict),
    c_4: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_3.txt").readline()).subs(inertia).subs(param_dict),
    c_5: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_4.txt").readline()).subs(inertia).subs(param_dict),
    c_6: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_5.txt").readline()).subs(inertia).subs(param_dict),
    c_7: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_6.txt").readline()).subs(inertia).subs(param_dict),
    c_8: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_7.txt").readline()).subs(inertia).subs(param_dict),
    c_9: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_3/matrix_2_8.txt").readline()).subs(inertia).subs(param_dict),

    free_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3_3/free_2_0.txt").readline()).subs(inertia).subs(param_dict)
}
eq3 = eq3.subs(mixed_coeff_eq3)
with open("eqns/eq3.txt", "w") as out:
    out.write(transform_to_simpy(str(eq3)))
print("prepared eq3")