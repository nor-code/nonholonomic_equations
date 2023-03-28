from main_file import *

mixed_coeff_eq1 = {
    free_1: parse_2_sympy_expression(open("../../resolve_second_diff/part3_3/free_0_0.txt").readline()).subs(inertia).subs(param_dict)
}

eq1 = eq1.subs(mixed_coeff_eq1)
with open("eqns/eq1.txt", "w") as out:
    out.write(transform_to_simpy(str(eq1)))
print("prepared eq1")