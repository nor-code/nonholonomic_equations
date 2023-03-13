from sympy import Matrix, expand, simplify
from multiprocessing import Process
from definitions.generic_coordinates import *
from definitions.coefficient_for_resolve import *
from utils.common import remove_required_and_above_smallness_from_expression, simplify_determinant
from utils.sympy_expression import parse_2_sympy_expression
from utils.to_sympy_expression import transform_to_simpy
import tqdm

main_vars_subs = {
    a1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    a2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    a3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq6/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t)),

    b1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    b2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    b3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq9/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t)),

    c1: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_x_t__2__.txt").readline()).coeff(diff(diff(x, t), t)),
    c2: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_y_t__2__.txt").readline()).coeff(diff(diff(y, t), t)),
    c3: parse_2_sympy_expression(open(
        "../../collect_parallel/eq10/d_d_β_t__2__.txt").readline()).coeff(diff(diff(x2, t), t))
}

print("___READED ALL COEFFICIENT___")

m11 = b2*c3 - b3*c2

m12 = -a2*c3 + a3*c2

m13 = a2*b3 - a3*b2

m21 = -b1*c3 + b3*c1

m22 = a1*c3 - a3*c1

m23 = -a1*b3 + a3*b1

m31 = b1*c2 - b2*c1

m32 = -a1*c2 + a2*c1

m33 = a1*b2 - a2*b1


det = a1*b2*c3 - a1*b3*c2 - a2*b1*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1


def simplify_and_expand_component(name, component, dict_var):
    result = 0
    for term in tqdm.tqdm(component.args):
        s = 1
        index = 0
        total = len(term.args)
        while index < total:
            s = s * term.args[index]
            s = s.subs(dict_var)
            s = remove_required_and_above_smallness_from_expression(expand(s), order=2)
            index += 1

        result = result + s

    result = simplify_determinant(result)
    with open('component_' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
for name, component in dict(
        zip(['m11', 'm12', 'm13', 'm21', 'm22', 'm23', 'm31', 'm32', 'm33', 'det'],
            [m11, m12, m13, m21, m22, m23, m31, m32, m33, det])).items():
    task = Process(
        target=simplify_and_expand_component,
        args=(name, component, main_vars_subs)
    )
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()