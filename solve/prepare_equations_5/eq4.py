from main_file import *
import sys
sys.setrecursionlimit(10000000)

mixed_coeff_eq4 = {
    d_1: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_0.txt").readline()).subs(inertia).subs(param_dict),
    d_2: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_1.txt").readline()).subs(inertia).subs(param_dict),
    d_3: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_2.txt").readline()).subs(inertia).subs(param_dict),
    d_4: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_3.txt").readline()).subs(inertia).subs(param_dict),
    d_5: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_4.txt").readline()).subs(inertia).subs(param_dict),
    d_6: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_5.txt").readline()).subs(inertia).subs(param_dict),
    d_7: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_6.txt").readline()).subs(inertia).subs(param_dict),
    d_8: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_7.txt").readline()).subs(inertia).subs(param_dict),
    d_9: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_3_8.txt").readline()).subs(inertia).subs(param_dict),

    free_4: parse_2_sympy_expression(open("../../resolve_second_diff/part3_5/free_3_0.txt").readline()).subs(inertia).subs(param_dict)
}
eq4 = eq4.subs(mixed_coeff_eq4)
with open("eqns/eq4.txt", "w") as out:
    out.write(transform_to_simpy(str(eq4)))
print("prepared eq4")