from main_file import *

mixed_coeff_eq5 = {
    free_5: -parse_2_sympy_expression(open("../../collect_parallel/eq8/free_term.txt").readline()).subs(inertia).subs(param_dict)
            /parse_2_sympy_expression(open("../../collect_parallel/eq8/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)).subs(inertia).subs(param_dict),
}
eq5 = eq5.subs(mixed_coeff_eq5)
with open("eqns/eq5.txt", "w") as out:
    out.write(transform_to_simpy(str(eq5)))
print("prepared eq5")