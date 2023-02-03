import json
import multiprocessing as mp
import sys
import time
from multiprocessing import Process, Lock, Pool
from typing import *
import tqdm
import re
import redis
from sympy import Add, Derivative, trigsimp, simplify, Mul

from utils.sympy_expression import parse_2_sympy_expression

sys.setrecursionlimit(100000)

import argparse
from utils.common import get_count_files_in_directory, remove_third_and_above_smallness_from_expression
from utils.to_sympy_expression import transform_to_simpy
from definitions.generic_coordinates import *

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int)

args = parser.parse_args()

map_dir_eq_path = {
    1: "../expand_parallel/eq1",
    2: "../expand_parallel/eq2",
    3: "../expand_parallel/eq3",
    4: "../expand_parallel/eq4",
    5: "../expand_parallel/eq5",
    7: "../expand_parallel/eq7"
}
final_independent_coordinates = [x, y, x1, x2, x3, x5]

second_derivatives = [diff(diff(var, t), t) for var in final_independent_coordinates]
second_dict_name = dict(
    zip(
        second_derivatives,
        [re.sub('[)( ,]', '_', str(dd_var)).replace('Derivative', 'd_d').replace('t____', '') for dd_var in second_derivatives])
)

mixed_derivatives = list(mixed[0] * mixed[1] for mixed in itertools.combinations([diff(var, t) for var in final_independent_coordinates], 2))
[mixed_derivatives.append(diff(var, t) * diff(var, t)) for var in final_independent_coordinates]
mixed_dict_name = dict(
    zip(
        mixed_derivatives,
        [re.sub('[)( ,*]', '_', str(mixed)).replace('Derivative', 'd').replace('t___', '') for mixed in mixed_derivatives]
    )
)

count_files = get_count_files_in_directory(map_dir_eq_path[args.n])

dict_expression = {}
counter = 0
for i in tqdm.tqdm(range(count_files)):
    for k, raw_term in json.load(open(map_dir_eq_path[args.n] + '/' + "term" + str(i) + '.json')).items():
        dict_expression[counter] = parse_2_sympy_expression(raw_term)
        counter += 1

lock = Lock()
client = redis.Redis(host='localhost', port=6379, db=0)

print("_____begin collecting coefficient_____")
print("_____size dictionary = %d _____" % len(dict_expression.keys()))


coeff_dict = dict(
    zip(
        list(str(var) for var in [*second_derivatives, *mixed_derivatives]),
        [0] * (len(second_derivatives) + len(mixed_derivatives))
    )
)
coeff_dict["free"] = 0

selected_term_indx = mp.Array('i', [0] * len(dict_expression.keys()), lock=True)


def get_result_from_redis(coeff_dict, redis_client):
    for key in coeff_dict.keys():
        value = redis_client.get(str(args.n) + key)
        if value is not None:
            coeff_dict[key] = value.decode('utf-8')


def get_free_term(_coeff_dict, _selected_term_indx, _dict_expression, eq_number):
    free_term = 0
    for index in range(len(_dict_expression.keys())):
        if _selected_term_indx[index] != 1:
            free_term = Add(free_term, _dict_expression[index])
    _coeff_dict["free"] = transform_to_simpy(str(free_term))

    with open("./eq" + str(eq_number) + '/free_term.txt', 'w') as out:
        out.write(transform_to_simpy(str(_coeff_dict["free"])))


def time_collecting(function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        function(*args, **kwargs)
        t2 = time.time()
        if len(args) == 6:
            _, _, _, one, _, two = args
            print("for collect before %s * %s time execution: %.2f [m]" % (one, two, (t2 - t1)/60))
        else:
            _, _, _, one, _ = args
            print("for collect before %s time execution: %.2f [m]" % (one, (t2 - t1)/60))
    return wrapper


@time_collecting
def collect_before_derivatives(arr, eq_number, name, d_one: Derivative, is_mixed, d_two: Optional[Derivative] = None):
    global dict_expression, coeff_dict, lock, args

    result_expression = 0
    first, second = False, False
    indexes = []
    for index, terms in dict_expression.items():
        if arr[index] == 1:
            continue
        for term in terms.args:
            if not is_mixed:
                if term == d_one:
                    result_expression = Add(result_expression, terms)
                    indexes.append(index)
                    # print("detected for ", self.d_one, " expr: ", result_expression)
                    break
            else:
                if term == d_one:
                    first = True
                elif term == d_two:
                    second = True

        if first and second:
            # print("find for mixed coordinates: ", self.d_one, self.d_two, " = ", terms)
            result_expression = Add(result_expression, terms)
            indexes.append(index)

        first, second = False, False

    # syms = d_one if not is_mixed else d_one * d_two
    # simpl_coeff = trigsimp(collect(result_expression, syms).coeff(syms))

    # result_expression = Mul(simpl_coeff, syms)
    if type(result_expression) != Mul:
        result_expression = remove_third_and_above_smallness_from_expression(result_expression)

    result_expression = simplify(result_expression)
    with open('./eq' + str(eq_number) + '/' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result_expression)))
    print("write to file collected coefficient = %s" % (str(d_one) + "*" + str(d_two)))

    client.set(str(args.n) + str(d_one) if not is_mixed else str(args.n) + str(d_one * d_two),
               transform_to_simpy(str(result_expression)))

    if len(indexes) != 0:
        lock.acquire()
        print("\nthread selected from common dictionary indexes = ", indexes)
        for i in indexes:
            arr[i] = 1
        lock.release()


tasks = []
for dd_var in second_derivatives:
    task = Process(
        target=collect_before_derivatives,
        args=(selected_term_indx, args.n, second_dict_name[dd_var], dd_var, False)
    )
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()
print("\n####### finished collecting before second derivatives #######\n")


tasks = []
for d_one, d_two in itertools.combinations([diff(var, t) for var in final_independent_coordinates], 2):
    task = Process(
        target=collect_before_derivatives,
        args=(selected_term_indx, args.n, mixed_dict_name[d_one*d_two], d_one, True, d_two)
    )
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()
print("\n####### finished collecting before mixed derivatives #######\n")


tasks = []
for d_var in list(diff(var, t) for var in final_independent_coordinates):
    task = Process(
        target=collect_before_derivatives,
        args=(selected_term_indx, args.n, mixed_dict_name[d_var * d_var], d_var * d_var, False)
    )
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()
print("\n####### finished collecting before squared derivatives #######\n")

t1 = time.time()
get_result_from_redis(coeff_dict, client)
get_free_term(coeff_dict, selected_term_indx, dict_expression, args.n)
t2 = time.time()

print("end collect free term. spent timw = %.2f [m]" % ((t2 - t1)/60))
# for k, v in coeff_dict.items():
#     coeff_dict[k] = str(v)
#
# with open('./out' + str(args.n) + '.json', 'w') as out:
#     out.write(json.dumps(coeff_dict))

print("selected = ", selected_term_indx[:])


