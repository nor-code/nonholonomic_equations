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

expr = (-x3*sin(x1 - x6)*sin(x7)*sin(x5)*cos(x1) - x3*sin(x1)*sin(x2)**2*sin(x7)*sin(x5)*cos(x1 - x6) - x3*sin(x1)*sin(x2)*sin(x5)*cos(x2)*cos(x7))*(x3**2 - cos(x1))*diff(x1, t) + ((x2 - x5)*diff(x2, t)/(x4 - x1)) + diff(x1, t)

print(srepr(expr))
Add(
    Mul(Add(Pow(Function('γ')(Symbol('t')), Integer(2)), Mul(Integer(-1), cos(Function('α')(Symbol('t'))))), Add(Mul(Integer(-1), Function('γ')(Symbol('t')), sin(Add(Function('α')(Symbol('t')), Mul(Integer(-1), Function('δ')(Symbol('t'))))), sin(Function('ε')(Symbol('t'))), sin(Function('ψ')(Symbol('t'))), cos(Function('α')(Symbol('t')))), Mul(Integer(-1), Function('γ')(Symbol('t')), sin(Function('α')(Symbol('t'))), Pow(sin(Function('β')(Symbol('t'))), Integer(2)), sin(Function('ε')(Symbol('t'))), sin(Function('ψ')(Symbol('t'))), cos(Add(Function('α')(Symbol('t')), Mul(Integer(-1), Function('δ')(Symbol('t')))))), Mul(Integer(-1), Function('γ')(Symbol('t')), sin(Function('α')(Symbol('t'))), sin(Function('β')(Symbol('t'))), sin(Function('ψ')(Symbol('t'))), cos(Function('β')(Symbol('t'))), cos(Function('ε')(Symbol('t'))))), Derivative(Function('α')(Symbol('t')), Tuple(Symbol('t'), Integer(1)))),
    Derivative(Function('α')(Symbol('t')), Tuple(Symbol('t'), Integer(1))),
    Mul(Pow(Add(Mul(Integer(-1), Function('α')(Symbol('t'))), Function('φ')(Symbol('t'))), Integer(-1)), Add(Function('β')(Symbol('t')), Mul(Integer(-1), Function('ψ')(Symbol('t')))), Derivative(Function('β')(Symbol('t')), Tuple(Symbol('t'), Integer(1))))
)

print(expr)
print(expr - ((x2 - x5)*diff(x2, t)/(x4 - x1)))

def k(name, *args):
    for n in (name, ) + args:
        print(" _ ", n)

k("tomas", "kraken", "sraken")

