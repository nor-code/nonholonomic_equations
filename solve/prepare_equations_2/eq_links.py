from main_file import *

eq5 = parse_2_sympy_expression(open("../../kinematic/part2/d_gamma.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x2, t): p,
        diff(x5, t): q
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_gamma_bottom.txt").readline())
eq5 = eq5.subs(param_dict)
with open("eqns/eq5.txt", "w") as out:
    out.write(transform_to_simpy(str(eq5)))
print("prepared eq5")


eq6 = parse_2_sympy_expression(open("../../kinematic/part2/d_eps.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x2, t): p,
        diff(x5, t): q
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_eps_bottom.txt").readline())
eq6 = eq6.subs(param_dict)
with open("eqns/eq6.txt", "w") as out:
    out.write(transform_to_simpy(str(eq6)))
print("prepared eq6")


eq7 = parse_2_sympy_expression(open("../../kinematic/part2/d_phi.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x2, t): p,
        diff(x5, t): q
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_phi_bottom.txt").readline())
eq7 = eq7.subs(param_dict)
with open("eqns/eq7.txt", "w") as out:
    out.write(transform_to_simpy(str(eq7)))
print("prepared eq7")


eq8 = parse_2_sympy_expression(open("../../kinematic/part2/d_tau.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x2, t): p,
        diff(x5, t): q
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_tau_bottom.txt").readline())
eq8 = eq8.subs(param_dict)
with open("eqns/eq8.txt", "w") as out:
    out.write(transform_to_simpy(str(eq8)))
print("prepared eq8")

END = time.time()
print("TOTAL TIME FOR PREPARED ALL EQUATIONS %.2f [m]" % ((END - BEGIN)/60))
