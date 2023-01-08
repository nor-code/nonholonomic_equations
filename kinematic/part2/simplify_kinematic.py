"""
упрощаем выражения для скоростей φ' δ' ε' τ'
"""
from multiprocessing import Process

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import *

t1 = time.time()

d_phi = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq0.txt').readline())
d_del = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq1.txt').readline())
d_eps = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq2.txt').readline())
d_tau = parse_2_sympy_expression(open('../../kinematic/part1/kin_eq3.txt').readline())


def solve_transform_and_write_to_file(d_var, name):
    d_var_top, d_var_bot = fraction(together(d_var))
    d_var_top = expand(d_var_top, deep=True)
    top = expand_and_collect_term_before_first_derivatives(d_var_top)
    bot = simplify(simplification_expression(d_var_bot))
    result = top / bot
    with open('../../kinematic/part2/' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
d_vars = [d_phi, d_del, d_eps, d_tau]
names = ['d_phi', 'd_del', 'd_eps', 'd_tau']
for i in range(len(d_vars)):
    task = Process(target=solve_transform_and_write_to_file, args=(d_vars[i], names[i]))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()

print("simplification end. total time = %.2f [m]" % ((t2 - t1) / 60))
