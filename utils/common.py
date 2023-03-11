import time

import tqdm
from sympy import cos, sin, expand, collect, Add, sympify, Mul, simplify, trigsimp, Pow, Derivative
from sympy.core.numbers import Zero, One

from definitions.denominators import *
from definitions.generic_coordinates import *
from definitions.lagrangian_multipliers import *


def is_remove_small_term_with_velocities(term, small_coordinates=None):
    if small_coordinates is None:
        small_coordinates = [x, y, x1, x2, x3, x4, x5, x6, x7, x8]

    count = base_remove_current_and_above_smallness(term, 2)
    if count >= 2:
        return True

    for sub_term in term.args:
        if type(sub_term) == Pow and type(sub_term.args[0]) == Derivative:
            derivative = sub_term.args[0]
            variable = derivative.args[0]
            if variable in small_coordinates:
                count += sub_term.args[1]
                if count >= 2:
                    return True
        elif type(sub_term) == Derivative:
            variable = sub_term.args[0]
            if variable in small_coordinates:
                count += 1
                if count >= 2:
                    return True

    return False


def base_remove_current_and_above_smallness(term, order, small_coordinates=None):
    if small_coordinates is None:
        small_coordinates = [x1, x2, x3, x4, x5, x6, x7, x8]

    count = 0
    if type(term) == Derivative:
        return count

    for tterm in term.args:
        if tterm in small_coordinates:
            count += 1
        elif type(tterm) is Pow and len(tterm.args) == 2:
            var, pow = tterm.args
            if var in small_coordinates:
                count += pow
        if count >= order:
            break
    return count


def remove_fourth_and_above_smallness_from_one_term(term):
    if base_remove_current_and_above_smallness(term, 4) < 4:
        return term
    else:
        return 0


def remove_current_and_above_smallness_from_one_term(term, order):
    if base_remove_current_and_above_smallness(term, order) < order:
        return term
    else:
        return 0


def __is_denominator_sym(symbol):
    return symbol in [d_phi_bot, d_eps_bot, d_tau_bot, d_del_bot, d_d_phi_bot, d_d_eps_bot, d_d_tau_bot, d_d_del_bot]


def remove_required_and_above_smallness_from_expression(expression, order):
    simplified = Zero()
    # if (type(expression) == Pow and __is_denominator_sym(expression.args[0])) or __is_denominator_sym(expression):
    #     return expression
    if type(expression) in (Symbol, One, Derivative):
        return expression

    if type(expression) == Mul:
        smallness_order = base_remove_current_and_above_smallness(expression, order)
        if smallness_order < order:
            return expression
        else:
            return 0

    for term in expand(expression).args: #tqdm.tqdm(expand(expression).args):
        count = base_remove_current_and_above_smallness(term, order)
        if count < order:
            try:
                simplified += term
            except:
                print()
    return simplified


def remove_fourth_and_above_smallness_from_expression(expression):
    simplified = Zero()
    # if (type(expression) == Pow and __is_denominator_sym(expression.args[0])) or __is_denominator_sym(expression):
    #     return expression
    for term in expand(expression).args:
        count = base_remove_current_and_above_smallness(term, 4)
        if count < 4:
            simplified = Add(term, simplified)
    return simplified


def remove_third_and_above_smallness_from_one_term(term):
    if base_remove_current_and_above_smallness(term, 3) < 3:
        return term
    else:
        return 0


def remove_third_and_above_smallness_from_expression(expression):
    if expression == 1:
        return 1
    simplified = Zero()
    # if (type(expression) == Pow and __is_denominator_sym(expression.args[0])) or __is_denominator_sym(expression):
    #     return expression
    for term in expand(expression).args:
        count = base_remove_current_and_above_smallness(term, 3)
        if count < 3:
            simplified = Add(term, simplified)
    return simplified


def get_count_files_in_directory(path):
    import os
    count = 0
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            count += 1
    return count


def simplification_expression(expression):
    """ упрощаем в предположении, что  α, γ и τ  мал """  # β
    simpl_raw = expression.subs(
        {
            cos(x1): 1,
            sin(x1): x1,

            cos(x2): 1,
            sin(x2): x2,

            cos(x3): 1,
            sin(x3): x3,

            cos(x5): 1,
            sin(x5): x5,

            cos(x6): 1,
            sin(x6): x6,

            cos(x7): 1,
            sin(x7): x7,

            cos(x8): 1,
            sin(x8): x8
        }
    )
    return simpl_raw


def _add_simplify(coefficient, var):
    return Mul(
        trigsimp(coefficient),
        var
    )


def expand_and_collect_term_before_derivatives_and_lambda(expression):
    bedin = time.time()
    # expression = nsimplify(simplification_expression(expand(expression)), rational=True)
    print(expression)
    print("begin ", len(str(expression)))
    simplified = 0

    # коэффициенты перед diff(diff(var, t), t)
    for d_d_var in second_diff_generic_coord:
        before_second_diff = collect(expression, d_d_var).coeff(d_d_var)
        if type(before_second_diff) is Symbol or not before_second_diff._eval_is_zero():
            print(d_d_var, ": ", before_second_diff)
            expression = sympify(expression - expand(Mul(before_second_diff * d_d_var)))
            simplified = Add(simplified, _add_simplify(before_second_diff, d_d_var))

    print("time collect second derivatives %.2f [m]" % ((time.time() - bedin) / 60))
    print("middle1 ", len(str(expression)))

    # коэффициенты перед diff(var_i, t) * diff(var_j, t)
    for d_one_d_another in mixed_diff_of_generic_coordinates:
        before_mixed_diff = collect(expression, d_one_d_another, exact=True).coeff(d_one_d_another)
        if type(before_mixed_diff) is Symbol or not before_mixed_diff._eval_is_zero():
            expression = sympify(expression - expand(Mul(before_mixed_diff, d_one_d_another)))
            sss = _add_simplify(before_mixed_diff, d_one_d_another)
            simplified = Add(simplified, sss)
            print("done collect before: ", d_one_d_another)

    print("time collect mixed first derivatives ", round((time.time() - bedin) / 60, 2))
    print("middle2 ", len(str(expression)))

    # коэффициенты перед λ_i
    for λ_i in λ:
        before_lambda = collect(expression, λ_i).coeff(λ_i)
        if before_lambda.is_Symbol or not before_lambda._eval_is_zero():
            expression = sympify(expression - expand(Mul(before_lambda, λ_i)))
            simplified = Add(simplified, _add_simplify(before_lambda, λ_i))

    print("begin free")
    free_term = simplify(
        trigsimp(expand(expression))
    )  # simplification_expression(simplify(expression - trigsimp(expand(simplified))))
    print("free ", free_term)
    simplified = Add(simplified, free_term)

    end = time.time()
    print("total time ", round((end - bedin) / 60, 2))
    return simplified


def expand_and_collect_term_before_first_derivatives(expression):
    expression = expand(expression)
    simplified = 0

    # коэффициенты перед diff(var, t)
    for d_var in first_diff_generic_vars:
        before_second_diff = collect(expression, d_var).coeff(d_var)
        if not before_second_diff._eval_is_zero():
            simplified = Add(simplified, Mul(trigsimp(before_second_diff), d_var))

    return simplified
