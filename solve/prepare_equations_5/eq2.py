from main_file import *
import sys
sys.setrecursionlimit(10000000)

mixed_coeff_eq2 = {
    b_1: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_0.txt").readline()).subs(inertia).subs(param_dict),
    b_2: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_1.txt").readline()).subs(inertia).subs(param_dict),
    b_3: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_2.txt").readline()).subs(inertia).subs(param_dict),
    b_4: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_3.txt").readline()).subs(inertia).subs(param_dict),
    b_5: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_4.txt").readline()).subs(inertia).subs(param_dict),
    b_6: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_5.txt").readline()).subs(inertia).subs(param_dict),
    b_7: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_6.txt").readline()).subs(inertia).subs(param_dict),
    b_8: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_7.txt").readline()).subs(inertia).subs(param_dict),
    b_9: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_1_8.txt").readline()).subs(inertia).subs(param_dict),

    free_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3_5/free_1_0.txt").readline()).subs(inertia).subs(param_dict)
}
eq2 = eq2.subs(mixed_coeff_eq2)
with open("eqns/eq2.txt", "w") as out:
    out.write(transform_to_simpy(str(eq2)))
print("prepared eq2")
