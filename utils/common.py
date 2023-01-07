from sympy import *
from definitions.constants import *
from definitions.generic_coordinates import *
from definitions.lagrangian_multipliers import *
from definitions.moments import *
import time


""" упрощаем в предположении, что (β) τ и γ мал """
def simplification_expression(expression):
    simpl_raw = expression.subs(cos(x8), 1)
    simpl_raw = simpl_raw.subs(sin(x8), x8)
    simpl_raw = simpl_raw.subs(cos(x3), 1)
    simpl_raw = simpl_raw.subs(sin(x3), x3)
    # simpl_raw = simpl_raw.subs(sin(x2), x2)
    # simpl_raw = simpl_raw.subs(cos(x2), 1)

    simpl_raw = simpl_raw.subs(x3 * x8, 0)
    # simpl_raw = simpl_raw.subs(x2 * x3, 0)
    simpl_raw = simpl_raw.subs(x2 * x8, 0)

    simpl_raw = simpl_raw.subs(x8 ** 2, 0)
    simpl_raw = simpl_raw.subs(x3 ** 2, 0)
    # simpl_raw = simpl_raw.subs(x2 ** 2, 0)

    simpl_raw = simpl_raw.subs(x8 ** 3, 0)
    simpl_raw = simpl_raw.subs(x3 ** 3, 0)
    # simpl_raw = simpl_raw.subs(x2 ** 3, 0)

    simpl_raw = simpl_raw.subs(x8 ** 4, 0)
    simpl_raw = simpl_raw.subs(x3 ** 4, 0)
    # simpl_raw = simpl_raw.subs(x2 ** 4, 0)

    simpl_raw = simpl_raw.subs(x8 ** 5, 0)
    simpl_raw = simpl_raw.subs(x3 ** 5, 0)
    # simpl_raw = simpl_raw.subs(x2 ** 5, 0)

    simpl_raw = simpl_raw.subs(x8 ** 6, 0)
    simpl_raw = simpl_raw.subs(x3 ** 6, 0)
    # simpl_raw = simpl_raw.subs(x2 ** 6, 0)

    # simpl_raw = simpl_raw.subs(x2 * x3 * x8, 0)

    res = sympify(simpl_raw)
    return res


def _add_simplify(coefficient, var):
    return Mul(
        simplification_expression(trigsimp(coefficient)),
        var
    )


def expand_and_collect_term_before_derivatives_and_lambda(expression):
    bedin = time.time()
    expression = nsimplify(simplification_expression(expand(expression)), rational=True)
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
    free_term = simplify(trigsimp(expand(expression))) # simplification_expression(simplify(expression - trigsimp(expand(simplified))))
    print("free ", free_term)
    simplified = Add(simplified, free_term)

    end = time.time()
    print("total time ", round((end - bedin) / 60, 2))
    return simplified


def expand_and_collect_term_before_first_derivatives(expression):
    expression = nsimplify(simplification_expression(expand(expression)), rational=True)
    simplified = 0

    # коэффициенты перед diff(diff(var, t), t)
    for d_var in first_diff_generic_vars:
        before_second_diff = collect(expression, d_var).coeff(d_var)
        if not before_second_diff._eval_is_zero():
            simplified = Add(simplified, _add_simplify(before_second_diff, d_var))

    return simplified