import re

from sympy import *

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
    latex_row = latex(row)
    for key in regexp_dict.keys():
        latex_row = re.sub(re.compile(key), regexp_dict[key], latex_row)
    return latex_row

