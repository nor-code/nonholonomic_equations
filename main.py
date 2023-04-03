# import Dynamics
# if __name__ == "__main__":
#     Dynamics.print_equations_for_Wolfram_Mathematica()
import time

# import numpy
# from aesara import pp
# t = at.dscalar('t')
# x = aesara.function([t], )
# y = x ** 2
# gy = at.grad(y, x)
# pp(gy)  # print out the gradient prior to optimization
# '((fill((x ** TensorConstant{2}), TensorConstant{1.0}) * TensorConstant{2}) * (x ** (TensorConstant{2} - TensorConstant{1})))'
# f = aesara.function([x], gy)
#
# t = f.grad(x)

import sympy
import tqdm
from sympy import *
import symengine as se
from definitions.generic_coordinates import *
from definitions.constants import *
from definitions.coefficient_for_resolve import *
from definitions.moments import *
from utils.common import remove_current_and_above_smallness_from_one_term, \
    remove_required_and_above_smallness_from_expression, simplification_expression, \
    expand_and_collect_term_before_derivatives_and_lambda, simplify_determinant
from utils.to_sympy_expression import transform_to_simpy


det = - 1.90851778423831e-31
eq1 = (-1.97691353227865e-31*x1 - 3.82303622092819e-30*x2 - 5.53079647595135e-30*x3 + 1.97691353227865e-31*x6 + 4.21534638775867e-33*x7 - 1.5777680732415e-34*x8 - 5.56266418986307e-32*x5 + 8.90948983600028e-32) / det
eq2 = (-2.48925491476809e-31*x1 - 3.0704252134923e-29*x2 - 2.04934187722853e-29*x3 + 2.48925491476809e-31*x6 - 1.22063281540091e-30*x7 + 1.24735481581263e-32*x8 + 1.68059349894109e-30*x5 + 4.05421529860773e-30) / det
eq3 = (-2.49201582209273e-30*x1 + 5.2044327855804e-28*x2 + 5.1915402936477e-28*x3 + 2.49201582209273e-30*x6 - 7.12971959567292e-30*x7 + 7.28113933758136e-32*x8 - 1.4242312856007e-28*x5 - 1.64864276595099e-28) / det
eq4 = (-2.56310474617209e-29*x1 + 1.53693399181981e-28*x2 - 2.9200095981471e-28*x3 + 2.56310474617209e-29*x6 - 1.29562046697849e-31*x7 - 5.98394648472464e-34*x8 + 6.5196526483529e-29*x5 - 7.18487386453375e-30) / det
eq5 = (2.91293769865105e-5*x1 - 0.00642178321401644*x2 - 0.00195558087339103*x3 - 2.91293769865105e-5*x6 + 5.49762612114189e-6*x7 - 5.33358684656883e-8*x8 + 8.85794729076537e-7*x5) / det

print(eq1)
print(eq2)
print(eq3)
print(eq4)
print(eq5)
u = 1.30593251407489e-38*R_p**8 - 2.513749125773e-25*R_p**6 - 1.31359896816564e-26*R_p**4 - 9.39155115099572e-29*R_p**2 - 6.03963248849376e-32
u = u.subs({R_p: 0.081})
print(u)

{a1: 0, a2: 0, a3: J_pz, a4: 0, a5: 0,
 b1: 0, b2: r*(C_Mz*M_p*r - C_mz*R*m + C_mz*m*r), b3: 0, b4: -C_Mz**2*M_p*r**2 - C_mz**2*R**2*m + 2*C_mz**2*R*m*r - C_mz**2*m*r**2 - J_px*r**2 - J_wx*R**2 + 2*J_wx*R*r - J_wx*r**2, b5: 0,
 c1: 0, c2: 0, c3: 0, c4: 0, c5: 2*M*R**2,
 d1: 0, d2: r*(-3*C_Mz*M_p - 3*C_mz*m - 5*M*R - 3*M_p*R - 3*R*m), d3: 0, d4: 3*C_Mz**2*M_p*r + 3*C_Mz*M_p*R*r - 3*C_mz**2*R*m + 3*C_mz**2*m*r - 3*C_mz*R**2*m + 3*C_mz*R*m*r + 3*J_px*r - 3*J_wx*R + 3*J_wx*r, d5: 0,
 e1: 3*C_Mz**2*M_p + 6*C_Mz*M_p*R + 3*C_mz**2*m + 6*C_mz*R*m + 3*J_py + 3*J_wy + 5*M*R**2 + 3*M_p*R**2 + 3*R**2*m, e2: 0, e3: 0, e4: 0, e5: 0}