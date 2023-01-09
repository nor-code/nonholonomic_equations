from multiprocessing import Process

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import *

t1 = time.time()

d_phi = parse_2_sympy_expression(open('../../kinematic/part2/d_phi.txt').readline())
d_del = parse_2_sympy_expression(open('../../kinematic/part2/d_del.txt').readline())
d_eps = parse_2_sympy_expression(open('../../kinematic/part2/d_eps.txt').readline())
d_tau = parse_2_sympy_expression(open('../../kinematic/part2/d_tau.txt').readline())


def calculate_second_diff(d_var, name):
    d_d_var = diff(d_var, t)
    d_d_var_top, d_d_var_bot = fraction(together(d_d_var))

    top = expand_and_collect_term_before_derivatives_and_lambda(d_d_var_top)
    bot = simplify(
        simplification_expression(
            expand(d_d_var_bot)
        )
    )

    result = top / bot
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
