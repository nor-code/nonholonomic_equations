from sympy import *
import re
from utils.sympy_expression import parse_2_sympy_expression

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
last_dict = {
    "λ": "\\\\bm{\\\\lambda}",
    "M_\{φ\}": "\\\\bm{M}_\\\\phi",
    "M_\{ψ\}": "\\\\bm{M}_\\\\psi"
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

    for key in last_dict.keys():
        row = re.sub(re.compile(key), last_dict[key], row)
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

print("kin_eq0.txt")
print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part1/kin_eq0.txt').readline())))
print("\nkin_eq1.txt")
print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part1/kin_eq1.txt').readline())))
print("\nkin_eq2.txt")
print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part1/kin_eq2.txt').readline())))
print("\nkin_eq3.txt")
print(print_in_latex(parse_2_sympy_expression(open('../kinematic/part1/kin_eq3.txt').readline())))

print("\n\neq1")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq1.txt').readline())))
print("\neq2")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq2.txt').readline())))
print("\neq3")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq3.txt').readline())))
print("\neq4")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq4.txt').readline())))
print("\neq5")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq5.txt').readline())))
print("\neq6")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq6.txt').readline())))
print("\neq7")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq7.txt').readline())))
print("\neq8")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq8.txt').readline())))
print("\neq9")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq9.txt').readline())))
print("\neq10")
print(print_in_latex(parse_2_sympy_expression(open('../dynamic/small_velocity/eq10.txt').readline())))

print("\n\nlambda1")
print("\\bm{\\lambda_{1}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part1/lambda_1.txt').readline())))
print("\nlambda2")
print("\\bm{\\lambda_{2}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part1/lambda_2.txt').readline())))
print("\nlambda3")
print("\\bm{\\lambda_{3}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part1/lambda_3.txt').readline())))
print("\nlambda4")
print("\\bm{\\lambda_{4}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part1/lambda_4.txt').readline())))

print("\n\neq_6_without_lambda.txt")
print("\\bm{\\lambda_{1}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part2/eq_6_without_lambda.txt').readline())))
print("\neq_8_without_lambda.txt")
print("\\bm{\\lambda_{2}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part2/eq_8_without_lambda.txt').readline())))
print("\neq_9_without_lambda.txt")
print("\\bm{\\lambda_{3}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part2/eq_9_without_lambda.txt').readline())))
print("\neq_10_without_lambda.txt")
print("\\bm{\\lambda_{4}} = ", print_in_latex(parse_2_sympy_expression(open('../lambda/part2/eq_10_without_lambda.txt').readline())))