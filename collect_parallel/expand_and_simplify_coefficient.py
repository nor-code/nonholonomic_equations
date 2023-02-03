# после того, как раскрыли все скобки и сгруппировали все члены
# нужно поставить значения и снова это упростить
# d_phi_bot     d_del_bot     d_eps_bot     d_tau_bot
# d_d_phi_bot   d_d_del_bot   d_d_eps_bot   d_d_tau_bot
from sympy import fraction, expand, simplify
from sympy.core.numbers import Zero

from definitions.denominators import *
from utils.common import remove_third_and_above_smallness_from_expression
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import transform_to_simpy

dict_coeff = {
    'eq1/d_x_2.txt': parse_2_sympy_expression(open("./eq1/d_x_2.txt").readline()),
    'eq1/d_x_t__d_y_t_.txt': parse_2_sympy_expression(open("./eq1/d_x_t__d_y_t_.txt").readline()),
    'eq1/d_x_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq1/d_x_t__d_α_t_.txt").readline()),
    'eq1/d_x_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq1/d_x_t__d_β_t_.txt").readline()),
    'eq1/d_x_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq1/d_x_t__d_γ_t_.txt").readline()),
    'eq1/d_x_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq1/d_x_t__d_ψ_t_.txt").readline()),
    'eq1/d_y_2.txt': parse_2_sympy_expression(open("./eq1/d_y_2.txt").readline()),
    'eq1/d_y_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq1/d_y_t__d_α_t_.txt").readline()),
    'eq1/d_y_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq1/d_y_t__d_β_t_.txt").readline()),
    'eq1/d_y_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq1/d_y_t__d_γ_t_.txt").readline()),
    'eq1/d_y_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq1/d_y_t__d_ψ_t_.txt").readline()),
    'eq1/d_α_2.txt': parse_2_sympy_expression(open("./eq1/d_α_2.txt").readline()),
    'eq1/d_α_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq1/d_α_t__d_β_t_.txt").readline()),
    'eq1/d_α_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq1/d_α_t__d_γ_t_.txt").readline()),
    'eq1/d_α_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq1/d_α_t__d_ψ_t_.txt").readline()),
    'eq1/d_β_2.txt': parse_2_sympy_expression(open("./eq1/d_β_2.txt").readline()),
    'eq1/d_β_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq1/d_β_t__d_γ_t_.txt").readline()),
    'eq1/d_β_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq1/d_β_t__d_ψ_t_.txt").readline()),
    'eq1/d_γ_2.txt': parse_2_sympy_expression(open("./eq1/d_γ_2.txt").readline()),
    'eq1/d_γ_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq1/d_γ_t__d_ψ_t_.txt").readline()),
    'eq1/d_ψ_2.txt': parse_2_sympy_expression(open("./eq1/d_ψ_2.txt").readline()),

    'eq2/d_x_2.txt': parse_2_sympy_expression(open("./eq2/d_x_2.txt").readline()),
    'eq2/d_x_t__d_y_t_.txt': parse_2_sympy_expression(open("./eq2/d_x_t__d_y_t_.txt").readline()),
    'eq2/d_x_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq2/d_x_t__d_α_t_.txt").readline()),
    'eq2/d_x_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq2/d_x_t__d_β_t_.txt").readline()),
    'eq2/d_x_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq2/d_x_t__d_γ_t_.txt").readline()),
    'eq2/d_x_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq2/d_x_t__d_ψ_t_.txt").readline()),
    'eq2/d_y_2.txt': parse_2_sympy_expression(open("./eq2/d_y_2.txt").readline()),
    'eq2/d_y_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq2/d_y_t__d_α_t_.txt").readline()),
    'eq2/d_y_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq2/d_y_t__d_β_t_.txt").readline()),
    'eq2/d_y_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq2/d_y_t__d_γ_t_.txt").readline()),
    'eq2/d_y_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq2/d_y_t__d_ψ_t_.txt").readline()),
    'eq2/d_α_2.txt': parse_2_sympy_expression(open("./eq2/d_α_2.txt").readline()),
    'eq2/d_α_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq2/d_α_t__d_β_t_.txt").readline()),
    'eq2/d_α_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq2/d_α_t__d_γ_t_.txt").readline()),
    'eq2/d_α_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq2/d_α_t__d_ψ_t_.txt").readline()),
    'eq2/d_β_2.txt': parse_2_sympy_expression(open("./eq2/d_β_2.txt").readline()),
    'eq2/d_β_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq2/d_β_t__d_γ_t_.txt").readline()),
    'eq2/d_β_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq2/d_β_t__d_ψ_t_.txt").readline()),
    'eq2/d_γ_2.txt': parse_2_sympy_expression(open("./eq2/d_γ_2.txt").readline()),
    'eq2/d_γ_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq2/d_γ_t__d_ψ_t_.txt").readline()),
    'eq2/d_ψ_2.txt': parse_2_sympy_expression(open("./eq2/d_ψ_2.txt").readline()),

    'eq3/d_x_2.txt': parse_2_sympy_expression(open("./eq3/d_x_2.txt").readline()),
    'eq3/d_x_t__d_y_t_.txt': parse_2_sympy_expression(open("./eq3/d_x_t__d_y_t_.txt").readline()),
    'eq3/d_x_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq3/d_x_t__d_α_t_.txt").readline()),
    'eq3/d_x_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq3/d_x_t__d_β_t_.txt").readline()),
    'eq3/d_x_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq3/d_x_t__d_γ_t_.txt").readline()),
    'eq3/d_x_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq3/d_x_t__d_ψ_t_.txt").readline()),
    'eq3/d_y_2.txt': parse_2_sympy_expression(open("./eq3/d_y_2.txt").readline()),
    'eq3/d_y_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq3/d_y_t__d_α_t_.txt").readline()),
    'eq3/d_y_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq3/d_y_t__d_β_t_.txt").readline()),
    'eq3/d_y_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq3/d_y_t__d_γ_t_.txt").readline()),
    'eq3/d_y_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq3/d_y_t__d_ψ_t_.txt").readline()),
    'eq3/d_α_2.txt': parse_2_sympy_expression(open("./eq3/d_α_2.txt").readline()),
    'eq3/d_α_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq3/d_α_t__d_β_t_.txt").readline()),
    'eq3/d_α_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq3/d_α_t__d_γ_t_.txt").readline()),
    'eq3/d_α_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq3/d_α_t__d_ψ_t_.txt").readline()),
    'eq3/d_β_2.txt': parse_2_sympy_expression(open("./eq3/d_β_2.txt").readline()),
    'eq3/d_β_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq3/d_β_t__d_γ_t_.txt").readline()),
    'eq3/d_β_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq3/d_β_t__d_ψ_t_.txt").readline()),
    'eq3/d_γ_2.txt': parse_2_sympy_expression(open("./eq3/d_γ_2.txt").readline()),
    'eq3/d_γ_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq3/d_γ_t__d_ψ_t_.txt").readline()),
    'eq3/d_ψ_2.txt': parse_2_sympy_expression(open("./eq3/d_ψ_2.txt").readline()),

    'eq4/d_x_2.txt': parse_2_sympy_expression(open("./eq4/d_x_2.txt").readline()),
    'eq4/d_x_t__d_y_t_.txt': parse_2_sympy_expression(open("./eq4/d_x_t__d_y_t_.txt").readline()),
    'eq4/d_x_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq4/d_x_t__d_α_t_.txt").readline()),
    'eq4/d_x_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq4/d_x_t__d_β_t_.txt").readline()),
    'eq4/d_x_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq4/d_x_t__d_γ_t_.txt").readline()),
    'eq4/d_x_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq4/d_x_t__d_ψ_t_.txt").readline()),
    'eq4/d_y_2.txt': parse_2_sympy_expression(open("./eq4/d_y_2.txt").readline()),
    'eq4/d_y_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq4/d_y_t__d_α_t_.txt").readline()),
    'eq4/d_y_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq4/d_y_t__d_β_t_.txt").readline()),
    'eq4/d_y_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq4/d_y_t__d_γ_t_.txt").readline()),
    'eq4/d_y_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq4/d_y_t__d_ψ_t_.txt").readline()),
    'eq4/d_α_2.txt': parse_2_sympy_expression(open("./eq4/d_α_2.txt").readline()),
    'eq4/d_α_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq4/d_α_t__d_β_t_.txt").readline()),
    'eq4/d_α_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq4/d_α_t__d_γ_t_.txt").readline()),
    'eq4/d_α_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq4/d_α_t__d_ψ_t_.txt").readline()),
    'eq4/d_β_2.txt': parse_2_sympy_expression(open("./eq4/d_β_2.txt").readline()),
    'eq4/d_β_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq4/d_β_t__d_γ_t_.txt").readline()),
    'eq4/d_β_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq4/d_β_t__d_ψ_t_.txt").readline()),
    'eq4/d_γ_2.txt': parse_2_sympy_expression(open("./eq4/d_γ_2.txt").readline()),
    'eq4/d_γ_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq4/d_γ_t__d_ψ_t_.txt").readline()),
    'eq4/d_ψ_2.txt': parse_2_sympy_expression(open("./eq4/d_ψ_2.txt").readline()),

    'eq5/d_x_2.txt': parse_2_sympy_expression(open("./eq5/d_x_2.txt").readline()),
    'eq5/d_x_t__d_y_t_.txt': parse_2_sympy_expression(open("./eq5/d_x_t__d_y_t_.txt").readline()),
    'eq5/d_x_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq5/d_x_t__d_α_t_.txt").readline()),
    'eq5/d_x_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq5/d_x_t__d_β_t_.txt").readline()),
    'eq5/d_x_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq5/d_x_t__d_γ_t_.txt").readline()),
    'eq5/d_x_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq5/d_x_t__d_ψ_t_.txt").readline()),
    'eq5/d_y_2.txt': parse_2_sympy_expression(open("./eq5/d_y_2.txt").readline()),
    'eq5/d_y_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq5/d_y_t__d_α_t_.txt").readline()),
    'eq5/d_y_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq5/d_y_t__d_β_t_.txt").readline()),
    'eq5/d_y_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq5/d_y_t__d_γ_t_.txt").readline()),
    'eq5/d_y_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq5/d_y_t__d_ψ_t_.txt").readline()),
    'eq5/d_α_2.txt': parse_2_sympy_expression(open("./eq5/d_α_2.txt").readline()),
    'eq5/d_α_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq5/d_α_t__d_β_t_.txt").readline()),
    'eq5/d_α_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq5/d_α_t__d_γ_t_.txt").readline()),
    'eq5/d_α_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq5/d_α_t__d_ψ_t_.txt").readline()),
    'eq5/d_β_2.txt': parse_2_sympy_expression(open("./eq5/d_β_2.txt").readline()),
    'eq5/d_β_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq5/d_β_t__d_γ_t_.txt").readline()),
    'eq5/d_β_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq5/d_β_t__d_ψ_t_.txt").readline()),
    'eq5/d_γ_2.txt': parse_2_sympy_expression(open("./eq5/d_γ_2.txt").readline()),
    'eq5/d_γ_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq5/d_γ_t__d_ψ_t_.txt").readline()),
    'eq5/d_ψ_2.txt': parse_2_sympy_expression(open("./eq5/d_ψ_2.txt").readline()),

    'eq7/d_x_2.txt': parse_2_sympy_expression(open("./eq7/d_x_2.txt").readline()),
    'eq7/d_x_t__d_y_t_.txt': parse_2_sympy_expression(open("./eq7/d_x_t__d_y_t_.txt").readline()),
    'eq7/d_x_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq7/d_x_t__d_α_t_.txt").readline()),
    'eq7/d_x_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq7/d_x_t__d_β_t_.txt").readline()),
    'eq7/d_x_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq7/d_x_t__d_γ_t_.txt").readline()),
    'eq7/d_x_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq7/d_x_t__d_ψ_t_.txt").readline()),
    'eq7/d_y_2.txt': parse_2_sympy_expression(open("./eq7/d_y_2.txt").readline()),
    'eq7/d_y_t__d_α_t_.txt': parse_2_sympy_expression(open("./eq7/d_y_t__d_α_t_.txt").readline()),
    'eq7/d_y_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq7/d_y_t__d_β_t_.txt").readline()),
    'eq7/d_y_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq7/d_y_t__d_γ_t_.txt").readline()),
    'eq7/d_y_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq7/d_y_t__d_ψ_t_.txt").readline()),
    'eq7/d_α_2.txt': parse_2_sympy_expression(open("./eq7/d_α_2.txt").readline()),
    'eq7/d_α_t__d_β_t_.txt': parse_2_sympy_expression(open("./eq7/d_α_t__d_β_t_.txt").readline()),
    'eq7/d_α_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq7/d_α_t__d_γ_t_.txt").readline()),
    'eq7/d_α_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq7/d_α_t__d_ψ_t_.txt").readline()),
    'eq7/d_β_2.txt': parse_2_sympy_expression(open("./eq7/d_β_2.txt").readline()),
    'eq7/d_β_t__d_γ_t_.txt': parse_2_sympy_expression(open("./eq7/d_β_t__d_γ_t_.txt").readline()),
    'eq7/d_β_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq7/d_β_t__d_ψ_t_.txt").readline()),
    'eq7/d_γ_2.txt': parse_2_sympy_expression(open("./eq7/d_γ_2.txt").readline()),
    'eq7/d_γ_t__d_ψ_t_.txt': parse_2_sympy_expression(open("./eq7/d_γ_t__d_ψ_t_.txt").readline()),
    'eq7/d_ψ_2.txt': parse_2_sympy_expression(open("./eq7/d_ψ_2.txt").readline()),
}

name_2_symb_dict = {
    d_phi_bot: parse_2_sympy_expression(open("../kinematic/part2/d_phi_bottom.txt").readline()),
    d_del_bot: parse_2_sympy_expression(open("../kinematic/part2/d_del_bottom.txt").readline()),
    d_eps_bot: parse_2_sympy_expression(open("../kinematic/part2/d_eps_bottom.txt").readline()),
    d_tau_bot: parse_2_sympy_expression(open("../kinematic/part2/d_tau_bottom.txt").readline())
}

for name, expr in dict_coeff.items():

    top, bot = fraction(expr)
    if bot == 1:
        print("skipped ", name, "\n")
        continue

    top = remove_third_and_above_smallness_from_expression(
        expand(
            top.subs(name_2_symb_dict)
        )
    )

    if top != Zero():
        bot = remove_third_and_above_smallness_from_expression(
            expand(
                bot.subs(name_2_symb_dict)
            )
        )
        print("bot = ", bot)
        top = simplify(top)

        res = top/bot
        with open('./' + name, 'w') as out:
            out.write(transform_to_simpy(str(res)))
    else:
        with open('./' + name, 'w') as out:
            out.write(transform_to_simpy(str(top)))

        print("top of fraction is zero. top =", top)

    print("finish for ", name, "\n")