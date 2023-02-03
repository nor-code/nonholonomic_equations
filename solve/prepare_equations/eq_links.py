from main_file import *

eq7 = parse_2_sympy_expression(open("../../kinematic/part2/d_del.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): p,
        diff(x2, t): q,
        diff(x3, t): r,
        diff(x5, t): h
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_del_bottom.txt").readline())
eq7 = eq7.subs(param_dict)
with open("eqns/eq7.txt", "w") as out:
    out.write(transform_to_simpy(str(eq7)))
print("prepared eq7")


eq8 = parse_2_sympy_expression(open("../../kinematic/part2/d_eps.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): p,
        diff(x2, t): q,
        diff(x3, t): r,
        diff(x5, t): h
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_eps_bottom.txt").readline())
eq8 = eq8.subs(param_dict)
with open("eqns/eq8.txt", "w") as out:
    out.write(transform_to_simpy(str(eq8)))
print("prepared eq8")


eq9 = parse_2_sympy_expression(open("../../kinematic/part2/d_phi.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): p,
        diff(x2, t): q,
        diff(x3, t): r,
        diff(x5, t): h
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_phi_bottom.txt").readline())
eq9 = eq9.subs(param_dict)
with open("eqns/eq9.txt", "w") as out:
    out.write(transform_to_simpy(str(eq9)))
print("prepared eq9")


eq10 = parse_2_sympy_expression(open("../../kinematic/part2/d_tau.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): p,
        diff(x2, t): q,
        diff(x3, t): r,
        diff(x5, t): h
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_tau_bottom.txt").readline())
eq10 = eq10.subs(param_dict)
with open("eqns/eq10.txt", "w") as out:
    out.write(transform_to_simpy(str(eq10)))
print("prepared eq10")

END = time.time()
print("TOTAL TIME FOR PREPARED ALL EQUATIONS %.2f [m]" % ((END - BEGIN)/60))
