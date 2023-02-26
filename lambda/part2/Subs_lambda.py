from utils.to_sympy_expression import *
from utils.common import *
from utils.sympy_expression import parse_2_sympy_expression
from multiprocessing import Process
from sympy import linear_eq_to_matrix, together, fraction
import sys
sys.setrecursionlimit(10000000)

t1 = time.time()

λ_1_expression = parse_2_sympy_expression(open("../../lambda/part1/lambda_1.txt").readline())
λ_2_expression = parse_2_sympy_expression(open("../../lambda/part1/lambda_2.txt").readline())
λ_3_expression = parse_2_sympy_expression(open("../../lambda/part1/lambda_3.txt").readline())
λ_4_expression = parse_2_sympy_expression(open("../../lambda/part1/lambda_4.txt").readline())


def subs_lambda_to_equation(eq, i):
    global λ_1_expression, λ_2_expression, λ_3_expression, λ_4_expression
    eq_top, _ = fraction(together(eq.subs(λ_1, λ_1_expression)))
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=5)
    print(str(i), " part 1 finished")

    eq_top, _ = fraction(together(eq_top.subs(λ_2, λ_2_expression)))
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=5)
    print(str(i), " part 2 finished")

    eq_top, _ = fraction(together(eq_top.subs(λ_3, λ_3_expression)))
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=5)
    print(str(i), " part 3 finished")

    eq_top, _ = fraction(together(eq_top.subs(λ_4, λ_4_expression)))
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=5)
    print(str(i), " part 4 finished")

    eq_top = expand_and_collect_term_before_derivatives_and_lambda(eq_top)
    print(str(i), " expand and collect term")
    with open("../../lambda/part2/eq_" + str(i) + "_without_lambda.txt", 'w') as out:
        out.write(transform_to_simpy(str(eq_top)))


Eq1 = parse_2_sympy_expression(open("../../dynamic/eq1.txt").readline())
Eq2 = parse_2_sympy_expression(open("../../dynamic/eq2.txt").readline())
Eq3 = parse_2_sympy_expression(open("../../dynamic/eq3.txt").readline())
Eq4 = parse_2_sympy_expression(open("../../dynamic/eq4.txt").readline())
Eq5 = parse_2_sympy_expression(open("../../dynamic/eq5.txt").readline())
Eq7 = parse_2_sympy_expression(open("../../dynamic/eq7.txt").readline())

tasks = []
eqns = [Eq1, Eq2, Eq3, Eq4, Eq5, Eq7]
numbers = [1, 2, 3, 4, 5, 7]
for i in range(len(eqns)):
    task = Process(target=subs_lambda_to_equation, args=(eqns[i], numbers[i]))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()

print("finished substitute lambdas in 1,2,3,4,5,7 equations. total time = %.2f " % ((t2 - t1) / 60))
