from main_file import *

mixed_coeff_eq6 = {
    e_1: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_0.txt").readline()).subs(inertia).subs(param_dict),
    e_2: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_1.txt").readline()).subs(inertia).subs(param_dict),
    e_3: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_2.txt").readline()).subs(inertia).subs(param_dict),
    e_4: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_3.txt").readline()).subs(inertia).subs(param_dict),
    e_5: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_4.txt").readline()).subs(inertia).subs(param_dict),
    e_6: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_5.txt").readline()).subs(inertia).subs(param_dict),
    e_7: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_6.txt").readline()).subs(inertia).subs(param_dict),
    e_8: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_7.txt").readline()).subs(inertia).subs(param_dict),
    e_9: parse_2_sympy_expression(open(
        "../../resolve_second_diff/part3_5/matrix_4_8.txt").readline()).subs(inertia).subs(param_dict),

    free_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3_5/free_4_0.txt").readline()).subs(inertia).subs(param_dict)

}
eq6 = eq6.subs(mixed_coeff_eq6)
with open("eqns/eq6.txt", "w") as out:
    out.write(transform_to_simpy(str(eq6)))
print("prepared eq6")
