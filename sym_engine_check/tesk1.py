from timeit import default_timer as clock
from symengine import var, sympify, function_symbol, Symbol
from utils.sympy_expression import *

import symengine as se
from symengine import Derivative, symbols

print("Converting to SymPy...")

s = open('../lambda/part2/eq_5_without_lambda.txt').read()
d_phi = parse_2_sympy_expression(open("../kinematic/part2/d_phi.txt").readline())
d_delta = parse_2_sympy_expression(open("../kinematic/part2/d_del.txt").readline())
d_eps = parse_2_sympy_expression(open("../kinematic/part2/d_eps.txt").readline())
d_tau = parse_2_sympy_expression(open("../kinematic/part2/d_tau.txt").readline())

d_d_phi = parse_2_sympy_expression(open("../kinematic/part3/d_d_phi.txt").readline())
d_d_delta = parse_2_sympy_expression(open("../kinematic/part3/d_d_del.txt").readline())
d_d_eps = parse_2_sympy_expression(open("../kinematic/part3/d_d_eps.txt").readline())
d_d_tau = parse_2_sympy_expression(open("../kinematic/part3/d_d_tau.txt").readline())

e = parse_2_sympy_expression(s)

print("Converting to SymEngine...")
ce = sympify(e)

cd_phi = sympify(d_phi)
cd_delta = sympify(d_delta)
cd_eps = sympify(d_eps)
cd_tau = sympify(d_tau)

cd_d_phi = sympify(d_d_phi)
cd_d_delta = sympify(d_d_delta)
cd_d_eps = sympify(d_d_eps)
cd_d_tau = sympify(d_d_tau)

print("SymEngine subs:")
t1 = clock()

time = se.Symbol("t")
phi = function_symbol("φ", time)
delta = function_symbol("δ", time)
eps = function_symbol("ε", time)
tau = function_symbol("τ", time)


cf = ce.subs(
    {
        se.diff(phi, time): cd_phi,
        se.diff(delta, time): cd_delta,
        se.diff(eps, time): cd_eps,
        se.diff(tau, time): cd_tau,
        se.diff(phi, time, time): cd_d_phi,
        se.diff(delta, time, time): cd_d_delta,
        se.diff(eps, time, time): cd_d_eps,
        se.diff(tau, time, time): cd_d_tau,
    }
)
print("end subs diff and second diff")
ce = cf.expand()
res = se.l
print(ce)
with open('outexpand5.txt', 'w') as out:
    out.write(str(ce))
t2 = clock()
print("Total time:", t2-t1, "s")


# Derivative(function_symbol("φ", Symbol("t")), Symbol("t")): cd_phi,
#         Derivative(function_symbol("δ", Symbol("t")), Symbol("t")): cd_delta,
#         Derivative(function_symbol("ε", Symbol("t")), Symbol("t")): cd_eps,
#         Derivative(function_symbol("τ", Symbol("t")), Symbol("t")): cd_tau,
#         Derivative(Derivative(function_symbol("φ", Symbol("t")), Symbol("t")), Symbol("t")): cd_d_phi,
#         Derivative(Derivative(function_symbol("δ", Symbol("t")), Symbol("t")), Symbol("t")): cd_d_delta,
#         Derivative(Derivative(function_symbol("ε", Symbol("t")), Symbol("t")), Symbol("t")): cd_d_eps,
#         Derivative(Derivative(function_symbol("v", Symbol("t")), Symbol("t")), Symbol("t")): cd_d_tau,

# print("SymPy diff:")
# t1 = clock()
# g = f.diff(sympy.Symbol("sq5"))
# t2 = clock()
# print("Total time:", t2-t1, "s")
# print("SymEngine diff:")
# t1 = clock()
# cg = cf.diff(Symbol("sq5"))
# t2 = clock()
# print("Total time:", t2-t1, "s")