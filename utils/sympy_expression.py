from definitions.generic_coordinates import *
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr

transformations = (standard_transformations + (implicit_multiplication_application,))
local_dictionary = {'x': x, 'y': y, 'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5, 'x6': x6, 'x7': x7, 'x8': x8}


def parse_2_sympy_expression(raw_str):
    return parse_expr(raw_str, transformations=transformations, local_dict=local_dictionary)