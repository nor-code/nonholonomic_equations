from main_file import *

mixed_coeff_eq5 = {
    free_5: parse_2_sympy_expression(open("../../resolve_second_diff/part3_3/free_4_0.txt").readline()).subs(inertia).subs(param_dict)
}
eq5 = eq5.subs(mixed_coeff_eq5)
with open("eqns/eq5.txt", "w") as out:
    out.write(transform_to_simpy(str(eq5)))
print("prepared eq5")