import json
import multiprocessing as mp
from multiprocessing import Process, Lock
from typing import *
import redis
import pickle
from Subs_kinematic import *
from utils.to_sympy_expression import transform_to_simpy

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int)

args = parser.parse_args()


map_eq = {
    1: Eq1_simpl,
    2: Eq2_simpl,
    3: Eq3_simpl,
    4: Eq4_simpl,
    5: Eq5_simpl,
    7: Eq7_simpl
}

lock = Lock()
client = redis.Redis(host='localhost', port=6379, db=0)

print("######### kinematic eq_№ ", args.n)
eq = subs_kinematic(map_eq[args.n], d_phi, d_delta, d_eps, d_tau, d_d_phi, d_d_delta, d_d_eps, d_d_tau)

print("_____finished subs kinematic's expression for eq_№ ", args.n, "_____")
eq_top, eq_bot = fraction(together(eq))

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
    global args
    print("\nstart expand ", number)
    expanded_term = simplification_expression(expand(term))
    print("finished expand ", number)
    client.set(str(args.n) + str(number), transform_to_simpy(str(expanded_term)))
    print("sended to redis ", number)


print("count terms %d " % len(eq_top.args))

tasks = []
for i, term in zip(range(len(eq_top.args)), eq_top.args):
    task = Process(target=sub_expand, args=(term, i))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

result = ""
for i in range(len(eq_top.args)):
    result = result + client.get(str(args.n) + str(i)).decode('utf-8')
    print("res: ", len(result))

with open('expand_expression' + str(args.n) + '.txt', 'w') as out:
    out.write(result)

print(len(eq_top.args))


