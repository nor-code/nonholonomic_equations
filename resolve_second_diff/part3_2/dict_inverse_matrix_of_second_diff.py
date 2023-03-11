import time

from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *


t1 = time.time()
inverse_coeff_matrix = {
    m11: parse_2_sympy_expression(open("../part2_2/component_m11.txt").readline()),
    m12: parse_2_sympy_expression(open("../part2_2/component_m12.txt").readline()),
    m13: parse_2_sympy_expression(open("../part2_2/component_m13.txt").readline()),

    m21: parse_2_sympy_expression(open("../part2_2/component_m21.txt").readline()),
    m22: parse_2_sympy_expression(open("../part2_2/component_m22.txt").readline()),
    m23: parse_2_sympy_expression(open("../part2_2/component_m23.txt").readline()),

    m31: parse_2_sympy_expression(open("../part2_2/component_m31.txt").readline()),
    m32: parse_2_sympy_expression(open("../part2_2/component_m32.txt").readline()),
    m33: parse_2_sympy_expression(open("../part2_2/component_m33.txt").readline()),

}
t2 = time.time()
print("initialized dict for inverse matrix. time of initialization = %.2f [m]" % ((t2 - t1)/60))
