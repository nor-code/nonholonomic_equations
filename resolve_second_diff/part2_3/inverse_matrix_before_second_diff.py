import time
from multiprocessing import Process

from sympy import Matrix, expand
from definitions.coefficient_for_resolve import *
from definitions.constants import C_My, C_Mx
from utils.common import remove_third_and_above_smallness_from_expression, \
    remove_required_and_above_smallness_from_expression, simplify_determinant
from utils.to_sympy_expression import replace_space_to_multiplication_sym, transform_to_simpy
import tqdm
from coefficient_dict import main_vars_subs

"""
случай когда все углы малы , кроме $\beta$ & $\epsilon$
"""
m11 = b5 * c4 * d3 * e2 - b4 * c5 * d3 * e2 - b5 * c3 * d4 * e2 + b3 * c5 * d4 * e2 + b4 * c3 * d5 * e2 - b3 * c4 * d5 * e2 - b5 * c4 * d2 * e3 + b4 * c5 * d2 * e3 + b5 * c2 * d4 * e3 - b2 * c5 * d4 * e3 - b4 * c2 * d5 * e3 + b2 * c4 * d5 * e3 + b5 * c3 * d2 * e4 - b3 * c5 * d2 * e4 \
      - b5 * c2 * d3 * e4 + b2 * c5 * d3 * e4 + b3 * c2 * d5 * e4 - b2 * c3 * d5 * e4 - b4 * c3 * d2 * e5 + b3 * c4 * d2 * e5 + b4 * c2 * d3 * e5 - b2 * c4 * d3 * e5 - b3 * c2 * d4 * e5 + b2 * c3 * d4 * e5

m12 = -a5 * c4 * d3 * e2 + a4 * c5 * d3 * e2 + a5 * c3 * d4 * e2 - a3 * c5 * d4 * e2 - a4 * c3 * d5 * e2 + a3 * c4 * d5 * e2 + a5 * c4 * d2 * e3 - a4 * c5 * d2 * e3 - a5 * c2 * d4 * e3 + a2 * c5 * d4 * e3 + a4 * c2 * d5 * e3 - a2 * c4 * d5 * e3 - a5 * c3 * d2 * e4 + a3 * c5 * d2 * e4 \
      + a5 * c2 * d3 * e4 - a2 * c5 * d3 * e4 - a3 * c2 * d5 * e4 + a2 * c3 * d5 * e4 + a4 * c3 * d2 * e5 - a3 * c4 * d2 * e5 - a4 * c2 * d3 * e5 + a2 * c4 * d3 * e5 + a3 * c2 * d4 * e5 - a2 * c3 * d4 * e5

m13 = a5 * b4 * d3 * e2 - a4 * b5 * d3 * e2 - a5 * b3 * d4 * e2 + a3 * b5 * d4 * e2 + a4 * b3 * d5 * e2 - a3 * b4 * d5 * e2 - a5 * b4 * d2 * e3 + a4 * b5 * d2 * e3 + a5 * b2 * d4 * e3 - a2 * b5 * d4 * e3 - a4 * b2 * d5 * e3 + a2 * b4 * d5 * e3 + a5 * b3 * d2 * e4 - a3 * b5 * d2 * e4 \
      - a5 * b2 * d3 * e4 + a2 * b5 * d3 * e4 + a3 * b2 * d5 * e4 - a2 * b3 * d5 * e4 - a4 * b3 * d2 * e5 + a3 * b4 * d2 * e5 + a4 * b2 * d3 * e5 - a2 * b4 * d3 * e5 - a3 * b2 * d4 * e5 + a2 * b3 * d4 * e5

m14 = -a5 * b4 * c3 * e2 + a4 * b5 * c3 * e2 + a5 * b3 * c4 * e2 - a3 * b5 * c4 * e2 - a4 * b3 * c5 * e2 + a3 * b4 * c5 * e2 + a5 * b4 * c2 * e3 - a4 * b5 * c2 * e3 - a5 * b2 * c4 * e3 + a2 * b5 * c4 * e3 + a4 * b2 * c5 * e3 - a2 * b4 * c5 * e3 - a5 * b3 * c2 * e4 + a3 * b5 * c2 * e4 \
      + a5 * b2 * c3 * e4 - a2 * b5 * c3 * e4 - a3 * b2 * c5 * e4 + a2 * b3 * c5 * e4 + a4 * b3 * c2 * e5 - a3 * b4 * c2 * e5 - a4 * b2 * c3 * e5 + a2 * b4 * c3 * e5 + a3 * b2 * c4 * e5 - a2 * b3 * c4 * e5

m15 = a5 * b4 * c3 * d2 - a4 * b5 * c3 * d2 - a5 * b3 * c4 * d2 + a3 * b5 * c4 * d2 + a4 * b3 * c5 * d2 - a3 * b4 * c5 * d2 - a5 * b4 * c2 * d3 + a4 * b5 * c2 * d3 + a5 * b2 * c4 * d3 - a2 * b5 * c4 * d3 - a4 * b2 * c5 * d3 + a2 * b4 * c5 * d3 + a5 * b3 * c2 * d4 - a3 * b5 * c2 * d4 \
      - a5 * b2 * c3 * d4 + a2 * b5 * c3 * d4 + a3 * b2 * c5 * d4 - a2 * b3 * c5 * d4 - a4 * b3 * c2 * d5 + a3 * b4 * c2 * d5 + a4 * b2 * c3 * d5 - a2 * b4 * c3 * d5 - a3 * b2 * c4 * d5 + a2 * b3 * c4 * d5

m21 = -b5 * c4 * d3 * e1 + b4 * c5 * d3 * e1 + b5 * c3 * d4 * e1 - b3 * c5 * d4 * e1 - b4 * c3 * d5 * e1 + b3 * c4 * d5 * e1 + b5 * c4 * d1 * e3 - b4 * c5 * d1 * e3 - b5 * c1 * d4 * e3 + b1 * c5 * d4 * e3 + b4 * c1 * d5 * e3 - b1 * c4 * d5 * e3 - b5 * c3 * d1 * e4 + b3 * c5 * d1 * e4 \
      + b5 * c1 * d3 * e4 - b1 * c5 * d3 * e4 - b3 * c1 * d5 * e4 + b1 * c3 * d5 * e4 + b4 * c3 * d1 * e5 - b3 * c4 * d1 * e5 - b4 * c1 * d3 * e5 + b1 * c4 * d3 * e5 + b3 * c1 * d4 * e5 - b1 * c3 * d4 * e5

m22 = a5 * c4 * d3 * e1 - a4 * c5 * d3 * e1 - a5 * c3 * d4 * e1 + a3 * c5 * d4 * e1 + a4 * c3 * d5 * e1 - a3 * c4 * d5 * e1 - a5 * c4 * d1 * e3 + a4 * c5 * d1 * e3 + a5 * c1 * d4 * e3 - a1 * c5 * d4 * e3 - a4 * c1 * d5 * e3 + a1 * c4 * d5 * e3 + a5 * c3 * d1 * e4 - a3 * c5 * d1 * e4 \
      - a5 * c1 * d3 * e4 + a1 * c5 * d3 * e4 + a3 * c1 * d5 * e4 - a1 * c3 * d5 * e4 - a4 * c3 * d1 * e5 + a3 * c4 * d1 * e5 + a4 * c1 * d3 * e5 - a1 * c4 * d3 * e5 - a3 * c1 * d4 * e5 + a1 * c3 * d4 * e5

m23 = -a5 * b4 * d3 * e1 + a4 * b5 * d3 * e1 + a5 * b3 * d4 * e1 - a3 * b5 * d4 * e1 - a4 * b3 * d5 * e1 + a3 * b4 * d5 * e1 + a5 * b4 * d1 * e3 - a4 * b5 * d1 * e3 - a5 * b1 * d4 * e3 + a1 * b5 * d4 * e3 + a4 * b1 * d5 * e3 - a1 * b4 * d5 * e3 - a5 * b3 * d1 * e4 + a3 * b5 * d1 * e4 \
      + a5 * b1 * d3 * e4 - a1 * b5 * d3 * e4 - a3 * b1 * d5 * e4 + a1 * b3 * d5 * e4 + a4 * b3 * d1 * e5 - a3 * b4 * d1 * e5 - a4 * b1 * d3 * e5 + a1 * b4 * d3 * e5 + a3 * b1 * d4 * e5 - a1 * b3 * d4 * e5

m24 = a5 * b4 * c3 * e1 - a4 * b5 * c3 * e1 - a5 * b3 * c4 * e1 + a3 * b5 * c4 * e1 + a4 * b3 * c5 * e1 - a3 * b4 * c5 * e1 - a5 * b4 * c1 * e3 + a4 * b5 * c1 * e3 + a5 * b1 * c4 * e3 - a1 * b5 * c4 * e3 - a4 * b1 * c5 * e3 + a1 * b4 * c5 * e3 + a5 * b3 * c1 * e4 - a3 * b5 * c1 * e4 \
      - a5 * b1 * c3 * e4 + a1 * b5 * c3 * e4 + a3 * b1 * c5 * e4 - a1 * b3 * c5 * e4 - a4 * b3 * c1 * e5 + a3 * b4 * c1 * e5 + a4 * b1 * c3 * e5 - a1 * b4 * c3 * e5 - a3 * b1 * c4 * e5 + a1 * b3 * c4 * e5

m25 = -a5 * b4 * c3 * d1 + a4 * b5 * c3 * d1 + a5 * b3 * c4 * d1 - a3 * b5 * c4 * d1 - a4 * b3 * c5 * d1 + a3 * b4 * c5 * d1 + a5 * b4 * c1 * d3 - a4 * b5 * c1 * d3 - a5 * b1 * c4 * d3 + a1 * b5 * c4 * d3 + a4 * b1 * c5 * d3 - a1 * b4 * c5 * d3 - a5 * b3 * c1 * d4 + a3 * b5 * c1 * d4 \
      + a5 * b1 * c3 * d4 - a1 * b5 * c3 * d4 - a3 * b1 * c5 * d4 + a1 * b3 * c5 * d4 + a4 * b3 * c1 * d5 - a3 * b4 * c1 * d5 - a4 * b1 * c3 * d5 + a1 * b4 * c3 * d5 + a3 * b1 * c4 * d5 - a1 * b3 * c4 * d5

m31 = b5 * c4 * d2 * e1 - b4 * c5 * d2 * e1 - b5 * c2 * d4 * e1 + b2 * c5 * d4 * e1 + b4 * c2 * d5 * e1 - b2 * c4 * d5 * e1 - b5 * c4 * d1 * e2 + b4 * c5 * d1 * e2 + b5 * c1 * d4 * e2 - b1 * c5 * d4 * e2 - b4 * c1 * d5 * e2 + b1 * c4 * d5 * e2 + b5 * c2 * d1 * e4 - b2 * c5 * d1 * e4 \
      - b5 * c1 * d2 * e4 + b1 * c5 * d2 * e4 + b2 * c1 * d5 * e4 - b1 * c2 * d5 * e4 - b4 * c2 * d1 * e5 + b2 * c4 * d1 * e5 + b4 * c1 * d2 * e5 - b1 * c4 * d2 * e5 - b2 * c1 * d4 * e5 + b1 * c2 * d4 * e5

m32 = -a5 * c4 * d2 * e1 + a4 * c5 * d2 * e1 + a5 * c2 * d4 * e1 - a2 * c5 * d4 * e1 - a4 * c2 * d5 * e1 + a2 * c4 * d5 * e1 + a5 * c4 * d1 * e2 - a4 * c5 * d1 * e2 - a5 * c1 * d4 * e2 + a1 * c5 * d4 * e2 + a4 * c1 * d5 * e2 - a1 * c4 * d5 * e2 - a5 * c2 * d1 * e4 + a2 * c5 * d1 * e4 \
      + a5 * c1 * d2 * e4 - a1 * c5 * d2 * e4 - a2 * c1 * d5 * e4 + a1 * c2 * d5 * e4 + a4 * c2 * d1 * e5 - a2 * c4 * d1 * e5 - a4 * c1 * d2 * e5 + a1 * c4 * d2 * e5 + a2 * c1 * d4 * e5 - a1 * c2 * d4 * e5

m33 = a5 * b4 * d2 * e1 - a4 * b5 * d2 * e1 - a5 * b2 * d4 * e1 + a2 * b5 * d4 * e1 + a4 * b2 * d5 * e1 - a2 * b4 * d5 * e1 - a5 * b4 * d1 * e2 + a4 * b5 * d1 * e2 + a5 * b1 * d4 * e2 - a1 * b5 * d4 * e2 - a4 * b1 * d5 * e2 + a1 * b4 * d5 * e2 + a5 * b2 * d1 * e4 - a2 * b5 * d1 * e4 \
      - a5 * b1 * d2 * e4 + a1 * b5 * d2 * e4 + a2 * b1 * d5 * e4 - a1 * b2 * d5 * e4 - a4 * b2 * d1 * e5 + a2 * b4 * d1 * e5 + a4 * b1 * d2 * e5 - a1 * b4 * d2 * e5 - a2 * b1 * d4 * e5 + a1 * b2 * d4 * e5

m34 = -a5 * b4 * c2 * e1 + a4 * b5 * c2 * e1 + a5 * b2 * c4 * e1 - a2 * b5 * c4 * e1 - a4 * b2 * c5 * e1 + a2 * b4 * c5 * e1 + a5 * b4 * c1 * e2 - a4 * b5 * c1 * e2 - a5 * b1 * c4 * e2 + a1 * b5 * c4 * e2 + a4 * b1 * c5 * e2 - a1 * b4 * c5 * e2 - a5 * b2 * c1 * e4 + a2 * b5 * c1 * e4 \
      + a5 * b1 * c2 * e4 - a1 * b5 * c2 * e4 - a2 * b1 * c5 * e4 + a1 * b2 * c5 * e4 + a4 * b2 * c1 * e5 - a2 * b4 * c1 * e5 - a4 * b1 * c2 * e5 + a1 * b4 * c2 * e5 + a2 * b1 * c4 * e5 - a1 * b2 * c4 * e5

m35 = a5 * b4 * c2 * d1 - a4 * b5 * c2 * d1 - a5 * b2 * c4 * d1 + a2 * b5 * c4 * d1 + a4 * b2 * c5 * d1 - a2 * b4 * c5 * d1 - a5 * b4 * c1 * d2 + a4 * b5 * c1 * d2 + a5 * b1 * c4 * d2 - a1 * b5 * c4 * d2 - a4 * b1 * c5 * d2 + a1 * b4 * c5 * d2 + a5 * b2 * c1 * d4 - a2 * b5 * c1 * d4 \
      - a5 * b1 * c2 * d4 + a1 * b5 * c2 * d4 + a2 * b1 * c5 * d4 - a1 * b2 * c5 * d4 - a4 * b2 * c1 * d5 + a2 * b4 * c1 * d5 + a4 * b1 * c2 * d5 - a1 * b4 * c2 * d5 - a2 * b1 * c4 * d5 + a1 * b2 * c4 * d5

m41 = -b5 * c3 * d2 * e1 + b3 * c5 * d2 * e1 + b5 * c2 * d3 * e1 - b2 * c5 * d3 * e1 - b3 * c2 * d5 * e1 + b2 * c3 * d5 * e1 + b5 * c3 * d1 * e2 - b3 * c5 * d1 * e2 - b5 * c1 * d3 * e2 + b1 * c5 * d3 * e2 + b3 * c1 * d5 * e2 - b1 * c3 * d5 * e2 - b5 * c2 * d1 * e3 + b2 * c5 * d1 * e3 \
      + b5 * c1 * d2 * e3 - b1 * c5 * d2 * e3 - b2 * c1 * d5 * e3 + b1 * c2 * d5 * e3 + b3 * c2 * d1 * e5 - b2 * c3 * d1 * e5 - b3 * c1 * d2 * e5 + b1 * c3 * d2 * e5 + b2 * c1 * d3 * e5 - b1 * c2 * d3 * e5

m42 = a5 * c3 * d2 * e1 - a3 * c5 * d2 * e1 - a5 * c2 * d3 * e1 + a2 * c5 * d3 * e1 + a3 * c2 * d5 * e1 - a2 * c3 * d5 * e1 - a5 * c3 * d1 * e2 + a3 * c5 * d1 * e2 + a5 * c1 * d3 * e2 - a1 * c5 * d3 * e2 - a3 * c1 * d5 * e2 + a1 * c3 * d5 * e2 + a5 * c2 * d1 * e3 - a2 * c5 * d1 * e3 \
      - a5 * c1 * d2 * e3 + a1 * c5 * d2 * e3 + a2 * c1 * d5 * e3 - a1 * c2 * d5 * e3 - a3 * c2 * d1 * e5 + a2 * c3 * d1 * e5 + a3 * c1 * d2 * e5 - a1 * c3 * d2 * e5 - a2 * c1 * d3 * e5 + a1 * c2 * d3 * e5

m43 = -a5 * b3 * d2 * e1 + a3 * b5 * d2 * e1 + a5 * b2 * d3 * e1 - a2 * b5 * d3 * e1 - a3 * b2 * d5 * e1 + a2 * b3 * d5 * e1 + a5 * b3 * d1 * e2 - a3 * b5 * d1 * e2 - a5 * b1 * d3 * e2 + a1 * b5 * d3 * e2 + a3 * b1 * d5 * e2 - a1 * b3 * d5 * e2 - a5 * b2 * d1 * e3 + a2 * b5 * d1 * e3 \
      + a5 * b1 * d2 * e3 - a1 * b5 * d2 * e3 - a2 * b1 * d5 * e3 + a1 * b2 * d5 * e3 + a3 * b2 * d1 * e5 - a2 * b3 * d1 * e5 - a3 * b1 * d2 * e5 + a1 * b3 * d2 * e5 + a2 * b1 * d3 * e5 - a1 * b2 * d3 * e5

m44 = a5 * b3 * c2 * e1 - a3 * b5 * c2 * e1 - a5 * b2 * c3 * e1 + a2 * b5 * c3 * e1 + a3 * b2 * c5 * e1 - a2 * b3 * c5 * e1 - a5 * b3 * c1 * e2 + a3 * b5 * c1 * e2 + a5 * b1 * c3 * e2 - a1 * b5 * c3 * e2 - a3 * b1 * c5 * e2 + a1 * b3 * c5 * e2 + a5 * b2 * c1 * e3 - a2 * b5 * c1 * e3 \
      - a5 * b1 * c2 * e3 + a1 * b5 * c2 * e3 + a2 * b1 * c5 * e3 - a1 * b2 * c5 * e3 - a3 * b2 * c1 * e5 + a2 * b3 * c1 * e5 + a3 * b1 * c2 * e5 - a1 * b3 * c2 * e5 - a2 * b1 * c3 * e5 + a1 * b2 * c3 * e5

m45 = -a5 * b3 * c2 * d1 + a3 * b5 * c2 * d1 + a5 * b2 * c3 * d1 - a2 * b5 * c3 * d1 - a3 * b2 * c5 * d1 + a2 * b3 * c5 * d1 + a5 * b3 * c1 * d2 - a3 * b5 * c1 * d2 - a5 * b1 * c3 * d2 + a1 * b5 * c3 * d2 + a3 * b1 * c5 * d2 - a1 * b3 * c5 * d2 - a5 * b2 * c1 * d3 + a2 * b5 * c1 * d3 \
      + a5 * b1 * c2 * d3 - a1 * b5 * c2 * d3 - a2 * b1 * c5 * d3 + a1 * b2 * c5 * d3 + a3 * b2 * c1 * d5 - a2 * b3 * c1 * d5 - a3 * b1 * c2 * d5 + a1 * b3 * c2 * d5 + a2 * b1 * c3 * d5 - a1 * b2 * c3 * d5

m51 = b4 * c3 * d2 * e1 - b3 * c4 * d2 * e1 - b4 * c2 * d3 * e1 + b2 * c4 * d3 * e1 + b3 * c2 * d4 * e1 - b2 * c3 * d4 * e1 - b4 * c3 * d1 * e2 + b3 * c4 * d1 * e2 + b4 * c1 * d3 * e2 - b1 * c4 * d3 * e2 - b3 * c1 * d4 * e2 + b1 * c3 * d4 * e2 + b4 * c2 * d1 * e3 - b2 * c4 * d1 * e3 \
      - b4 * c1 * d2 * e3 + b1 * c4 * d2 * e3 + b2 * c1 * d4 * e3 - b1 * c2 * d4 * e3 - b3 * c2 * d1 * e4 + b2 * c3 * d1 * e4 + b3 * c1 * d2 * e4 - b1 * c3 * d2 * e4 - b2 * c1 * d3 * e4 + b1 * c2 * d3 * e4

m52 = -a4 * c3 * d2 * e1 + a3 * c4 * d2 * e1 + a4 * c2 * d3 * e1 - a2 * c4 * d3 * e1 - a3 * c2 * d4 * e1 + a2 * c3 * d4 * e1 + a4 * c3 * d1 * e2 - a3 * c4 * d1 * e2 - a4 * c1 * d3 * e2 + a1 * c4 * d3 * e2 + a3 * c1 * d4 * e2 - a1 * c3 * d4 * e2 - a4 * c2 * d1 * e3 + a2 * c4 * d1 * e3 \
      + a4 * c1 * d2 * e3 - a1 * c4 * d2 * e3 - a2 * c1 * d4 * e3 + a1 * c2 * d4 * e3 + a3 * c2 * d1 * e4 - a2 * c3 * d1 * e4 - a3 * c1 * d2 * e4 + a1 * c3 * d2 * e4 + a2 * c1 * d3 * e4 - a1 * c2 * d3 * e4

m53 = a4 * b3 * d2 * e1 - a3 * b4 * d2 * e1 - a4 * b2 * d3 * e1 + a2 * b4 * d3 * e1 + a3 * b2 * d4 * e1 - a2 * b3 * d4 * e1 - a4 * b3 * d1 * e2 + a3 * b4 * d1 * e2 + a4 * b1 * d3 * e2 - a1 * b4 * d3 * e2 - a3 * b1 * d4 * e2 + a1 * b3 * d4 * e2 + a4 * b2 * d1 * e3 - a2 * b4 * d1 * e3 \
      - a4 * b1 * d2 * e3 + a1 * b4 * d2 * e3 + a2 * b1 * d4 * e3 - a1 * b2 * d4 * e3 - a3 * b2 * d1 * e4 + a2 * b3 * d1 * e4 + a3 * b1 * d2 * e4 - a1 * b3 * d2 * e4 - a2 * b1 * d3 * e4 + a1 * b2 * d3 * e4

m54 = -a4 * b3 * c2 * e1 + a3 * b4 * c2 * e1 + a4 * b2 * c3 * e1 - a2 * b4 * c3 * e1 - a3 * b2 * c4 * e1 + a2 * b3 * c4 * e1 + a4 * b3 * c1 * e2 - a3 * b4 * c1 * e2 - a4 * b1 * c3 * e2 + a1 * b4 * c3 * e2 + a3 * b1 * c4 * e2 - a1 * b3 * c4 * e2 - a4 * b2 * c1 * e3 + a2 * b4 * c1 * e3 \
      + a4 * b1 * c2 * e3 - a1 * b4 * c2 * e3 - a2 * b1 * c4 * e3 + a1 * b2 * c4 * e3 + a3 * b2 * c1 * e4 - a2 * b3 * c1 * e4 - a3 * b1 * c2 * e4 + a1 * b3 * c2 * e4 + a2 * b1 * c3 * e4 - a1 * b2 * c3 * e4

m55 = a4 * b3 * c2 * d1 - a3 * b4 * c2 * d1 - a4 * b2 * c3 * d1 + a2 * b4 * c3 * d1 + a3 * b2 * c4 * d1 - a2 * b3 * c4 * d1 - a4 * b3 * c1 * d2 + a3 * b4 * c1 * d2 + a4 * b1 * c3 * d2 - a1 * b4 * c3 * d2 - a3 * b1 * c4 * d2 + a1 * b3 * c4 * d2 + a4 * b2 * c1 * d3 - a2 * b4 * c1 * d3 \
      - a4 * b1 * c2 * d3 + a1 * b4 * c2 * d3 + a2 * b1 * c4 * d3 - a1 * b2 * c4 * d3 - a3 * b2 * c1 * d4 + a2 * b3 * c1 * d4 + a3 * b1 * c2 * d4 - a1 * b3 * c2 * d4 - a2 * b1 * c3 * d4 + a1 * b2 * c3 * d4

det = a5 * b4 * c3 * d2 * e1 - a4 * b5 * c3 * d2 * e1 - a5 * b3 * c4 * d2 * e1 + a3 * b5 * c4 * d2 * e1 + a4 * b3 * c5 * d2 * e1 - a3 * b4 * c5 * d2 * e1 - a5 * b4 * c2 * d3 * e1 + a4 * b5 * c2 * d3 * e1 + a5 * b2 * c4 * d3 * e1 - a2 * b5 * c4 * d3 * e1 - a4 * b2 * c5 * d3 * e1 + a2 * b4 * c5 * d3 * e1 \
      + a5 * b3 * c2 * d4 * e1 - a3 * b5 * c2 * d4 * e1 - a5 * b2 * c3 * d4 * e1 + a2 * b5 * c3 * d4 * e1 + a3 * b2 * c5 * d4 * e1 - a2 * b3 * c5 * d4 * e1 - a4 * b3 * c2 * d5 * e1 + a3 * b4 * c2 * d5 * e1 + a4 * b2 * c3 * d5 * e1 - a2 * b4 * c3 * d5 * e1 - a3 * b2 * c4 * d5 * e1 + a2 * b3 * c4 * d5 * e1 \
      - a5 * b4 * c3 * d1 * e2 + a4 * b5 * c3 * d1 * e2 + a5 * b3 * c4 * d1 * e2 - a3 * b5 * c4 * d1 * e2 - a4 * b3 * c5 * d1 * e2 + a3 * b4 * c5 * d1 * e2 + a5 * b4 * c1 * d3 * e2 - a4 * b5 * c1 * d3 * e2 - a5 * b1 * c4 * d3 * e2 + a1 * b5 * c4 * d3 * e2 + a4 * b1 * c5 * d3 * e2 - a1 * b4 *c5 * d3 * e2 \
      - a5 * b3 * c1 * d4 * e2 + a3 * b5 * c1 * d4 * e2 + a5 * b1 * c3 * d4 * e2 - a1 * b5 * c3 * d4 * e2 - a3 * b1 * c5 * d4 * e2 + a1 * b3 * c5 * d4 * e2 + a4 * b3 * c1 * d5 * e2 - a3 * b4 * c1 * d5 * e2 - a4 * b1 * c3 * d5 * e2 + a1 * b4 * c3 * d5 * e2 + a3 * b1 * c4 * d5 * e2 - a1 * b3 * c4 * d5 * e2 \
      + a5 * b4 * c2 * d1 * e3 - a4 * b5 * c2 * d1 * e3 - a5 * b2 * c4 * d1 * e3 + a2 * b5 * c4 * d1 * e3 + a4 * b2 * c5 * d1 * e3 - a2 * b4 * c5 * d1 * e3 - a5 * b4 * c1 * d2 * e3 + a4 * b5 * c1 * d2 * e3 + a5 * b1 * c4 * d2 * e3 - a1 * b5 * c4 * d2 * e3 - a4 * b1 * c5 * d2 * e3 + a1 * b4 * c5 * d2 * e3 \
      + a5 * b2 * c1 * d4 * e3 - a2 * b5 * c1 * d4 * e3 - a5 * b1 * c2 * d4 * e3 + a1 * b5 * c2 * d4 * e3 + a2 * b1 * c5 * d4 * e3 - a1 * b2 * c5 * d4 * e3 - a4 * b2 * c1 * d5 * e3 + a2 * b4 * c1 * d5 * e3 + a4 * b1 * c2 * d5 * e3 - a1 * b4 * c2 * d5 * e3 - a2 * b1 * c4 * d5 * e3 + a1 * b2 * c4 * d5 * e3 \
      - a5 * b3 * c2 * d1 * e4 + a3 * b5 * c2 * d1 * e4 + a5 * b2 * c3 * d1 * e4 - a2 * b5 * c3 * d1 * e4 - a3 * b2 * c5 * d1 * e4 + a2 * b3 * c5 * d1 * e4 + a5 * b3 * c1 * d2 * e4 - a3 * b5 * c1 * d2 * e4 - a5 * b1 * c3 * d2 * e4 + a1 * b5 * c3 * d2 * e4 + a3 * b1 * c5 * d2 * e4 - a1 * b3 * c5 * d2 * e4 \
      - a5 * b2 * c1 * d3 * e4 + a2 * b5 * c1 * d3 * e4 + a5 * b1 * c2 * d3 * e4 - a1 * b5 * c2 * d3 * e4 - a2 * b1 * c5 * d3 * e4 + a1 * b2 * c5 * d3 * e4 + a3 * b2 * c1 * d5 * e4 - a2 * b3 * c1 * d5 * e4 - a3 * b1 * c2 * d5 * e4 + a1 * b3 * c2 * d5 * e4 + a2 * b1 * c3 * d5 * e4 - a1 * b2 * c3 * d5 * e4 \
      + a4 * b3 * c2 * d1 * e5 - a3 * b4 * c2 * d1 * e5 - a4 * b2 * c3 * d1 * e5 + a2 * b4 * c3 * d1 * e5 + a3 * b2 * c4 * d1 * e5 - a2 * b3 * c4 * d1 * e5 - a4 * b3 * c1 * d2 * e5 + a3 * b4 * c1 * d2 * e5 + a4 * b1 * c3 * d2 * e5 - a1 * b4 * c3 * d2 * e5 - a3 * b1 * c4 * d2 * e5 + a1 * b3 * c4 * d2 * e5 \
      + a4 * b2 * c1 * d3 * e5 - a2 * b4 * c1 * d3 * e5 - a4 * b1 * c2 * d3 * e5 + a1 * b4 * c2 * d3 * e5 + a2 * b1 * c4 * d3 * e5 - a1 * b2 * c4 * d3 * e5 - a3 * b2 * c1 * d4 * e5 + a2 * b3 * c1 * d4 * e5 + a3 * b1 * c2 * d4 * e5 - a1 * b3 * c2 * d4 * e5 - a2 * b1 * c3 * d4 * e5 + a1 * b2 * c3 * d4 * e5

# Inverse_matrix_before_second_diff = (1 / det) * Matrix(
#     [[m11, m12, m13, m14, m15],
#      [m21, m22, m23, m24, m25],
#      [m31, m32, m33, m34, m35],
#      [m41, m42, m43, m44, m45],
#      [m51, m52, m53, m54, m55]]
# )


def simplify_and_expand_component(name, component, dict_var):
    result = 0
    for term in tqdm.tqdm(component.args):
        s = 1
        index = 0
        total = len(term.args)
        while index < total:
            s = s * term.args[index]
            s = s.subs(dict_var)
            s = s.subs({C_Mx: 0, C_My: 0})
            s = remove_required_and_above_smallness_from_expression(expand(s), order=2)
            index += 1

        result = result + s

    result = simplify_determinant(result)
    with open('component_' + name + '.txt', 'w') as out:
        out.write(transform_to_simpy(str(result)))


tasks = []
for name, component in dict(
        zip(['m11', 'm12', 'm13', 'm14', 'm15', 'm21', 'm22', 'm23', 'm24', 'm25', 'm31', 'm32', 'm33', 'm34', 'm35', 'm41', 'm42', 'm43', 'm44', 'm45', 'm51', 'm52', 'm53', 'm54', 'm55', 'det'],
            [m11, m12, m13, m14, m15, m21, m22, m23, m24, m25, m31, m32, m33, m34, m35, m41, m42, m43, m44, m45, m51, m52, m53, m54, m55, det])).items():
    task = Process(
        target=simplify_and_expand_component,
        args=(name, component, main_vars_subs)
    )
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

# for k, v in dict(zip(['m21', 'm22', 'm23', 'm24', 'm25', 'm31', 'm32', 'm33', 'm34', 'm35', 'm41', 'm42', 'm43', 'm44', 'm45', 'm51', 'm52', 'm53', 'm54', 'm55', 'det'],
#                      [m21,   m22,    m23,   m24,   m25,   m31,   m32,   m33,   m34,   m35,   m41,   m42,   m43,   m44,   m45,   m51,   m52,   m53,   m54,   m55,   det])).items():
#     print(k, "=", replace_space_to_multiplication_sym(v))