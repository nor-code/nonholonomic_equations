from sympy import Matrix, expand
from multiprocessing import Process
from definitions.generic_coordinates import *
from definitions.coefficient_for_resolve import *
from utils.common import simplify_determinant, remove_required_and_above_smallness_from_expression_v2, \
    remove_required_and_above_smallness_from_expression
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import transform_to_simpy
import tqdm

main_vars_subs = {
    a1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    a2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    a3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    a4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),

    b1: parse_2_sympy_expression(open(
         "../../collect_parallel/eq8/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    b2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    b3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    b4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq8/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),

    c1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    c2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    c3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    c4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),

    d1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    d2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    d3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_α_t__2__.txt").readline()).coeff(diff(diff(x1, t), t)),
    d4: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_δ_t__2__.txt").readline()).coeff(diff(diff(x6, t), t)),
}

print("___READED ALL COEFFICIENT___")

m11 = -b4*c3*d2 + b3*c4*d2 + b4*c2*d3 - b2*c4*d3 - b3*c2*d4 + b2*c3*d4

m12 = a4*c3*d2 - a3*c4*d2 - a4*c2*d3 + a2*c4*d3 + a3*c2*d4 - a2*c3*d4

m13 = -a4*b3*d2 + a3*b4*d2 + a4*b2*d3 - a2*b4*d3 - a3*b2*d4 + a2*b3*d4

m14 = a4*b3*c2 - a3*b4*c2 - a4*b2*c3 + a2*b4*c3 + a3*b2*c4 - a2*b3*c4

m21 = b4*c3*d1 - b3*c4*d1 - b4*c1*d3 + b1*c4*d3 + b3*c1*d4 - b1*c3*d4

m22 = -a4*c3*d1 + a3*c4*d1 + a4*c1*d3 - a1*c4*d3 - a3*c1*d4 + a1*c3*d4

m23 = a4*b3*d1 - a3*b4*d1 - a4*b1*d3 + a1*b4*d3 + a3*b1*d4 - a1*b3*d4

m24 = -a4*b3*c1 + a3*b4*c1 + a4*b1*c3 - a1*b4*c3 - a3*b1*c4 + a1*b3*c4

m31 = -b4*c2*d1 + b2*c4*d1 + b4*c1*d2 - b1*c4*d2 - b2*c1*d4 + b1*c2*d4

m32 = a4*c2*d1 - a2*c4*d1 - a4*c1*d2 + a1*c4*d2 + a2*c1*d4 - a1*c2*d4

m33 = -a4*b2*d1 + a2*b4*d1 + a4*b1*d2 - a1*b4*d2 - a2*b1*d4 + a1*b2*d4

m34 = a4*b2*c1 - a2*b4*c1 - a4*b1*c2 + a1*b4*c2 + a2*b1*c4 - a1*b2*c4

m41 = b3*c2*d1 - b2*c3*d1 - b3*c1*d2 + b1*c3*d2 + b2*c1*d3 - b1*c2*d3

m42 = -a3*c2*d1 + a2*c3*d1 + a3*c1*d2 - a1*c3*d2 - a2*c1*d3 + a1*c2*d3

m43 = a3*b2*d1 - a2*b3*d1 - a3*b1*d2 + a1*b3*d2 + a2*b1*d3 - a1*b2*d3

m44 = -a3*b2*c1 + a2*b3*c1 + a3*b1*c2 - a1*b3*c2 - a2*b1*c3 + a1*b2*c3

det = a4*b3*c2*d1 - a3*b4*c2*d1 - a4*b2*c3*d1 + a2*b4*c3*d1 + a3*b2*c4*d1 - a2*b3*c4*d1 - a4*b3*c1*d2 + a3*b4*c1*d2 \
      + a4*b1*c3*d2 - a1*b4*c3*d2 - a3*b1*c4*d2 + a1*b3*c4*d2 + a4*b2*c1*d3 - a2*b4*c1*d3 - a4*b1*c2*d3 + a1*b4*c2*d3 \
      + a2*b1*c4*d3 - a1*b2*c4*d3 - a3*b2*c1*d4 + a2*b3*c1*d4 + a3*b1*c2*d4 - a1*b3*c2*d4 - a2*b1*c3*d4 + a1*b2*c3*d4


def simplify_and_expand_component(name, component, dict_var):
    result = 0
    for term in tqdm.tqdm(component.args):
        s = 1
        index = 0
        total = len(term.args)
        while index < total:
            s = s * term.args[index]
            s = s.subs(dict_var)
            s = remove_required_and_above_smallness_from_expression_v2(expand(s), order=2)
            index += 1

        result = result + s

    # result = simplify_determinant(result)
    with open('component_' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
for name, component in dict(
        zip(['m11', 'm12', 'm13', 'm14', 'm21', 'm22', 'm23', 'm24', 'm31', 'm32', 'm33', 'm34', 'm41', 'm42', 'm43', 'm44', 'det'],
            [m11, m12, m13, m14, m21, m22, m23, m24, m31, m32, m33, m34, m41, m42, m43, m44, det])).items():
    task = Process(
        target=simplify_and_expand_component,
        args=(name, component, main_vars_subs)
    )
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()