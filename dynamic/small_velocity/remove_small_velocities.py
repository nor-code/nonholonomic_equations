from sympy import expand

from utils.Wolfram import Wolfram
from utils.common import expand_and_collect_term_before_derivatives_and_lambda, \
    is_remove_small_term_with_velocities
from utils.latex_converter import print_in_latex
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import transform_to_simpy

eqns_indx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wolfram = Wolfram()
for indx in eqns_indx:
    eq_i = expand(parse_2_sympy_expression(open("../eq" + str(indx) + ".txt").readline()), deep=True, trig=True)
    simplified_eq_i = 0
    for term_of_eq_i in eq_i.args:
        if not is_remove_small_term_with_velocities(term_of_eq_i):
            simplified_eq_i += term_of_eq_i
    
    final_res = expand_and_collect_term_before_derivatives_and_lambda(simplified_eq_i)
    with open("eq" + str(indx) + ".txt", 'w') as new_out:
        print("eq" + str(indx) + " = " + print_in_latex(final_res))
        new_out.write(transform_to_simpy(str(final_res)))
    with open("eq_wolf" + str(indx) + ".txt", 'w') as wolf_out:
        wolf_out.write(wolfram.transformForWolframMathematica(str(final_res)))

print("\nIN LATEX STYLE:")
for indx in eqns_indx:
    with open("eq" + str(indx) + ".txt", 'r') as latex_res:
        print("eq" + str(indx) + " = " + print_in_latex(latex_res.readline()), ";")

print("\nIN WOLFRAM STYLE:")
for indx in eqns_indx:
    with open("eq_wolf" + str(indx) + ".txt", 'r') as wolf_res:
        print("eq" + str(indx) + " = " + wolf_res.readline(), ";")
