from main_file import *

mixed_coeff_eq3 = {
    free_3: parse_2_sympy_expression(open("../../resolve_second_diff/part3_3/free_2_0.txt").readline()).subs(inertia).subs(param_dict)
}
eq3 = eq3.subs(mixed_coeff_eq3)
with open("eqns/eq3.txt", "w") as out:
    out.write(transform_to_simpy(str(eq3)))
print("prepared eq3")