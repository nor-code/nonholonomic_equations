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
    det = 5.22081647244234e-11

    eq1 = (-4.3731972343125e-12*g*x3) / det
    eq2 = (1.85870132529682e-11*g*x2) / det
    eq3 = (-1.05690771180335e-9*g*x2) / det
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


t = np.linspace(0, 15, 10000)

y0 = [0, 0,
      0, 0,
      pi/3, 0,
      0, 0,
      pi/3,
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

### траектория y-x
fig1, ax1 = plt.subplots(1, 1)
ax1.set_xlabel('x, [m]')
ax1.set_ylabel('y, [m]', rotation="horizontal")
ax1.plot(sol[:, 0], sol[:, 2])


### на одном графике φ, β, x, y
fig1, ax2 = plt.subplots(1, 1)
ax2.plot(t, sol[:, 4], 'r', linewidth=3, label='β')
ax2.plot(t, sol[:, 10], 'g', linewidth=2.1, label='φ')
ax2.plot(t, sol[:, 8], 'b', linewidth=1.5, label='γ')
# ax2.plot(t, sol[:, 0], 'g', linewidth=1.6, label='x')
# ax2.plot(t, sol[:, 2], 'm', linewidth=1.1, label='y')

ax2.legend(loc='best')
ax2.set_xlabel('t, [s]', loc='center')
ax2.set_ylabel('[rad]', loc='center', rotation="horizontal")
ax2.set_title('φ, β, y')
ax2.grid()

fig3, ax3 = plt.subplots(1, 1)
ax3.set_xlabel('t, [s]')
ax3.set_ylabel('y, [m]', rotation="horizontal")
ax3.plot(t, sol[:, 0], label='x', linewidth=3)
ax3.plot(t, sol[:, 2], label='y')
ax3.legend(loc='best')


plt.show()
