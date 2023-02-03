from definitions.generic_coordinates import *
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr
transformations = (standard_transformations + (implicit_multiplication_application,))

a1, a2, a3, a4, a5, a7 = symbols('a1, a2, a3, a4, a5, a7')
b1, b2, b3, b4, b5, b7 = symbols('b1, b2, b3, b4, b5, b7')
c1, c2, c3, c4, c5, c7 = symbols('c1, c2, c3, c4, c5, c7')
d1, d2, d3, d4, d5, d7 = symbols('d1, d2, d3, d4, d5, d7')
e1, e2, e3, e4, e5, e7 = symbols('e1, e2, e3, e4, e5, e7')
f1, f2, f3, f4, f5, f7 = symbols('f1, f2, f3, f4, f5, f7')

for_resolve_second_diff = {
    'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5,  'a7': a7,
    'b1': b1, 'b2': b2, 'b3': b3, 'b4': b4, 'b5': b5, 'b7': b7,
    'c1': c1, 'c2': c2, 'c3': c3, 'c4': c4, 'c5': c5, 'c7': c7,
    'd1': d1, 'd2': d2, 'd3': d3, 'd4': d4, 'd5': d5, 'd7': d7,
    'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5, 'e7': e7,
    'f1': f1, 'f2': f2, 'f3': f3, 'f4': f4, 'f5': f5, 'f7': f7,
}
r_part_1 = Symbol('right_part_1')
r_part_2 = Symbol('right_part_2')
r_part_3 = Symbol('right_part_3')
r_part_4 = Symbol('right_part_4')
r_part_5 = Symbol('right_part_5')
r_part_7 = Symbol('right_part_7')

right_parts = {
    'right_part_1': r_part_1,
    'right_part_2': r_part_2,
    'right_part_3': r_part_3,
    'right_part_4': r_part_4,
    'right_part_5': r_part_5,
    'right_part_7': r_part_7
}

local_dictionary = {
    'x': x,
    'y': y,
    'x1': x1,
    'x2': x2,
    'x3': x3,
    'x4': x4,
    'x5': x5,
    'x6': x6,
    'x7': x7,
    'x8': x8,
}

dictionary = for_resolve_second_diff | local_dictionary | right_parts


def parse_2_sympy_expression(raw_str):
    return parse_expr(raw_str, transformations=transformations, local_dict=dictionary)


