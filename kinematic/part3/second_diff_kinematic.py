from multiprocessing import Process

from sympy import together, fraction, Symbol

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import *
from definitions.denominators import *

t1 = time.time()

d_phi = parse_2_sympy_expression(open('../../kinematic/part2/d_phi.txt').readline())
d_del = parse_2_sympy_expression(open('../../kinematic/part2/d_del.txt').readline())
d_eps = parse_2_sympy_expression(open('../../kinematic/part2/d_eps.txt').readline())
d_tau = parse_2_sympy_expression(open('../../kinematic/part2/d_tau.txt').readline())

map_name_2_symbol = {
    'd_d_phi': d_d_phi_bot,
    'd_d_del': d_d_del_bot,
    'd_d_eps': d_d_eps_bot,
    'd_d_tau': d_d_tau_bot
}


def calculate_second_diff(d_var, name):
    d_d_var = diff(d_var, t)
    d_d_var_top, d_d_var_bot = fraction(together(d_d_var))

    top = expand_and_collect_term_before_derivatives_and_lambda(d_d_var_top)
    print("finished 1st collect and expand")

    top = top.subs(diff(x4, t),  d_phi)
    top = top.subs(diff(x6, t), d_del)
    top = top.subs(diff(x7, t), d_eps)
    top = top.subs(diff(x8, t), d_tau)
    print("finished 2nd collect and expand")

    top, bot1 = fraction(together(top))
    print("finished fraction and together")

    top = expand_and_collect_term_before_derivatives_and_lambda(top)
    print("finished 2st collect and expand")

    bot2 = simplification_expression(
        trigsimp(
            simplification_expression(
                expand(d_d_var_bot)
            )
        )
    )
    print("finished simplification denominator. 1")
    bot = simplification_expression(
        trigsimp(simplification_expression(Mul(bot1, bot2)))
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
