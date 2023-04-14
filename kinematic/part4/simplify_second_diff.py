from multiprocessing import Process

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import *

t1 = time.time()

d_d_gamma = parse_2_sympy_expression(open('../part3/d_d_gamma.txt').readline())
d_d_beta = parse_2_sympy_expression(open('../part3/d_d_beta.txt').readline())
d_d_eps = parse_2_sympy_expression(open('../part3/d_d_eps.txt').readline())
d_d_tau = parse_2_sympy_expression(open('../part3/d_d_tau.txt').readline())

d_d_gamma_bot = parse_2_sympy_expression(open('../part3/d_d_gamma_bottom.txt').readline())
d_d_beta_bot = parse_2_sympy_expression(open('../part3/d_d_beta_bottom.txt').readline())
d_d_eps_bot = parse_2_sympy_expression(open('../part3/d_d_eps_bottom.txt').readline())
d_d_tau_bot = parse_2_sympy_expression(open('../part3/d_d_tau_bottom.txt').readline())

print("finished parse from files")

d_d_gamma = d_d_gamma / d_d_gamma_bot
d_d_beta = d_d_beta / d_d_beta_bot
d_d_eps = d_d_eps / d_d_eps_bot
d_d_tau = d_d_tau / d_d_tau_bot


def simplify_second_diff(d_d_var,  name):
    d_d_var = simplify(d_d_var)
    with open('../../kinematic/part4/' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(d_d_var)))


tasks = []
d_d_vars = [d_d_gamma, d_d_beta, d_d_eps, d_d_tau]
names = ['d_d_gamma', 'd_d_beta', 'd_d_eps', 'd_d_tau']
for i in range(len(d_d_vars)):
    task = Process(target=simplify_second_diff, args=(d_d_vars[i], names[i]))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()

print("second diff calc end. total time = %.2f [m]" % ((t2 - t1) / 60))

