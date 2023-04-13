from main_file import *
import sys
sys.setrecursionlimit(10000000)

mixed_coeff_eq5 = {
    free_7: -parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/free_term.txt").readline()).subs(inertia).subs(param_dict),
}
eq5 = eq5.subs(mixed_coeff_eq5)
with open("eqns/eq5.txt", "w") as out:
    out.write(transform_to_simpy(str(eq5)))
print("prepared eq5")