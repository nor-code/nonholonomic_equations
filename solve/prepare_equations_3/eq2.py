from main_file import *

mixed_coeff_eq2 = {
    free_2: parse_2_sympy_expression(open("../../resolve_second_diff/part3_3/free_1_0.txt").readline()).subs(inertia).subs(param_dict)
}
eq2 = eq2.subs(mixed_coeff_eq2)
with open("eqns/eq2.txt", "w") as out:
    out.write(transform_to_simpy(str(eq2)))
print("prepared eq2")
