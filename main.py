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

det = -7.42832185376219e-23

eq1 = (-2.17315176280445e-24*x1 - 8.45285769554097e-24*x2 + 5.99152336268184e-23*x3 + 2.17315176280445e-24*x6 + 8.43553334021883e-26*x5 + 1.29277712781996e-23) / det
eq2 = (-2.79740722648263e-24*x1 + 4.27813666560385e-22*x2 + 9.38137145258243e-24*x3 + 2.79740722648263e-24*x6 + 7.53264872726334e-23*x5 - 1.30535964648204e-23) / det
eq3 = (-6.46949010235949e-22*x1 + 2.44514928137893e-21*x2 + 2.29426671260204e-22*x3 + 6.46949010235949e-22*x6 + 2.57584614435016e-22*x5 - 3.75450278368382e-23) / det
eq4 = (-3.26694843060306e-21*x1 + 1.44948090739847e-20*x2 - 2.73632726189001e-23*x3 + 3.26694843060306e-21*x6 - 1.56435264841182e-22*x5 - 5.15045549259663e-22) / det
eq6 = (6.13749734881271e-23*x1 + 3.42116500164963e-20*x2 + 5.61199288135578e-21*x3 - 6.13749734881271e-23*x6 + 1.39258239262595e-22*x5 - 1.8962176942436e-23) / det

print("eq1 = ", transform_to_simpy(str(eq1)))
print("eq2 = ", transform_to_simpy(str(eq2)))
print("eq3 = ", transform_to_simpy(str(eq3)))
print("eq4 = ", transform_to_simpy(str(eq4)))
print("eq6 = ", transform_to_simpy(str(eq6)))

{a1: 0, a2: 0, a3: J_pz, a4: 0, a5: 0,
 b1: 0, b2: r*(C_Mz*M_p*r - C_mz*R*m + C_mz*m*r), b3: 0, b4: -C_Mz**2*M_p*r**2 - C_mz**2*R**2*m + 2*C_mz**2*R*m*r - C_mz**2*m*r**2 - J_px*r**2 - J_wx*R**2 + 2*J_wx*R*r - J_wx*r**2, b5: 0,
 c1: 0, c2: 0, c3: 0, c4: 0, c5: 2*M*R**2,
 d1: 0, d2: r*(-3*C_Mz*M_p - 3*C_mz*m - 5*M*R - 3*M_p*R - 3*R*m), d3: 0, d4: 3*C_Mz**2*M_p*r + 3*C_Mz*M_p*R*r - 3*C_mz**2*R*m + 3*C_mz**2*m*r - 3*C_mz*R**2*m + 3*C_mz*R*m*r + 3*J_px*r - 3*J_wx*R + 3*J_wx*r, d5: 0,
 e1: 3*C_Mz**2*M_p + 6*C_Mz*M_p*R + 3*C_mz**2*m + 6*C_mz*R*m + 3*J_py + 3*J_wy + 5*M*R**2 + 3*M_p*R**2 + 3*R**2*m, e2: 0, e3: 0, e4: 0, e5: 0}