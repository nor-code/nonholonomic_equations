import time

from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *


t1 = time.time()
inverse_coeff_matrix = {
    m11: parse_2_sympy_expression(open("../part2_3/component_m11.txt").readline()),
    m12: parse_2_sympy_expression(open("../part2_3/component_m12.txt").readline()),
    m13: parse_2_sympy_expression(open("../part2_3/component_m13.txt").readline()),
    m14: parse_2_sympy_expression(open("../part2_3/component_m14.txt").readline()),
    m15: parse_2_sympy_expression(open("../part2_3/component_m15.txt").readline()),
    
    m21: parse_2_sympy_expression(open("../part2_3/component_m21.txt").readline()),
    m22: parse_2_sympy_expression(open("../part2_3/component_m22.txt").readline()),
    m23: parse_2_sympy_expression(open("../part2_3/component_m23.txt").readline()),
    m24: parse_2_sympy_expression(open("../part2_3/component_m24.txt").readline()),
    m25: parse_2_sympy_expression(open("../part2_3/component_m25.txt").readline()),

    m31: parse_2_sympy_expression(open("../part2_3/component_m31.txt").readline()),
    m32: parse_2_sympy_expression(open("../part2_3/component_m32.txt").readline()),
    m33: parse_2_sympy_expression(open("../part2_3/component_m33.txt").readline()),
    m34: parse_2_sympy_expression(open("../part2_3/component_m34.txt").readline()),
    m35: parse_2_sympy_expression(open("../part2_3/component_m35.txt").readline()),

    m41: parse_2_sympy_expression(open("../part2_3/component_m41.txt").readline()),
    m42: parse_2_sympy_expression(open("../part2_3/component_m42.txt").readline()),
    m43: parse_2_sympy_expression(open("../part2_3/component_m43.txt").readline()),
    m44: parse_2_sympy_expression(open("../part2_3/component_m44.txt").readline()),
    m45: parse_2_sympy_expression(open("../part2_3/component_m45.txt").readline()),

    m51: parse_2_sympy_expression(open("../part2_3/component_m51.txt").readline()),
    m52: parse_2_sympy_expression(open("../part2_3/component_m52.txt").readline()),
    m53: parse_2_sympy_expression(open("../part2_3/component_m53.txt").readline()),
    m54: parse_2_sympy_expression(open("../part2_3/component_m54.txt").readline()),
    m55: parse_2_sympy_expression(open("../part2_3/component_m55.txt").readline()),
}
t2 = time.time()
print("initialized dict for inverse matrix. time of initialization = %.2f [m]" % ((t2 - t1)/60))
