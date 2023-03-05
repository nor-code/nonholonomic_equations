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
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=2)  # order = 5
    print(str(i), " part 1 finished")

    eq_top, _ = fraction(together(eq_top.subs(λ_2, λ_2_expression)))
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=2)  # order = 5
    print(str(i), " part 2 finished")

    eq_top, _ = fraction(together(eq_top.subs(λ_3, λ_3_expression)))
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=2)  # order = 5
    print(str(i), " part 3 finished")

    eq_top, _ = fraction(together(eq_top.subs(λ_4, λ_4_expression)))
    eq_top = remove_required_and_above_smallness_from_expression(expand(eq_top, deep=True), order=2)  # order = 5
    print(str(i), " part 4 finished")

    eq_top = expand_and_collect_term_before_derivatives_and_lambda(eq_top)
    print(str(i), " expand and collect term")
    with open("../../lambda/part2/eq_" + str(i) + "_without_lambda.txt", 'w') as out:
        out.write(transform_to_simpy(str(eq_top)))


Eq3 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq3.txt").readline())  # open("../../dynamic/eq1.txt")
Eq6 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq6.txt").readline())  # open("../../dynamic/eq2.txt")
Eq7 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq7.txt").readline())  # open("../../dynamic/eq3.txt")
Eq8 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq8.txt").readline())  # open("../../dynamic/eq4.txt")
Eq9 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq9.txt").readline())  # open("../../dynamic/eq5.txt")
Eq10 = parse_2_sympy_expression(open("../../dynamic/small_velocity/eq10.txt").readline())  # open("../../dynamic/eq6.txt")

tasks = []
eqns = [Eq3, Eq6, Eq7, Eq8, Eq9, Eq10]
numbers = [3, 6, 7, 8, 9, 10]
for i in range(len(eqns)):
    task = Process(target=subs_lambda_to_equation, args=(eqns[i], numbers[i]))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

t2 = time.time()

print("finished substitute lambdas in 1, 2, 3, 4, 5, 7 equations. total time = %.2f " % ((t2 - t1) / 60))
