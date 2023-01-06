from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import argparse
import json
import tqdm
from Subs_kinematic import *

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int)

args = parser.parse_args()

dictionary_file = {
    7: 'out7.json'
}

raw = open(dictionary_file[args.n])
dict_eq = json.load(raw)
transformations = (standard_transformations + (implicit_multiplication_application,))
local_dictionary = {'x': x, 'y': y, 'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5, 'x6': x6, 'x7': x7, 'x8': x8}

dict_equation = {}
for k, v in tqdm.tqdm(dict_eq.items()):
    key = transform_to_simpy(k)
    key = parse_expr(key, transformations=transformations, local_dict=local_dictionary)
    value = parse_expr(v, transformations=transformations, local_dict=local_dictionary)
    dict_equation[key] = value

final_independent_coordinates = [x, y, x1, x2, x3, x5]
second_derivatives = [diff(diff(var, t), t) for var in final_independent_coordinates]
mixed_derivatives = list(mixed[0] * mixed[1] for mixed in itertools.combinations([diff(var, t) for var in final_independent_coordinates], 2))
[mixed_derivatives.append(diff(var, t) * diff(var, t)) for var in final_independent_coordinates]

m11, m12, m13, m14, m15, m16, m21, m22, m23, m24, m25, m26, m31, m32, m33,\
    m34, m35, m36, m41, m42, m43, m44, m45, m46, m51, m52, m53, m54, m55, m56, m61, m62, m63, m64, m65, m66\
    = symbols('m11, m12, m13, m14, m15, m16, m21, m22, m23, m24, m25, m26, m31, m32, m33,'
              ' m34, m35, m36, m41, m42, m43, m44, m45, m46, m51, m52, m53, m54, m55, m56, m61, m62, m63, m64, m65, m66')
A = Matrix([
    [m11, m12, m13, m14, m15, m16],
    [m21, m22, m23, m24, m25, m26],
    [m31, m32, m33, m34, m35, m36],
    [m41, m42, m43, m44, m45, m46],
    [m51, m52, m53, m54, m55, m56],
    [m61, m62, m63, m64, m65, m66]
])
for dd_var in second_derivatives:
    if dict_equation[dd_var] == 0:
        A = A.subs(m61, 0)

A = A.inv()
print(A)