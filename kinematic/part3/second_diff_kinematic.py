from multiprocessing import Process

import sympy
from sympy import together, fraction, Symbol

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import *
from definitions.denominators import *
from definitions.symengine_var import *
import sys
import tqdm
sys.setrecursionlimit(1000000)


t1 = time.time()

d_phi_top = parse_2_sympy_expression(open('../../kinematic/part2/d_phi.txt').readline())
d_del_top = parse_2_sympy_expression(open('../../kinematic/part2/d_del.txt').readline())
d_eps_top = parse_2_sympy_expression(open('../../kinematic/part2/d_eps.txt').readline())
d_tau_top = parse_2_sympy_expression(open('../../kinematic/part2/d_tau.txt').readline())

d_phi_bot = parse_2_sympy_expression(open('../../kinematic/part2/d_phi_bottom.txt').readline())
d_del_bot = parse_2_sympy_expression(open('../../kinematic/part2/d_del_bottom.txt').readline())
d_eps_bot = parse_2_sympy_expression(open('../../kinematic/part2/d_eps_bottom.txt').readline())
d_tau_bot = parse_2_sympy_expression(open('../../kinematic/part2/d_tau_bottom.txt').readline())

d_phi = d_phi_top / d_phi_bot
d_del = d_del_top / d_del_bot
d_eps = d_eps_top / d_eps_bot
d_tau = d_tau_top / d_tau_bot

map_name_2_symbol = {
    'd_d_phi': d_d_phi_bot,
    'd_d_del': d_d_del_bot,
    'd_d_eps': d_d_eps_bot,
    'd_d_tau': d_d_tau_bot
}


def calculate_second_diff(d_var, name):
    d_d_var = diff(d_var, t)
    d_d_var_top, d_d_var_bot = fraction(together(d_d_var))

    d_d_var_top = remove_required_and_above_smallness_from_expression(
        expand(d_d_var_top, deep=True),
        order=5
    )

    print("first collect in d_d_var_top and remove small term")

    d_d_var_top = d_d_var_top.subs(
        {
            diff(x4, t): d_phi,
            diff(x6, t): d_del,
            diff(x7, t): d_eps,
            diff(x8, t): d_tau
        },
        simultaneous=True
    )
    print("finished sub first derivatives")

    top, bot1 = fraction(together(d_d_var_top))
    print("finished fraction and together")

    top_as_se = se.expand(se.sympify(top))
    print("sym_engine expand finished")
    # top = expand_and_collect_term_before_derivatives_and_lambda(
    #     remove_required_and_above_smallness_from_expression(
    #         parse_2_sympy_expression(transform_to_simpy(str(top_as_se))),
    #         order=5
    #     )
    # )

    res = 0
    count = 0
    for term_ in tqdm.tqdm(top_as_se.args):
        term_ = parse_2_sympy_expression(transform_to_simpy(str(term_)))
        top = expand(term_)

        if type(top) == Mul:
            simpl_top = remove_current_and_above_smallness_from_one_term(term_, order=5)
        else:
            simpl_top = remove_required_and_above_smallness_from_expression(term_, order=5)

        if simpl_top != sympy.core.numbers.Zero():
            expression = expand(simpl_top)
            if type(expression) == Add:
                for tterm in expression.args:
                    res += transform_to_simpy(str(tterm))
                    count += 1
            else:
                res += transform_to_simpy(str(expression))
                count += 1
    print("finished 2st collect and expand", count)
    print("res ", res)

    bot2 = remove_fourth_and_above_smallness_from_expression(
        expand(d_d_var_bot, deep=True)
    )
    print("finished simplification denominator. 1")

    bot = trigsimp(
        remove_required_and_above_smallness_from_expression(
            expand(Mul(bot1, bot2), deep=True),
            order=5
        )
    )
    print("finished simplification denominator. 2")

    with open('../../kinematic/part3/' + name + '_bottom' + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(bot)))

    result = top / map_name_2_symbol[name]
    with open('../../kinematic/part3/' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
d_vars = [d_phi, d_del, d_eps, d_tau]
names = ['d_d_phi', 'd_d_del', 'd_d_eps', 'd_d_tau']
for i in range(len(d_vars)):
    task = Process(target=calculate_second_diff, args=(d_vars[i], names[i]))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()

print("second diff calc end. total time = %.2f [m]" % ((t2 - t1) / 60))
