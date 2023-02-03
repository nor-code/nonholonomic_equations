from multiprocessing import Process

from sympy import together, fraction, Symbol

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import *

t1 = time.time()

d_d_phi = parse_2_sympy_expression(open('../part3/d_d_phi.txt').readline())
d_d_del = parse_2_sympy_expression(open('../part3/d_d_del.txt').readline())
d_d_eps = parse_2_sympy_expression(open('../part3/d_d_eps.txt').readline())
d_d_tau = parse_2_sympy_expression(open('../part3/d_d_tau.txt').readline())
print("finished parse from files")

map_name_2_symbol = {
    'd_d_phi': Symbol('d_d_phi_bot'),
    'd_d_del': Symbol('d_d_del_bot'),
    'd_d_eps': Symbol('d_d_eps_bot'),
    'd_d_tau': Symbol('d_d_tau_bot')
}


def simplify_second_diff(d_d_var, name):

    d_d_var_top, d_d_var_bot = fraction(d_d_var)
    d_d_var_top = d_d_var_top.subs(
        {
            sin(x2): x2 - (x2**3/6),
            sin(x2) ** 2: x2 ** 2,
            sin(x2) ** 3: 0,
            sin(x2) ** 4: 0,
            sin(x2) ** 5: 0,
            sin(x2) ** 6: 0,
            cos(x2): 1,
            cos(x2) ** 2: 1,
            cos(x2) ** 3: 1,
            cos(x2) ** 4: 1,
            cos(x2) ** 5: 1,
            cos(x2) ** 6: 1
        }
    )
    print("finished subs")

    d_d_var_top = d_d_var_top.expand()
    print("finished expand")

    d_d_var_top = d_d_var_top.subs(
        {
            x1 ** 4: 0,
            x1 ** 5: 0,
            x1 ** 6: 0,
            x1 ** 7: 0,
            x1 ** 8: 0,
            x1 ** 9: 0,

            x2 ** 3: 0,
            x2 ** 4: 0,
            x2 ** 5: 0,
            x2 ** 6: 0,
            x2 ** 7: 0,
            x2 ** 8: 0,
            x2 ** 9: 0,
            x2 ** 10: 0,
            x2 ** 11: 0,
            x2 ** 12: 0,
            x2 ** 13: 0,
            x2 ** 14: 0,
            x2 ** 15: 0,
            x2 ** 16: 0,
            x2 ** 17: 0,
            x2 ** 18: 0,
            x2 ** 19: 0,
            x2 ** 20: 0
        }
    )

    d_d_var_top = simplify(d_d_var_top)
    d_d_var_top = d_d_var_top.subs(
        {
            sin(x2): x2 - (x2 ** 3 / 6),
            sin(x2) ** 2: x2 ** 2,
            sin(x2) ** 3: 0,
            sin(x2) ** 4: 0,
            sin(x2) ** 5: 0,
            sin(x2) ** 6: 0,
            cos(x2): 1,
            cos(x2) ** 2: 1,
            cos(x2) ** 3: 1,
            cos(x2) ** 4: 1,
            cos(x2) ** 5: 1,
            cos(x2) ** 6: 1
        }
    )
    d_d_var_top = d_d_var_top.subs(
        {
            x1 ** 4: 0,
            x1 ** 5: 0,
            x1 ** 6: 0,
            x1 ** 7: 0,
            x1 ** 8: 0,
            x1 ** 9: 0,

            x2 ** 3: 0,
            x2 ** 4: 0,
            x2 ** 5: 0,
            x2 ** 6: 0,
            x2 ** 7: 0,
            x2 ** 8: 0,
            x2 ** 9: 0,
            x2 ** 10: 0,
            x2 ** 11: 0,
            x2 ** 12: 0,
            x2 ** 13: 0,
            x2 ** 14: 0,
            x2 ** 15: 0,
            x2 ** 16: 0,
            x2 ** 17: 0,
            x2 ** 18: 0,
            x2 ** 19: 0,
            x2 ** 20: 0
        }
    )

    with open('../../kinematic/part4/' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(d_d_var_top)))


tasks = []
d_d_vars = [d_d_phi, d_d_del, d_d_eps, d_d_tau]
names = ['d_d_phi', 'd_d_del', 'd_d_eps', 'd_d_tau']
for i in range(len(d_d_vars)):
    task = Process(target=simplify_second_diff, args=(d_d_vars[i], names[i]))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()

print("second diff calc end. total time = %.2f [m]" % ((t2 - t1) / 60))

