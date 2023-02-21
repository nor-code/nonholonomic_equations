"""
упрощаем выражения для скоростей φ' δ' ε' τ'
"""
from multiprocessing import Process

from sympy import together, fraction

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import *
from definitions.denominators import *

t1 = time.time()

d_phi = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq0.txt').readline())
d_del = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq1.txt').readline())
d_eps = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq2.txt').readline())
d_tau = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq3.txt').readline())


def solve_transform_and_write_to_file(d_var, name, bottom_symbol):
    d_var_top, d_var_bot = fraction(together(d_var))
    bot = simplify(
        remove_fourth_and_above_smallness_from_expression(
            expand(
                simplification_expression(expand(d_var_bot, deep=True, trig=True)), deep=True
            )
        )
    )

    d_var_top = remove_fourth_and_above_smallness_from_expression(
        expand(
            simplification_expression(expand(d_var_top, deep=True, trig=True)), deep=True
        )
    )
    top = expand_and_collect_term_before_first_derivatives(d_var_top)

    result = top  # / bottom_symbol
    with open('../../kinematic/part2/' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))

    with open('../../kinematic/part2/' + name + '_bottom' + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(bot)))


tasks = []
d_vars = [d_phi, d_del, d_eps, d_tau]
names = ['d_phi', 'd_del', 'd_eps', 'd_tau']
name_2_symb_dict = {
    'd_phi': d_phi_bot,
    'd_del': d_del_bot,
    'd_eps': d_eps_bot,
    'd_tau': d_tau_bot
}
for i in range(len(d_vars)):
    task = Process(target=solve_transform_and_write_to_file, args=(d_vars[i], names[i], name_2_symb_dict[names[i]]))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()

print("simplification end. total time = %.2f [m]" % ((t2 - t1) / 60))
