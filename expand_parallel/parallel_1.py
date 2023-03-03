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


d_phi_top = parse_2_sympy_expression(open("../kinematic/part2/d_phi.txt").readline())
d_phi_bot = parse_2_sympy_expression(open("../kinematic/part2/d_phi_bottom.txt").readline())

d_delta_top = parse_2_sympy_expression(open("../kinematic/part2/d_del.txt").readline())
d_delta_bot = parse_2_sympy_expression(open("../kinematic/part2/d_del_bottom.txt").readline())

d_eps_top = parse_2_sympy_expression(open("../kinematic/part2/d_eps.txt").readline())
d_eps_bot = parse_2_sympy_expression(open("../kinematic/part2/d_eps_bottom.txt").readline())

d_tau_top = parse_2_sympy_expression(open("../kinematic/part2/d_tau.txt").readline())
d_tau_bot = parse_2_sympy_expression(open("../kinematic/part2/d_tau_bottom.txt").readline())

d_d_phi = parse_2_sympy_expression(open("../kinematic/part4/d_d_phi.txt").readline())
d_d_delta = parse_2_sympy_expression(open("../kinematic/part4/d_d_del.txt").readline())
d_d_eps = parse_2_sympy_expression(open("../kinematic/part4/d_d_eps.txt").readline())
d_d_tau = parse_2_sympy_expression(open("../kinematic/part4/d_d_tau.txt").readline())

cd_phi = se.sympify(d_phi_top/d_phi_bot)
cd_delta = se.sympify(d_delta_top/d_delta_bot)
cd_eps = se.sympify(d_eps_top/d_eps_bot)
cd_tau = se.sympify(d_tau_top/d_tau_bot)

cd_d_phi = se.sympify(d_d_phi)
cd_d_delta = se.sympify(d_d_delta)
cd_d_eps = se.sympify(d_d_eps)
cd_d_tau = se.sympify(d_d_tau)


def subs_kinematic(equation):
    t1 = clock()
    eq = se.sympify(equation)
    eq = eq.subs(
        {
            se.diff(phi, timet): cd_phi,
            se.diff(delta, timet): cd_delta,
            se.diff(eps, timet): cd_eps,
            se.diff(tau, timet): cd_tau,

            se.diff(phi, timet, timet): cd_d_phi,
            se.diff(delta, timet, timet): cd_d_delta,
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
    1: parse_2_sympy_expression(open("../lambda/part2/eq_1_without_lambda.txt").readline()),
    2: parse_2_sympy_expression(open("../lambda/part2/eq_2_without_lambda.txt").readline()),
    3: parse_2_sympy_expression(open("../lambda/part2/eq_3_without_lambda.txt").readline()),
    4: parse_2_sympy_expression(open("../lambda/part2/eq_4_without_lambda.txt").readline()),
    5: parse_2_sympy_expression(open("../lambda/part2/eq_5_without_lambda.txt").readline()),
    7: parse_2_sympy_expression(open("../lambda/part2/eq_7_without_lambda.txt").readline())
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

    each_dict = {}

    for i in tqdm.tqdm(range(len(term.args))):
        component = term.args[i]
        if type(component) is Pow and type(component.args[0]) is Add:
            expanded_term = se.expand(se.sympify(component))
            simpl_expanded_term = 0
            for term_ in expanded_term.args:
                top, bot = fraction(together(parse_2_sympy_expression(transform_to_simpy(str(term_)))))
                top = expand(simplification_expression(expand(expand_trig(top))))

                if type(top) == Mul:
                    simpl_top = remove_current_and_above_smallness_from_one_term(top, order=5)
                    simpl_expanded_term += simpl_top
                else:
                    simpl_top = remove_required_and_above_smallness_from_expression(top, order=5)
                    simpl_expanded_term += simpl_top
            each_dict[i] = simpl_expanded_term

        else:
            each_dict[i] = se.sympify(component)

    def multiply_in_series(dict_expanded):
        begin = 1
        for element in dict_expanded.values():
            expanded = se.expand(se.Mul(se.sympify(element), begin))
            if type(expanded) is se.Integer or type(expanded) is se.Mul:
                begin = expanded
                continue

            simplified = 0
            for term_ in expanded.args:
                top, bot = fraction(together(parse_2_sympy_expression(transform_to_simpy(str(term_)))))
                top = expand(simplification_expression(expand(expand_trig(top))))

                if type(top) == Mul:
                    simpl_top = remove_current_and_above_smallness_from_one_term(top, order=5)
                    simplified += simpl_top
                else:
                    simpl_top = remove_required_and_above_smallness_from_expression(top, order=5)
                    simplified += simpl_top
            begin = simplified
        return begin

    expanded_term = multiply_in_series(each_dict)

    print("expanded via symengine. total number = %d" % number)

    result_dict = {}
    count = 0

    if type(expanded_term) in (se.Integer, int):
        result_dict[count] = transform_to_simpy(str(expanded_term))
        count += 1
    else:
        for term_ in expanded_term.args:
            top, bot = fraction(together(parse_2_sympy_expression(transform_to_simpy(str(term_)))))
            top = expand(simplification_expression(expand(expand_trig(top))))

            if type(top) == Mul:
                simpl_top = remove_current_and_above_smallness_from_one_term(top, order=5)
            else:
                simpl_top = remove_required_and_above_smallness_from_expression(top, order=5)

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
for i, term in zip(range(len(eq.args)), eq.args):
    task = Process(target=sub_expand, args=(term, i))
    task.start()
    tasks.append(task)
    # if i % 2 == 0:
    #     for task in tasks:
    #         task.join()
    #     print("finished tasks. size of tasks = %d. create next tasks" % (len(tasks)))
    #     tasks = []

print("size task = %d" % len(tasks))
for task in tasks:
    task.join()

# print("LAST PART")
# task = []
# for i, term in zip(range(part_one, len(eq.args)), eq.args[part_one:]):
#     task = Process(target=sub_expand, args=(term, i))
#     task.start()
#     tasks.append(task)
#
# print("size task = %d" % len(tasks))
# for task in tasks:
#     task.join()

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
