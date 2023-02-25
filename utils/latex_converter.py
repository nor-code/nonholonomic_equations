import re
from sympy import *

from utils.to_sympy_expression import transform_to_simpy

second_diff_dict = {
    r'diff(diff(x, t), t)': '\\frac{d^{2}}{d t^{2}} x',
    r'diff(diff(y, t), t)': '\\fraction{d^{2}}{d t^{2}} y',
    r'diff(diff(α, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\alpha',
    r'diff(diff(β, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\beta',
    r'diff(diff(γ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\gamma',
    r'diff(diff(φ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\phi',
    r'diff(diff(ψ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\psi',
    r'diff(diff(δ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\delta',
    r'diff(diff(ε, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\epsilon',
    r'diff(diff(τ, t), t)': '\\fraction{d^{2}}{d t^{2}} \\\\tau'
}

first_diff_dict = {
    r'diff(x, t)': '\\frac{d}{d t} x',
    r'diff(y, t)': '\\fraction{d}{d t} y',
    r'diff(α, t)': '\\fraction{d}{d t} \\\\alpha',
    r'diif(β, t)': '\\fraction{d}{d t} \\\\beta',
    r'diff(γ, t)': '\\fraction{d}{d t} \\\\gamma',
    r'diff(φ, t)': '\\fraction{d}{d t} \\\\phi',
    r'diff(ψ, t)': '\\fraction{d}{d t} \\\\psi',
    r'diff(δ, t)': '\\fraction{d}{d t} \\\\delta',
    r'diff(ε, t)': '\\fraction{d}{d t} \\\\epsilon',
    r'diff(τ, t)': '\\fraction{d}{d t} \\\\tau'
}

regexp_dict = {
    r'x': 'x',
    r'y': 'y',
    r'α': '\\\\alpha',
    r'β': '\\\\beta',
    r'γ': '\\\\gamma',
    r'φ': '\\\\phi',
    r'ψ': '\\\\psi',
    r'δ': '\\\\delta',
    r'ε': '\\\\epsilon',
    r'τ': '\\\\tau'
}


def print_in_latex(row):
    """
    преобразуем к латех формату
    :param row: переменная в sympy формате
    :return: latex-строка
    """
    row = latex(transform_to_simpy(row))
    for key in second_diff_dict.keys():
        row = re.sub(re.compile(key), regexp_dict[key], row)

    for key in first_diff_dict.keys():
        row = re.sub(re.compile(key), regexp_dict[key], row)

    for key in regexp_dict.keys():
        row = re.sub(re.compile(key), regexp_dict[key], row)
    return row

