import time

from Kinematics import *
from utils.common import expand_and_collect_term_before_first_derivatives
from utils.to_sympy_expression import transform_to_simpy


t1 = time.time()

# A0 = 0, A1 != 0, b != 0
(A0, A1), b = linear_ode_to_matrix(
    [nonholonomic_links[0], nonholonomic_links[1], nonholonomic_links[2], nonholonomic_links[4]],
    [Derivative(x4, t), Derivative(x6, t), Derivative(x7, t), Derivative(x8, t)],
    t, 1
)

print("A1 = ", A1)
A1 = sym.simplify(A1)
print("simplified A1 = ", A1)

A1_inv = A1.inv()
print("inv A1 = ", A1_inv)

solution = A1_inv * b
print("d_phi ", solution.row(0)[0])
print("d_del ", solution.row(1)[0])
print("d_eps ", solution.row(2)[0])
print("d_tau ", solution.row(3)[0])


kinematic_equations = [solution.row(0)[0], solution.row(1)[0], solution.row(2)[0], solution.row(3)[0]]
for i in range(len(kinematic_equations)):
    with open("kin_eq" + str(i) + ".txt", "w") as out:
        out.write(transform_to_simpy(str(kinematic_equations[i])))

t2 = time.time()

print("finished resolve kinematic equations. spent time = %.2f [m] or %.2f [s]" % (((t2 - t1) / 60), (t2 - t1)))
