from sympy import *
import re

from utils.common import remove_required_and_above_smallness_from_expression, simplification_expression, \
    is_remove_small_term_with_velocities
from utils.sympy_expression import parse_2_sympy_expression

# second_diff_dict = {
#     r'diff(diff(x, t), t)': '\\frac{d^{2}}{d t^{2}} x',
#     r'diff(diff(y, t), t)': '\\fraction{d^{2}}{d t^{2}} y',
#     r'diff(diff(α, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\alpha',
#     r'diff(diff(β, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\beta',
#     r'diff(diff(γ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\gamma',
#     r'diff(diff(φ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\phi',
#     r'diff(diff(ψ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\psi',
#     r'diff(diff(δ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\delta',
#     r'diff(diff(ε, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\epsilon',
#     r'diff(diff(τ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\tau'
# }
#
# first_diff_dict = {
#     r'diff(x, t)': '\\frac{d}{d t} x',
#     r'diff(y, t)': '\\fraction{d}{d t} y',
#     r'diff(α, t)': '\\fraction{d}{d t} \\\\alpha',
#     r'diif(β, t)': '\\fraction{d}{d t} \\\\beta',
#     r'diff(γ, t)': '\\fraction{d}{d t} \\\\gamma',
#     r'diff(φ, t)': '\\fraction{d}{d t} \\\\phi',
#     r'diff(ψ, t)': '\\fraction{d}{d t} \\\\psi',
#     r'diff(δ, t)': '\\fraction{d}{d t} \\\\delta',
#     r'diff(ε, t)': '\\fraction{d}{d t} \\\\epsilon',
#     r'diff(τ, t)': '\\fraction{d}{d t} \\\\tau'
# }

regexp_dict = {
    r'x\{\\left\(t \\right\)\}': 'x',
    r'y\{\\left\(t \\right\)\}': 'y',
    r'α\{\\left\(t \\right\)\}': '\\\\alpha',
    r'β\{\\left\(t \\right\)\}': '\\\\beta',
    r'γ\{\\left\(t \\right\)\}': '\\\\gamma',
    r'φ\{\\left\(t \\right\)\}': '\\\\phi',
    r'ψ\{\\left\(t \\right\)\}': '\\\\psi',
    r'δ\{\\left\(t \\right\)\}': '\\\\delta',
    r'ε\{\\left\(t \\right\)\}': '\\\\epsilon',
    r'τ\{\\left\(t \\right\)\}': '\\\\tau',
    r'α\^\{': '\\\\alpha^{',
    r'β\^\{': '\\\\beta^{',
    r'γ\^\{': '\\\\gamma^{',
    r'φ\^\{': '\\\\phi^{',
    r'ψ\^\{': '\\\\psi^{',
    r'δ\^\{': '\\\\delta^{',
    r'ε\^\{': '\\\\epsilon^{',
    r'τ\^\{': '\\\\tau^{',
    r'\}\{\\left\(t \\right\)\}': '}'
}


def print_in_latex(expression):
    """
    преобразуем к латех формату
    :param row: переменная в sympy формате
    :return: latex-строка
    """
    row = latex(expression)

    for key in regexp_dict.keys():
        row = re.sub(re.compile(key), regexp_dict[key], row)
    return row


# print("d_del")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_del.txt').readline())))
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_del_bottom.txt').readline())))
# print("---\n")
# print("d_eps")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_eps.txt').readline())))
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_eps_bottom.txt').readline())))
# print("---\n")
# print("d_phi")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_phi.txt').readline())))
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_phi_bottom.txt').readline())))
# print("---\n")
# print("d_tau")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_tau.txt').readline())))
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part2/d_tau_bottom.txt').readline())))
# print("---")
#
#
# print("d_d_del")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part4/d_d_del.txt').readline())))
# print("---\n")
# print("d_d_eps")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part4/d_d_eps.txt').readline())))
# print("---\n")
# print("d_d_phi")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part4/d_d_phi.txt').readline())))
# print("---\n")
# print("d_d_tau")
# print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part4/d_d_tau.txt').readline())))
# print("---")

# print("eq1")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq1.txt').readline())))
# print("\neq2")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq2.txt').readline())))
# print("\neq3")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq3.txt').readline())))
# print("\neq4")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq4.txt').readline())))
# print("\neq5")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq5.txt').readline())))
# print("\neq6")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq6.txt').readline())))
# print("\neq7")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq7.txt').readline())))
# print("\neq8")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq8.txt').readline())))
# print("\neq9")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq9.txt').readline())))
# print("\neq10")
# print(print_in_latex(parse_2_sympy_expression(open('../dynamic/eq10.txt').readline())))