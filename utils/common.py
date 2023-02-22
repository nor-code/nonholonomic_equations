from sympy import cos, sin, nsimplify, expand, collect, Add, sympify, Mul, simplify, trigsimp, Pow
from sympy.core.numbers import Zero

from definitions.constants import *
from definitions.generic_coordinates import *
from definitions.lagrangian_multipliers import *
from definitions.moments import *
from definitions.denominators import *
import time
import tqdm


def base_remove_current_and_above_smallness(term, order):
    count = 0
    for tterm in term.args:
        if tterm == x1 or tterm == x2 or tterm == x3 or tterm == x8:
            count += 1
        elif type(tterm) is Pow and len(tterm.args) == 2:
            var, pow = tterm.args
            if var == x1 or var == x2 or var == x3 or var == x8:
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
    for term in tqdm.tqdm(expand(expression).args):
        count = base_remove_current_and_above_smallness(term, order)
        if count < order:
            simplified = Add(term, simplified)
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


# """ упрощаем в предположении, что τ и γ мал """
# def simplification_expression(expression):
#     simpl_raw = expression.subs(cos(x8), 1)
#     simpl_raw = simpl_raw.subs(sin(x8), x8)
#     simpl_raw = simpl_raw.subs(cos(x3), 1)
#     simpl_raw = simpl_raw.subs(sin(x3), x3)
#     # simpl_raw = simpl_raw.subs(sin(x2), x2)
#     # simpl_raw = simpl_raw.subs(cos(x2), 1)
#
#     simpl_raw = simpl_raw.subs(x3 * x8, 0)
#     # simpl_raw = simpl_raw.subs(x2 * x3, 0)
#     simpl_raw = simpl_raw.subs(x2 * x8, 0)
#
#     simpl_raw = simpl_raw.subs(x8 ** 2, 0)
#     simpl_raw = simpl_raw.subs(x3 ** 2, 0)
#     # simpl_raw = simpl_raw.subs(x2 ** 2, 0)
#
#     simpl_raw = simpl_raw.subs(x8 ** 3, 0)
#     simpl_raw = simpl_raw.subs(x3 ** 3, 0)
#     # simpl_raw = simpl_raw.subs(x2 ** 3, 0)
#
#     simpl_raw = simpl_raw.subs(x8 ** 4, 0)
#     simpl_raw = simpl_raw.subs(x3 ** 4, 0)
#     # simpl_raw = simpl_raw.subs(x2 ** 4, 0)
#
#     simpl_raw = simpl_raw.subs(x8 ** 5, 0)
#     simpl_raw = simpl_raw.subs(x3 ** 5, 0)
#     # simpl_raw = simpl_raw.subs(x2 ** 5, 0)
#
#     simpl_raw = simpl_raw.subs(x8 ** 6, 0)
#     simpl_raw = simpl_raw.subs(x3 ** 6, 0)
#     # simpl_raw = simpl_raw.subs(x2 ** 6, 0)
#
#     # simpl_raw = simpl_raw.subs(x2 * x3 * x8, 0)
#
#     res = sympify(simpl_raw)
#     return res


def simplification_expression(expression):
    """ упрощаем в предположении, что  α, γ и τ  мал """  # β
    simpl_raw = expression.subs(
        {
            cos(x1): 1 - x1 ** 2 / 2 - x1 ** 4 / 24,
            sin(x1): x1 - x1 ** 3 / 6,

            cos(x3): 1 - x3 ** 2 / 2 - x3 ** 4 / 24,
            sin(x3): x3 - x3 ** 2 / 6,

            cos(x8): 1 - x8 ** 2 / 2 - x8 ** 4 / 24,
            sin(x8): x8 - x8 ** 3 / 6,

            sin(x2): x2 - x2 ** 3 / 6,
            cos(x2): 1 - x2 ** 2 / 2 - x2 ** 4 / 24,
        }
    )
    return simpl_raw


# """ упрощаем в предположении, что β γ и τ  мал """
# def simplification_expression(expression):
#     simpl_raw = expression.subs(
#         {cos(x8): 1 - x8**2 / 2,
#          sin(x8): x8 - x8**3 / 6,
#
#          cos(x3): 1 - x3**2 / 2,
#          sin(x3): x3 - x3**3 / 6,
#
#          cos(x2): 1 - x2 ** 2 / 2,
#          sin(x2): x2 - x2**3 / 6,
#
#          x2 * x3 ** 2 * x8: 0,
#          x2 ** 2 * x3 * x8: 0,
#          x2 * x3 * x8 ** 2: 0,
#
#          x2**2 * x3**2: 0,
#          x2**2 * x8**2: 0,
#          x3**2 * x8**2: 0,
#
#          x3 * x8 ** 3: 0,
#          x3 ** 3 * x8: 0,
#          x2 ** 3 * x8: 0,
#          x2 ** 3 * x3: 0,
#          x2 * x3 ** 3: 0,
#          x2 * x8 ** 3: 0,
#
#          x2 ** 4: 0,
#          x3 ** 4: 0,
#          x8 ** 4: 0,
#
#          x2 ** 5: 0,
#          x3 ** 5: 0,
#          x8 ** 5: 0,
#
#          x2 ** 6: 0,
#          x3 ** 6: 0,
#          x8 ** 6: 0,
#
#          x2 ** 7: 0,
#          x3 ** 7: 0,
#          x8 ** 7: 0,
#
#          x2 ** 8: 0,
#          x3 ** 8: 0,
#          x8 ** 8: 0,
#
#          x2 ** 9: 0,
#          x3 ** 9: 0,
#          x8 ** 9: 0,
#          }
#     )
#     return sympify(simpl_raw)


def _add_simplify(coefficient, var):
    return Mul(
        simplification_expression(trigsimp(coefficient)),
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
        if not before_second_diff._eval_is_zero():
            print(d_d_var, ": ", before_second_diff)
            expression = sympify(expression - expand(Mul(before_second_diff * d_d_var)))
            simplified = Add(simplified, _add_simplify(before_second_diff, d_d_var))

    print("time collect second derivatives %.2f [m]" % ((time.time() - bedin) / 60))
    print("middle1 ", len(str(expression)))

    # коэффициенты перед diff(var_i, t) * diff(var_j, t)
    for d_one_d_another in mixed_diff_of_generic_coordinates:
        before_mixed_diff = collect(expression, d_one_d_another, exact=True).coeff(d_one_d_another)
        if not before_mixed_diff._eval_is_zero():
            expression = sympify(expression - expand(Mul(before_mixed_diff, d_one_d_another)))
            sss = _add_simplify(before_mixed_diff, d_one_d_another)
            simplified = Add(simplified, sss)
            print("done collect before: ", d_one_d_another)

    print("time collect mixed first derivatives ", round((time.time() - bedin) / 60, 2))
    print("middle2 ", len(str(expression)))

    # коэффициенты перед λ_i
    for λ_i in λ:
        before_lambda = collect(expression, λ_i).coeff(λ_i)
        if before_lambda.is_Symbol:
            expression = sympify(expression - expand(Mul(before_lambda, λ_i)))
            simplified = Add(simplified, _add_simplify(before_lambda, λ_i))
        elif not before_lambda._eval_is_zero():
            expression = sympify(expression - expand(Mul(before_lambda, λ_i)))
            simplified = Add(simplified, _add_simplify(before_lambda, λ_i))

    print("begin free")
    free_term = simplify(
        trigsimp(expand(expression)))  # simplification_expression(simplify(expression - trigsimp(expand(simplified))))
    print("free ", free_term)
    simplified = Add(simplified, free_term)

    end = time.time()
    print("total time ", round((end - bedin) / 60, 2))
    return simplified


def expand_and_collect_term_before_first_derivatives(expression):
    expression = simplification_expression(expand(expression))
    simplified = 0

    # коэффициенты перед diff(diff(var, t), t)
    for d_var in first_diff_generic_vars:
        before_second_diff = simplify(expand(collect(expression, d_var).coeff(d_var)))
        if not before_second_diff._eval_is_zero():
            simplified = Add(simplified, _add_simplify(before_second_diff, d_var))

    return simplified
