import time

from sympy import diff, sin, cos, together, fraction, simplify
from definitions.generic_coordinates import *
from definitions.coefficient_for_resolve import *
from definitions.constants import *
from definitions.moments import M_φ, M_ψ
from utils.sympy_expression import parse_2_sympy_expression
import sys
from  utils.latex_converter import print_in_latex
from utils.to_sympy_expression import transform_to_simpy


BEGIN = time.time()

u, v, p, q, s1, w1 = symbols("u, v, p, q, s1, w1")  # скорости x y x2 x5  x1 x6  (x, y, β, ψ,    α, δ)

p1, n, q1, r1 = symbols("p1, n, q1, r1")  # скорости x3, x4, x7, x8 (γ, φ, ε, τ) выражаются через неголономные связи


inertia = {
    J_px: M_p * R_p ** 2 / 4 + M_p * C_Mz ** 2,
    J_py: M_p * R_p ** 2 / 4 + M_p * C_Mz ** 2,
    J_pz: M_p * R_p ** 2 / 4,
    J_wx: m * r ** 2 / 4 + m * C_mz ** 2,
    J_wy: m * r ** 2 / 2 + m * C_mz ** 2,
    J_wz: m * r ** 2 / 4
}

param_dict = {
    C_mz: (0.081 - 0.026),
    C_Mz: 0.01,

    g: 10,
    R: 0.081,
    r: 0.026,
    m: 0.05,
    M: 0.137,
    M_p: 0.65,
    R_p: 0.08,

}

# подсистема на y и β
Y_Betta_Matrix = Matrix([
    [(C_Mz*M_p*r**2 - C_mz**2*R*m + C_mz**2*m*r - C_mz*R*m*r + C_mz*m*r**2 - J_wx*R + J_wx*r),              (r**2 * (C_Mz**2*M_p + J_px) + (R - r)**2 * (C_mz**2 * m + J_wx))],
    [r*(C_Mz * M_p + C_mz * m + (5*M/3 + M_p + m)*R), - ((C_Mz**2*M_p + C_Mz*M_p*R + J_px)*r - (C_mz**2*m + C_mz*R*m + J_wx)*(R - r))]
])
print(print_in_latex(Y_Betta_Matrix))

right_part = Matrix([
    [-(C_Mz * M_p + C_mz * m) * g * r**2],
    [(C_Mz * M_p + C_mz * m) * g * r]
])
print(print_in_latex(right_part))

result = Y_Betta_Matrix.inv() * right_part

result[0] = together(result[0])
y_top, y_bot = fraction(result[0])
print("y_top = ", print_in_latex(simplify(y_top)))
print("y_bot = ", print_in_latex(y_bot))

result[1] = together(result[1])
beta_top, beta_bot = fraction(result[1])
print("beta_top = ", print_in_latex(beta_top))
print("beta_bot = ", print_in_latex(beta_bot))


eq_x = -(R*g*(C_Mz*M_p + C_mz*m) * x3)/((J_py + J_wy) + (M_p + m + 5*M/3)*R**2 + 2*(C_Mz*M_p + C_mz*m) + (C_Mz**2 * M_p + C_mz**2 * m))
print(print_in_latex(eq_x))
print("eq_x = ", print_in_latex(eq_x))
eq_x = eq_x.subs(inertia).subs(param_dict)
print("eq_x = ", print_in_latex(eq_x))

eq_y = (result[0] * x2).subs(inertia).subs(param_dict)
print("eq_y = ", print_in_latex(eq_y))
eq_beta = (result[1] * x2).subs(inertia).subs(param_dict)
print("eq_beta = ", print_in_latex(eq_beta))

eq_alpha = 0
eq_delta = 0
eq_psi = 0

eq7 = parse_2_sympy_expression(open("../../kinematic/part2/d_gamma.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): s1,
        diff(x2, t): p,
        diff(x5, t): q,
        diff(x6, t): w1
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_gamma_bottom.txt").readline())
print("eq_gamma = ", print_in_latex(eq7))
eq7 = eq7.subs(inertia)
eq7 = eq7.subs(param_dict)
print("eq_gamma = ", print_in_latex(eq7))


eq8 = parse_2_sympy_expression(open("../../kinematic/part2/d_eps.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): s1,
        diff(x2, t): p,
        diff(x5, t): q,
        diff(x6, t): w1
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_eps_bottom.txt").readline())
print("eq_eps = ", print_in_latex(eq8))
eq8 = eq8.subs(inertia)
eq8 = eq8.subs(param_dict)
print("eq_eps = ", print_in_latex(eq8))


eq9 = parse_2_sympy_expression(open("../../kinematic/part2/d_phi.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): s1,
        diff(x2, t): p,
        diff(x5, t): q,
        diff(x6, t): w1
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_phi_bottom.txt").readline())
print("eq_phi = ", print_in_latex(eq9))
eq9 = eq9.subs(inertia)
eq9 = eq9.subs(param_dict)
print("eq_phi = ", print_in_latex(eq9))


eq10 = parse_2_sympy_expression(open("../../kinematic/part2/d_tau.txt").readline()).subs(
    {
        diff(x, t): u,
        diff(y, t): v,
        diff(x1, t): s1,
        diff(x2, t): p,
        diff(x5, t): q,
        diff(x6, t): w1
    }
)/parse_2_sympy_expression(open("../../kinematic/part2/d_tau_bottom.txt").readline())
print("eq_tau = ", print_in_latex(eq10))
eq10 = eq10.subs(inertia)
eq10 = eq10.subs(param_dict)
print("eq_tau = ", print_in_latex(eq10))


print("eq_x = ", eq_x)
print("eq_y = ", eq_y)
print("eq_alpha = 0")
print("eq_beta = ", eq_beta)
print("eq_delta = 0")
print("eq_psi = 0")
print("eq7 = ", eq7)
print("eq8 = ", eq8)
print("eq9 = ", eq9)
print("eq10 = ", eq10)
