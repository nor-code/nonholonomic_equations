from definitions.generic_coordinates import *
from utils.sympy_expression import parse_2_sympy_expression
from definitions.coefficient_for_resolve import *

mixed_coeff_var = {

}
print("initialized dict. of mixed coordinates")

dict_free_term_equations = {
    free_1: parse_2_sympy_expression(open("../../collect_parallel/eq3/free_term.txt").readline()),
    free_2: parse_2_sympy_expression(open("../../collect_parallel/eq6/free_term.txt").readline()),
    free_3: parse_2_sympy_expression(open("../../collect_parallel/eq9/free_term.txt").readline()),
    free_4: parse_2_sympy_expression(open("../../collect_parallel/eq10/free_term.txt").readline()),

}
print("initialized dict. of free term equations (contains control moments and generic forces of gravity)")


