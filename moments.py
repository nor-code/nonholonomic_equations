from sympy import Function, Symbol
from generic_coordinates import t

M_ψ = Symbol('M_ψ')
M_ψ = Function('M_ψ')(t)

M_φ = Symbol('M_φ')
M_φ = Function('M_φ')(t)

M_ψ_p = - M_ψ