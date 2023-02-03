import re
import time

from sympy import together, fraction, Add
from sympy.core.numbers import Zero

from definitions.generic_coordinates import *
from utils.common import base_remove_current_and_above_smallness
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import transform_to_simpy
import tqdm
from definitions.symengine_var import *
from resolve_second_diff.part2.coefficient_dict import main_vars_subs


t1 = time.time()

r_part_1 = se.Symbol('right_part_1')
r_part_2 = se.Symbol('right_part_2')
r_part_3 = se.Symbol('right_part_3')
r_part_4 = se.Symbol('right_part_4')
r_part_5 = se.Symbol('right_part_5')
r_part_7 = se.Symbol('right_part_7')

map_expr = {
    1: se.Symbol('a_1') * se.diff(se_x, timet)**2 + se.Symbol('a_2') * se.diff(se_x, timet)*diff(se_y, timet) + se.Symbol('a_3') * se.diff(se_x, timet)*diff(se_alpha, timet) + se.Symbol('a_4') * se.diff(se_x, timet)*diff(se_beta, timet)
       + se.Symbol('a_5') * se.diff(se_x, timet)*diff(se_gama, timet) + se.Symbol('a_6') * se.diff(se_x, timet)*diff(se_psi, timet) + se.Symbol('a_7') * se.diff(se_y, timet)**2 + se.Symbol('a_8') * se.diff(se_y, timet)*se.diff(se_alpha, timet)
       + se.Symbol('a_9') * se.diff(se_y, timet)*se.diff(se_beta, timet) + se.Symbol('a_10') * se.diff(se_y, timet)*se.diff(se_gama, timet) + se.Symbol('a_11') * se.diff(se_y, timet)*se.diff(se_psi, timet)
       + se.Symbol('a_12') * se.diff(se_alpha, timet)**2 + se.Symbol('a_13') * se.diff(se_alpha, timet)*se.diff(se_beta, timet) + se.Symbol('a_14') * se.diff(se_alpha, timet)*se.diff(se_gama, timet)
       + se.Symbol('a_15') * se.diff(se_alpha, timet)*se.diff(se_psi, timet) + se.Symbol('a_16') * se.diff(se_beta, timet)**2 + se.Symbol('a_17') * se.diff(se_beta, timet)*se.diff(se_gama, timet)
       + se.Symbol('a_18') * se.diff(se_beta, timet)*se.diff(se_psi, timet) + se.Symbol('a_19') * se.diff(se_gama, timet)**2 + se.Symbol('a_20') * se.diff(se_gama, timet) * se.diff(se_psi, timet)
       + se.Symbol('a_21') * se.diff(se_psi, timet)**2,
    2: se.Symbol('b_1') * se.diff(se_x, timet)**2 + se.Symbol('b_2') * se.diff(se_x, timet)*diff(se_y, timet) + se.Symbol('b_3') * se.diff(se_x, timet)*diff(se_alpha, timet) + se.Symbol('b_4') * se.diff(se_x, timet)*diff(se_beta, timet)
       + se.Symbol('b_5') * se.diff(se_x, timet)*diff(se_gama, timet) + se.Symbol('b_6') * se.diff(se_x, timet)*diff(se_psi, timet) + se.Symbol('b_7') * se.diff(se_y, timet)**2 + se.Symbol('b_8') * se.diff(se_y, timet)*se.diff(se_alpha, timet)
       + se.Symbol('b_9') * se.diff(se_y, timet)*se.diff(se_beta, timet) + se.Symbol('b_10') * se.diff(se_y, timet)*se.diff(se_gama, timet) + se.Symbol('b_11') * se.diff(se_y, timet)*se.diff(se_psi, timet)
       + se.Symbol('b_12') * se.diff(se_alpha, timet)**2 + se.Symbol('b_13') * se.diff(se_alpha, timet)*se.diff(se_beta, timet) + se.Symbol('b_14') * se.diff(se_alpha, timet)*se.diff(se_gama, timet)
       + se.Symbol('b_15') * se.diff(se_alpha, timet)*se.diff(se_psi, timet) + se.Symbol('b_16') * se.diff(se_beta, timet)**2 + se.Symbol('b_17') * se.diff(se_beta, timet)*se.diff(se_gama, timet)
       + se.Symbol('b_18') * se.diff(se_beta, timet)*se.diff(se_psi, timet) + se.Symbol('b_19') * se.diff(se_gama, timet)**2 + se.Symbol('b_20') * se.diff(se_gama, timet) * se.diff(se_psi, timet)
       + se.Symbol('b_21') * se.diff(se_psi, timet)**2,
    3: se.Symbol('c_1') * se.diff(se_x, timet)**2 + se.Symbol('c_2') * se.diff(se_x, timet)*diff(se_y, timet) + se.Symbol('c_3') * se.diff(se_x, timet)*diff(se_alpha, timet) + se.Symbol('c_4') * se.diff(se_x, timet)*diff(se_beta, timet)
       + se.Symbol('c_5') * se.diff(se_x, timet)*diff(se_gama, timet) + se.Symbol('c_6') * se.diff(se_x, timet)*diff(se_psi, timet) + se.Symbol('c_7') * se.diff(se_y, timet)**2 + se.Symbol('c_8') * se.diff(se_y, timet)*se.diff(se_alpha, timet)
       + se.Symbol('c_9') * se.diff(se_y, timet)*se.diff(se_beta, timet) + se.Symbol('c_10') * se.diff(se_y, timet)*se.diff(se_gama, timet) + se.Symbol('c_11') * se.diff(se_y, timet)*se.diff(se_psi, timet)
       + se.Symbol('c_12') * se.diff(se_alpha, timet)**2 + se.Symbol('c_13') * se.diff(se_alpha, timet)*se.diff(se_beta, timet) + se.Symbol('c_14') * se.diff(se_alpha, timet)*se.diff(se_gama, timet)
       + se.Symbol('c_15') * se.diff(se_alpha, timet)*se.diff(se_psi, timet) + se.Symbol('c_16') * se.diff(se_beta, timet)**2 + se.Symbol('c_17') * se.diff(se_beta, timet)*se.diff(se_gama, timet)
       + se.Symbol('c_18') * se.diff(se_beta, timet)*se.diff(se_psi, timet) + se.Symbol('c_19') * se.diff(se_gama, timet)**2 + se.Symbol('c_20') * se.diff(se_gama, timet) * se.diff(se_psi, timet)
       + se.Symbol('c_21') * se.diff(se_psi, timet)**2,
    4: se.Symbol('d_1') * se.diff(se_x, timet)**2 + se.Symbol('d_2') * se.diff(se_x, timet)*diff(se_y, timet) + se.Symbol('d_3') * se.diff(se_x, timet)*diff(se_alpha, timet) + se.Symbol('d_4') * se.diff(se_x, timet)*diff(se_beta, timet)
       + se.Symbol('d_5') * se.diff(se_x, timet)*diff(se_gama, timet) + se.Symbol('d_6') * se.diff(se_x, timet)*diff(se_psi, timet) + se.Symbol('d_7') * se.diff(se_y, timet)**2 + se.Symbol('d_8') * se.diff(se_y, timet)*se.diff(se_alpha, timet)
       + se.Symbol('d_9') * se.diff(se_y, timet)*se.diff(se_beta, timet) + se.Symbol('d_10') * se.diff(se_y, timet)*se.diff(se_gama, timet) + se.Symbol('d_11') * se.diff(se_y, timet)*se.diff(se_psi, timet)
       + se.Symbol('d_12') * se.diff(se_alpha, timet)**2 + se.Symbol('d_13') * se.diff(se_alpha, timet)*se.diff(se_beta, timet) + se.Symbol('d_14') * se.diff(se_alpha, timet)*se.diff(se_gama, timet)
       + se.Symbol('d_15') * se.diff(se_alpha, timet)*se.diff(se_psi, timet) + se.Symbol('d_16') * se.diff(se_beta, timet)**2 + se.Symbol('d_17') * se.diff(se_beta, timet)*se.diff(se_gama, timet)
       + se.Symbol('d_18') * se.diff(se_beta, timet)*se.diff(se_psi, timet) + se.Symbol('d_19') * se.diff(se_gama, timet)**2 + se.Symbol('d_20') * se.diff(se_gama, timet) * se.diff(se_psi, timet)
       + se.Symbol('d_21') * se.diff(se_psi, timet)**2,
    5: se.Symbol('e_1') * se.diff(se_x, timet)**2 + se.Symbol('e_2') * se.diff(se_x, timet)*diff(se_y, timet) + se.Symbol('e_3') * se.diff(se_x, timet)*diff(se_alpha, timet) + se.Symbol('e_4') * se.diff(se_x, timet)*diff(se_beta, timet)
       + se.Symbol('e_5') * se.diff(se_x, timet)*diff(se_gama, timet) + se.Symbol('e_6') * se.diff(se_x, timet)*diff(se_psi, timet) + se.Symbol('e_7') * se.diff(se_y, timet)**2 + se.Symbol('e_8') * se.diff(se_y, timet)*se.diff(se_alpha, timet)
       + se.Symbol('e_9') * se.diff(se_y, timet)*se.diff(se_beta, timet) + se.Symbol('e_10') * se.diff(se_y, timet)*se.diff(se_gama, timet) + se.Symbol('e_11') * se.diff(se_y, timet)*se.diff(se_psi, timet)
       + se.Symbol('e_12') * se.diff(se_alpha, timet)**2 + se.Symbol('e_13') * se.diff(se_alpha, timet)*se.diff(se_beta, timet) + se.Symbol('e_14') * se.diff(se_alpha, timet)*se.diff(se_gama, timet)
       + se.Symbol('e_15') * se.diff(se_alpha, timet)*se.diff(se_psi, timet) + se.Symbol('e_16') * se.diff(se_beta, timet)**2 + se.Symbol('e_17') * se.diff(se_beta, timet)*se.diff(se_gama, timet)
       + se.Symbol('e_18') * se.diff(se_beta, timet)*se.diff(se_psi, timet) + se.Symbol('e_19') * se.diff(se_gama, timet)**2 + se.Symbol('e_20') * se.diff(se_gama, timet) * se.diff(se_psi, timet)
       + se.Symbol('e_21') * se.diff(se_psi, timet)**2,
    7: se.Symbol('b_1') * se.diff(se_x, timet)**2 + se.Symbol('b_2') * se.diff(se_x, timet)*diff(se_y, timet) + se.Symbol('b_3') * se.diff(se_x, timet)*diff(se_alpha, timet) + se.Symbol('b_4') * se.diff(se_x, timet)*diff(se_beta, timet)
       + se.Symbol('b_5') * se.diff(se_x, timet)*diff(se_gama, timet) + se.Symbol('b_6') * se.diff(se_x, timet)*diff(se_psi, timet) + se.Symbol('b_7') * se.diff(se_y, timet)**2 + se.Symbol('b_8') * se.diff(se_y, timet)*se.diff(se_alpha, timet)
       + se.Symbol('b_9') * se.diff(se_y, timet)*se.diff(se_beta, timet) + se.Symbol('b_10') * se.diff(se_y, timet)*se.diff(se_gama, timet) + se.Symbol('b_11') * se.diff(se_y, timet)*se.diff(se_psi, timet)
       + se.Symbol('b_12') * se.diff(se_alpha, timet)**2 + se.Symbol('b_13') * se.diff(se_alpha, timet)*se.diff(se_beta, timet) + se.Symbol('b_14') * se.diff(se_alpha, timet)*se.diff(se_gama, timet)
       + se.Symbol('b_15') * se.diff(se_alpha, timet)*se.diff(se_psi, timet) + se.Symbol('b_16') * se.diff(se_beta, timet)**2 + se.Symbol('b_17') * se.diff(se_beta, timet)*se.diff(se_gama, timet)
       + se.Symbol('b_18') * se.diff(se_beta, timet)*se.diff(se_psi, timet) + se.Symbol('b_19') * se.diff(se_gama, timet)**2 + se.Symbol('b_20') * se.diff(se_gama, timet) * se.diff(se_psi, timet)
       + se.Symbol('b_21') * se.diff(se_psi, timet)**2
}
matrix = {
    1: list(se.symbols('a1, a2, a3, a4, a5, a7')),
    2: list(se.symbols('b1, b2, b3, b4, b5, b7')),
    3: list(se.symbols('c1, c2, c3, c4, c5, c7')),
    4: list(se.symbols('d1, d2, d3, d4, d5, d7')),
    5: list(se.symbols('e1, e2, e3, e4, e5, e7')),
    7: list(se.symbols('f1, f2, f3, f4, f5, f7'))
}

path = '../../collect_parallel/eq'
template_name = 'd_d_%s_t__2__.txt'
names = [template_name % var for var in ['x', 'y', 'α', 'β', 'γ', 'ψ']]
diff_list = [se_x, se_y, se_alpha, se_beta, se_gama, se_psi]

final_independent_coordinates = [x, y, x1, x2, x3, x5]
mixed_derivatives = list(mixed[0] * mixed[1] for mixed in itertools.combinations([diff(var, t) for var in final_independent_coordinates], 2))
[mixed_derivatives.append(diff(var, t) * diff(var, t)) for var in final_independent_coordinates]
mixed_dict_name = dict(
    zip(
        mixed_derivatives,
        [re.sub('[)( ,*]', '_', str(mixed)).replace('Derivative', 'd').replace('t___', '') for mixed in mixed_derivatives]
    )
)


def build_left_part(number, file_names):
    global map_expr
    total = se.sympify('0')
    for i, name in zip(range(6), file_names):
        expression = parse_2_sympy_expression(open(path + str(number) + '/' + name).readline())
        if expression == Zero():
            print("zero")
            continue
        total = se.Add(total, se.Mul(matrix[number][i], se.diff(diff_list[i], timet, timet)))
    total = total + map_expr[number]
    return total


a, b, c, d, e, f = se.symbols("a b c d e f")

left_part_equations = []
for i in tqdm.tqdm([1, 2, 3, 4, 5]):
    eq = se.sympify(build_left_part(i, names))
    eq = eq.subs(
        {
            se.diff(se_x, timet, timet): a,
            se.diff(se_y, timet, timet): b,
            se.diff(se_alpha, timet, timet): c,
            se.diff(se_beta, timet, timet): d,
            se.diff(se_gama, timet, timet): e,
            # se.diff(se_psi, timet, timet): f
        }
    )
    left_part_equations.append(eq)

sol1, sol2, sol3, sol4, sol5 = se.linsolve(left_part_equations, [a, b, c, d, e])

print("begin simplify")

for i, sol in zip(range(6), [sol1, sol2, sol3, sol4, sol5]):
    t1 = time.time()

    sympy_solution = parse_2_sympy_expression(transform_to_simpy(str(sol)))
    top, bot = fraction(together(sympy_solution))
    # top = se.expand(se.sympify(top))
    bot = se.expand(se.sympify(bot))
    bot = bot.subs(
        main_vars_subs
    )
    print("finished subs %.2f [m]" % ((time.time() - t1)/60))

    bot = se.sympify(bot)
    print("to sympy. len = %d" % len(bot.args))

    simplified = Zero()
    # if (type(expression) == Pow and __is_denominator_sym(expression.args[0])) or __is_denominator_sym(expression):
    #     return expression
    for term in tqdm.tqdm(bot.args):
        print(transform_to_simpy(str(term)))
        expanded_term = se.expand(se.sympify(term))
        print("finish sub_expand")
        for sub_term in expanded_term.args:
            count = base_remove_current_and_above_smallness(parse_2_sympy_expression(transform_to_simpy(str(sub_term))))
            if count < 4:
                simplified = Add(sub_term, simplified)

    print("finish remove fourth and above term smallness. len = %d" % len(simplified.args))

    t2 = time.time()
    print("simplify & get fraction by time %.2f" % ((t2 - t1) / 60))

    with open('sol_' + str(i) + '_top' + '.txt', 'w') as out:
        print("begin write i = ", i)
        out.write(transform_to_simpy(str(top)))
        print("finish write i = ", i)

    with open('sol_' + str(i) + '_bot' + '.txt', 'w') as out:
        print("begin write i = ", i)
        out.write(str(simplified))
        print("finish write i = ", i)

t2 = time.time()

print("finished by time = %.2f [m]" % ((t2 - t1)/60))
