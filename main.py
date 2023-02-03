# import Dynamics
# if __name__ == "__main__":
#     Dynamics.print_equations_for_Wolfram_Mathematica()


# import numpy
# import aesara
# import aesara.tensor as at
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

mmm = Matrix([[a1, a2, a3, a4, a5],
              [b1, b2, b3, b4, b5],
              [c1, c2, c3, c4, c5],
              [d1, d2, d3, d4, d5],
              [e1, e2, e3, e4, e5]])

