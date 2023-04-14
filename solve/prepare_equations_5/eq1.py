from main_file import *
import sys
sys.setrecursionlimit(10000000)

mixed_coeff_eq1 = {
    a_1: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_0.txt").readline()).subs(inertia).subs(param_dict),
    a_2: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_1.txt").readline()).subs(inertia).subs(param_dict),
    a_3: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_2.txt").readline()).subs(inertia).subs(param_dict),
    a_4: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_3.txt").readline()).subs(inertia).subs(param_dict),
    a_5: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_4.txt").readline()).subs(inertia).subs(param_dict),
    a_6: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_5.txt").readline()).subs(inertia).subs(param_dict),
    a_7: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_6.txt").readline()).subs(inertia).subs(param_dict),
    a_8: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_7.txt").readline()).subs(inertia).subs(param_dict),
    a_9: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_0_8.txt").readline()).subs(inertia).subs(param_dict),

    free_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3_5/free_0_0.txt").readline()).subs(inertia).subs(param_dict)
}

eq1 = eq1.subs(mixed_coeff_eq1)
with open("eqns/eq1.txt", "w") as out:
    out.write(transform_to_simpy(str(eq1)))
print("prepared eq1")