import math

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos
from scipy.integrate import odeint
from definitions.constants import *
from numba import jit
from math import sqrt, pi


# @jit
def system_eq(y, t):
    x, u, y, v, x2, p, x5, q, x3, x4, x7, x8 = y

    g = 10
    det = -0.0288131477482463

    eq1 = (2.1823764883542e-9 * g * x2 - 1.40087215164248e-5 * g * x3) / det
    eq2 = (4.26663509953055e-6 * g * x2) / det
    eq3 = (0.000311390983020061 * g * x2 - 3.56890541243072e-8 * g * x3) / det
    eq4 = 0

    eq5 = 12.3456790123457 * u
    eq6 = 12.3456790123457 * v
    eq7 = -3.11538461538462 * p + 38.4615384615385 * v
    eq8 = 12.3456790123457 * u

    dy1dx = [u,
             eq1,

             v,
             eq2,

             p,
             eq3,

             q,
             eq4,

             eq5,
             eq6,
             eq7,
             eq8
             ]
    return dy1dx


t = np.linspace(0, 30, 10_000)

y0 = [0, 0,
      0, 0,
      pi/12, pi/12,
      0, 0,
      0,
      0,
      0,
      0
]

sol = odeint(system_eq, y0, t, rtol=1e-9)

fig, ax = plt.subplots(6, 2)

### x
ax[0][0].set_xlabel('t')
ax[0][0].set_ylabel('x')
ax[0][0].plot(t, sol[:, 0])

ax[0][1].set_xlabel('t')
ax[0][1].set_ylabel('u')
ax[0][1].plot(t, sol[:, 1])

### y
ax[1][0].set_xlabel('t')
ax[1][0].set_ylabel('y')
ax[1][0].plot(t, sol[:, 2])

ax[1][1].set_xlabel('t')
ax[1][1].set_ylabel('v')
ax[1][1].plot(t, sol[:, 3])

### β
ax[2][0].set_xlabel('t')
ax[2][0].set_ylabel('β')
ax[2][0].plot(t, sol[:, 4])

ax[2][1].set_xlabel('t')
ax[2][1].set_ylabel('p')
ax[2][1].plot(t, sol[:, 5])

### ψ
ax[3][0].set_xlabel('t')
ax[3][0].set_ylabel('ψ')
ax[3][0].plot(t, sol[:, 6])

ax[3][1].set_xlabel('t')
ax[3][1].set_ylabel('q')
ax[3][1].plot(t, sol[:, 7])

### γ
ax[4][0].set_xlabel('t')
ax[4][0].set_ylabel('γ')
ax[4][0].plot(t, sol[:, 8])

### φ
ax[4][1].set_xlabel('t')
ax[4][1].set_ylabel('φ')
ax[4][1].plot(t, sol[:, 9])

### ε
ax[5][0].set_xlabel('t')
ax[5][0].set_ylabel('ε')
ax[5][0].plot(t, sol[:, 10])

### τ
ax[5][1].set_xlabel('t')
ax[5][1].set_ylabel('τ')
ax[5][1].plot(t, sol[:, 11])

fig1, ax1 = plt.subplots(1, 1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.plot(sol[:, 0], sol[:, 2])

plt.show()
