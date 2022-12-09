# import Dynamics
# if __name__ == "__main__":
#     Dynamics.print_equations_for_Wolfram_Mathematica()

# x_raw = input().split(" ")
# y_raw = input().split(" ")
#
# x = list(float(x_i) for x_i in x_raw)
# y = list(float(y_i) for y_i in y_raw)
#
# mean_x = sum(x) / float(len(x))
# mean_y = sum(y) / float(len(y))
#
# var_x, var_y = sum((x_i - mean_x) ** 2 for x_i in x) / float(len(x)),\
#                sum((y_i - mean_y) ** 2 for y_i in y) / float(len(y))
#
# covar_xy = sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y)) / float(len(x))
#
# a = covar_xy / var_x
# b = mean_y - a * mean_x
#
# print(a)
# print(b)

from sympy import *
from definitions.constants import *
from definitions.generic_coordinates import *
from utils.common import *
from sympy.solvers.solveset import linsolve
from utils.to_sympy_expression import *
#
# x, y, z = symbols('x, y, z')
# t = Symbol('t')
# x1 = Function('α')(t)
# x2 = Function('β')(t)
# x3 = Function('w')(t)
# solution = linsolve([x + y + z - diff(x1, t) + sin(x3)*diff(x3, t), x + y + 2 * z - 3 * x1 - diff(x2, t)],
#              (diff(x1, t), diff(x2, t))
# )
#
# print("x'1 = ", solution.args[0][0])
# print("x'1 = ", diff(solution.args[0][0], t))
#
# eq1 = diff(diff(x1, t), t) + sin(x1) * diff(x1, t) + x1*22
# print("\neq1 = ", eq1)
#
# eq1 = eq1.subs(diff(diff(x1, t), t), diff(solution.args[0][0], t))
# print("after subs1 eq1 = ", eq1)
#
# eq1 = eq1.subs(diff(x1, t), solution.args[0][0])
# print("after subs2 eq1 = ", eq1)
