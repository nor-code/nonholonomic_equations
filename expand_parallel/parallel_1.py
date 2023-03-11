import argparse
import json
from multiprocessing import Process, Lock, Value
import sys

import sympy.core.numbers

sys.setrecursionlimit(100000)
import redis
from sympy import fraction, together, expand_trig

from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import transform_to_simpy
from timeit import default_timer as clock
from definitions.symengine_var import *


def _sub_step(equation, var, expression):
    equation_top, bot = fraction(
        together(
            equation.subs(var, expression)
        )
    )
    return equation_top


d_gamma_top = parse_2_sympy_expression(open("../kinematic/part2/d_gamma.txt").readline())
d_gamma_bot = parse_2_sympy_expression(open("../kinematic/part2/d_gamma_bottom.txt").readline())

d_phi_top = parse_2_sympy_expression(open("../kinematic/part2/d_phi.txt").readline())
d_phi_bot = parse_2_sympy_expression(open("../kinematic/part2/d_phi_bottom.txt").readline())

d_eps_top = parse_2_sympy_expression(open("../kinematic/part2/d_eps.txt").readline())
d_eps_bot = parse_2_sympy_expression(open("../kinematic/part2/d_eps_bottom.txt").readline())

d_tau_top = parse_2_sympy_expression(open("../kinematic/part2/d_tau.txt").readline())
d_tau_bot = parse_2_sympy_expression(open("../kinematic/part2/d_tau_bottom.txt").readline())

d_d_gamma = parse_2_sympy_expression(open("../kinematic/part4/d_d_gamma.txt").readline())
d_d_phi = parse_2_sympy_expression(open("../kinematic/part4/d_d_phi.txt").readline())
d_d_eps = parse_2_sympy_expression(open("../kinematic/part4/d_d_eps.txt").readline())
d_d_tau = parse_2_sympy_expression(open("../kinematic/part4/d_d_tau.txt").readline())

cd_gamma = se.sympify(d_gamma_top/d_gamma_bot)
cd_phi = se.sympify(d_phi_top/d_phi_bot)
cd_eps = se.sympify(d_eps_top/d_eps_bot)
cd_tau = se.sympify(d_tau_top/d_tau_bot)

cd_d_gamma = se.sympify(d_d_gamma)
cd_d_phi = se.sympify(d_d_phi)
cd_d_eps = se.sympify(d_d_eps)
cd_d_tau = se.sympify(d_d_tau)


def subs_kinematic(equation):
    t1 = clock()
    eq = se.sympify(equation)
    eq = eq.subs(
        {
            se.diff(se_gama, timet): cd_gamma,
            se.diff(phi, timet): cd_phi,
            se.diff(eps, timet): cd_eps,
            se.diff(tau, timet): cd_tau,

            se.diff(se_gama, timet, timet): cd_d_gamma,
            se.diff(phi, timet, timet): cd_d_phi,
            se.diff(eps, timet, timet): cd_d_eps,
            se.diff(tau, timet, timet): cd_d_tau,
        }
    )
    # a, b, c, d, e, f = se.symbols("a b c d e f")
    # eq = eq.subs(
    #     {
    #         se.diff(se_x, time, time): a,
    #         se.diff(se_y, time, time): b,
    #         se.diff(se_alpha, time, time): c,
    #         se.diff(se_beta, time, time): d,
    #         se.diff(se_gama, time, time): e,
    #         se.diff(se_psi, time, time): f
    #     }
    # )
    # eq, _ = fraction(together(parse_2_sympy_expression(str(transform_to_simpy(str(eq))))))
    eq = parse_2_sympy_expression(str(transform_to_simpy(str(eq))))

    print("len args = ", len(eq.args))
    t2 = clock()
    print("finish subs for eq#_%d Total time: %.2f [s]" % (args.n, t2 - t1))

    return eq


parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int)

args = parser.parse_args()

map_eq = {
    3: parse_2_sympy_expression(open("../lambda/part2/eq_3_without_lambda.txt").readline()),
    6: parse_2_sympy_expression(open("../lambda/part2/eq_6_without_lambda.txt").readline()),
    7: parse_2_sympy_expression(open("../lambda/part2/eq_7_without_lambda.txt").readline()),
    8: parse_2_sympy_expression(open("../lambda/part2/eq_8_without_lambda.txt").readline()),
    9: parse_2_sympy_expression(open("../lambda/part2/eq_9_without_lambda.txt").readline()),
    10: parse_2_sympy_expression(open("../lambda/part2/eq_10_without_lambda.txt").readline())
}

lock = Lock()
counter = Value('i', 0)
client = redis.Redis(host='localhost', port=6379, db=0)

print("######### kinematic eq_№ ", args.n)
eq = subs_kinematic(map_eq[args.n])

print("_____expand all parentheses in eq_№ ", args.n, "_____")


def time_benchmark(function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        function(*args, **kwargs)
        t2 = time.time()
        _, number = args
        print("finished expand term # %d. passed by time %.2f [m]" % (number, (t2 - t1) / 60))

    return wrapper


@time_benchmark
def sub_expand(term, number):
    global args, counter

    expanded_term = se.expand(
        se.sympify(term)
    )

    print("expanded via symengine. total number = %d term = %d" % (number, len(expanded_term.args)))

    result_dict = {}
    count = 0
    if type(expanded_term) is not se.Add:
        result_dict[count] = transform_to_simpy(
            str(simplification_expression(parse_2_sympy_expression(transform_to_simpy(str(expanded_term)))))
        )

        count += 1
    else:
        for term_ in expanded_term.args:
            top, bot = fraction(together(parse_2_sympy_expression(transform_to_simpy(str(term_)))))
            top = expand(simplification_expression(expand(expand_trig(top))))

            simpl_top = Zero()
            if type(top) == Mul:
                if not is_remove_small_term_with_velocities(top):
                    simpl_top = trigsimp(top)
            elif type(top) == Symbol:
                simpl_top = top
            else:
                for _term_ in top.args:
                    if not is_remove_small_term_with_velocities(_term_):
                        simpl_top += trigsimp(_term_)

            if simpl_top != sympy.core.numbers.Zero():
                expression = expand(simpl_top / bot)
                if type(expression) == Add:
                    for tterm in expression.args:
                        result_dict[count] = transform_to_simpy(str(tterm))
                        count += 1
                else:
                    result_dict[count] = transform_to_simpy(str(expression))
                    count += 1

    print("finished expand symengine. number = %d, count term = %d" % (number, len(result_dict.keys())))

    with open("./eq" + str(args.n) + "/term" + str(number) + '.json', 'w') as out:
        out.write(json.dumps(result_dict))

    del result_dict, expanded_term
    print("---- end %d ----" % number)
    # print("sended to redis eq#_%d , count_term = %d" % (number, len(expanded_term.args)))


print("count terms %d " % len(eq.args))
eq, _ = fraction(together(eq))
print("start")
tasks = []
print("----> ", transform_to_simpy(str(eq)))
for i, term in zip(range(len(eq.args)), eq.args):
    task = Process(target=sub_expand, args=(term, i))
    task.start()
    tasks.append(task)

print("size task = %d" % len(tasks))
for task in tasks:
    task.join()

result = {}
for i in range(counter.value - 1):
    try:
        decoded = client.get(str(args.n) + str(i)).decode('utf-8')
        result[i] = decoded
    except:
        result[i] = str(0)
        # print("exception. i = %d" % i)

print("counter = ", counter.value)
print("map size = ", len(result.keys()))

with open('expand_expression' + str(args.n) + '.json', 'w') as out:
    out.write(json.dumps(result))

print("FINISH")
