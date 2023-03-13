# import Dynamics
# if __name__ == "__main__":
#     Dynamics.print_equations_for_Wolfram_Mathematica()


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
from sympy import *
from definitions.generic_coordinates import *
from definitions.constants import *
from definitions.coefficient_for_resolve import *
from definitions.moments import *
from utils.latex_converter import *

mmm = Matrix([[a1, a2, a3],
              [b1, b2, b3],
              [c1, c2, c3]])

g = 10
det = 1.86366951079694e-10

eq1 = (3.95690713497203e-13*g*x2 + 1.17259764725008e-11*g*x3) / det
eq2 = (- 9.04715639563326e-11*g*x2) / det
eq3 = (3.45511608982093e-10*g*x2 - 5.8423230602685e-11*g*x3) / det

print(eq1)
print(eq2)
print(eq3)
print("----")
det = -0.0288131477482463

eq1 = (2.1823764883542e-9 * g * x2 - 1.40087215164248e-5 * g * x3) / det
eq2 = (4.26663509953055e-6 * g * x2) / det
eq3 = (0.000311390983020061 * g * x2 - 3.56890541243072e-8 * g * x3) / det
print(eq1)
print(eq2)
print(eq3)