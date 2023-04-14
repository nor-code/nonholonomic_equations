import time

from sympy import simplify

from Kinematics import *
from utils.common import expand_and_collect_term_before_first_derivatives, simplification_expression, \
    remove_required_and_above_smallness_from_expression, is_remove_small_term_with_velocities
from utils.latex_converter import print_in_latex
from utils.to_sympy_expression import transform_to_simpy


t1 = time.time()


def remove_small_term(eq_i):
    res = 0
    for term_of_eq_i in eq_i.args:
        if not is_remove_small_term_with_velocities(term_of_eq_i):
            res += term_of_eq_i
    return res


ORDER = 2
eq1 = remove_small_term(remove_required_and_above_smallness_from_expression(simplification_expression(nonholonomic_links[0]), order=ORDER))
eq2 = remove_small_term(remove_required_and_above_smallness_from_expression(simplification_expression(nonholonomic_links[1]), order=ORDER))
eq3 = remove_small_term(remove_required_and_above_smallness_from_expression(simplification_expression(nonholonomic_links[2]), order=ORDER))
eq4 = remove_small_term(remove_required_and_above_smallness_from_expression(simplification_expression(nonholonomic_links[3]), order=ORDER))
eq5 = remove_small_term(remove_required_and_above_smallness_from_expression(simplification_expression(nonholonomic_links[4]), order=ORDER))

print(print_in_latex(eq1))
print(print_in_latex(eq2))
print(print_in_latex(eq3))
print(print_in_latex(eq4))
print(print_in_latex(eq5))

var_for_resolve = [Derivative(x2, t), Derivative(x3, t), Derivative(x7, t), Derivative(x8, t)]

# A0 = 0, A1 != 0, b != 0
(A0, A1), b = linear_ode_to_matrix(
    [eq1, eq2, eq3, eq4],
    var_for_resolve,
    t, 1
)

b = -b

print("A1 = ", A1)
A1 = sym.simplify(A1)
print("simplified A1 = ", A1)

A1_inv = A1.inv()
print("inv A1 = ", A1_inv)

solution = A1_inv * b
print(var_for_resolve[0], " : ", solution.row(0)[0])
print(var_for_resolve[1], " : ", solution.row(1)[0])
print(var_for_resolve[2], " : ", solution.row(2)[0])
print(var_for_resolve[3], " : ", solution.row(3)[0])


kinematic_equations = [solution.row(0)[0], solution.row(1)[0], solution.row(2)[0], solution.row(3)[0]]
for i in range(len(kinematic_equations)):
    with open("kin_eq" + str(i) + ".txt", "w") as out:
        out.write(transform_to_simpy(str(kinematic_equations[i])))

t2 = time.time()

print("finished resolve kinematic equations. spent time = %.2f [m] or %.2f [s]" % (((t2 - t1) / 60), (t2 - t1)))
