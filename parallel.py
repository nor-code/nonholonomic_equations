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
expression = expand(eq_top)

print("_____begin collecting coefficient_____")
dict_expression = dict(
    zip(
        range(len(expression.args)), list(expression.args)
    )
)
print("size dictionary = ", len(dict_expression.keys()))

final_independent_coordinates = [x, y, x1, x2, x3, x5]
second_derivatives = [diff(diff(var, t), t) for var in final_independent_coordinates]
mixed_derivatives = list(mixed[0] * mixed[1] for mixed in itertools.combinations([diff(var, t) for var in final_independent_coordinates], 2))
[mixed_derivatives.append(diff(var, t) * diff(var, t)) for var in final_independent_coordinates]

coeff_dict = dict(
    zip(
        list(str(var) for var in [*second_derivatives, *mixed_derivatives]),
        zeros(len(second_derivatives) + len(mixed_derivatives))
    )
)
coeff_dict["free"] = 0

selected_term_indx = mp.Array('i', [0] * len(dict_expression.keys()), lock=True)


def get_result_from_redis(coeff_dict, redis_client):
    for key in coeff_dict.keys():
        value = redis_client.get(str(args.n) + key)
        if value is not None:
            coeff_dict[key] = value.decode('utf-8')


def get_free_term(_coeff_dict, _selected_term_indx, _dict_expression):
    free_term = 0
    for index in range(len(_dict_expression.keys())):
        if _selected_term_indx[index] != 1:
            free_term = Add(free_term, _dict_expression[index])
    _coeff_dict["free"] = transform_to_simpy(str(free_term))


def time_benchmark(function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        function(*args, **kwargs)
        t2 = time.time()
        if len(args) == 4:
            _, one, _, two = args
            print("for collect before %s * %s time execution: %.2f [s]" % (one, two, t2 - t1))
        else:
            _, one, _ = args
            print("for collect before %s time execution: %.2f [s]" % (one, t2 - t1))
    return wrapper


@time_benchmark
def processing(arr, d_one: Derivative, is_mixed, d_two: Optional[Derivative] = None):
    global dict_expression, coeff_dict, lock, args

    result_expression = 0
    first, second = False, False
    indexes = []
    for index, terms in dict_expression.items():
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

    if result_expression != 0:
        syms = d_one if not is_mixed else d_one * d_two
        simpl_coeff = trigsimp(collect(result_expression, syms).coeff(syms))

        result_expression = Mul(simpl_coeff, syms)

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
    task = Process(target=processing, args=(selected_term_indx, dd_var, False))
    task.start()
    tasks.append(task)

for d_one, d_two in itertools.combinations([diff(var, t) for var in final_independent_coordinates], 2):
    task = Process(target=processing, args=(selected_term_indx, d_one, True, d_two))
    task.start()
    tasks.append(task)

for d_var in list(diff(var, t) for var in final_independent_coordinates):
    task = Process(target=processing, args=(selected_term_indx, d_var * d_var, False))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

get_result_from_redis(coeff_dict, client)
get_free_term(coeff_dict, selected_term_indx, dict_expression)

for k, v in coeff_dict.items():
    coeff_dict[k] = str(v)

with open('./out' + str(args.n) + '.json', 'w') as out:
    out.write(json.dumps(coeff_dict))

print("selected = ", selected_term_indx[:])


