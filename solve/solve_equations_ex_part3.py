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
    x, u, y1, v, x1, s1, x2, p, x6, w1, x5, q, x3, x7, x4, x8 = y

    g = 10
    det = 1.04026865165399e-18

    eq1 = (-8.5851687632612e-19*x3) / det
    eq2 = (1.40949076463541e-16*x2) / det
    eq3 = 0
    eq4 = (-1.69553461911007e-16*x2) / det
    eq5 = 0 #(-0.019317922*x2 - 0.061813125*x3) / det
    eq6 = 0
    eq7 = 12.3456790123457*u
    eq8 = -12.3456790123457*v
    eq9 = -3.11538461538462*p
    eq10 = 12.3456790123457*u

    dy1dx = [u,    # 0
             eq1,  # 1

             v,    # 2
             eq2,  # 3

             s1,   # 4
             eq3,  # 5

             p,    # 6
             eq4,  # 7

             w1,   # 8
             eq5,  # 9

             q,    # 10
             eq6,  # 11

             eq7,  # 12
             eq8,  # 13
             eq9,  # 14
             eq10  # 15
    ]
    return dy1dx


t = np.linspace(0, 100, 10000)

y0 = [0, 0,
      0, 0,
      0, 0,
      pi/3, 0,
      0, 0,
      0, 0,
      0,
      0,
      0,
      0
]

sol = odeint(system_eq, y0, t)

fig, ax = plt.subplots(8, 2)

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

### α
ax[2][0].set_xlabel('t')
ax[2][0].set_ylabel('α')
ax[2][0].plot(t, sol[:, 4])

ax[2][1].set_xlabel('t')
ax[2][1].set_ylabel('α')
ax[2][1].plot(t, sol[:, 5])

### β
ax[3][0].set_xlabel('t')
ax[3][0].set_ylabel('β')
ax[3][0].plot(t, sol[:, 6])

ax[3][1].set_xlabel('t')
ax[3][1].set_ylabel('β')
ax[3][1].plot(t, sol[:, 7])

### δ
ax[4][0].set_xlabel('t')
ax[4][0].set_ylabel('δ')
ax[4][0].plot(t, sol[:, 8])

ax[4][1].set_xlabel('t')
ax[4][1].set_ylabel('δ')
ax[4][1].plot(t, sol[:, 9])

### ψ
ax[5][0].set_xlabel('t')
ax[5][0].set_ylabel('ψ')
ax[5][0].plot(t, sol[:, 10])

ax[5][1].set_xlabel('t')
ax[5][1].set_ylabel('q')
ax[5][1].plot(t, sol[:, 11])

### γ
ax[6][0].set_xlabel('t')
ax[6][0].set_ylabel('γ')
ax[6][0].plot(t, sol[:, 12])

### φ
ax[6][1].set_xlabel('t')
ax[6][1].set_ylabel('φ')
ax[6][1].plot(t, sol[:, 13])

### ε
ax[7][0].set_xlabel('t')
ax[7][0].set_ylabel('ε')
ax[7][0].plot(t, sol[:, 14])

### τ
ax[7][1].set_xlabel('t')
ax[7][1].set_ylabel('τ')
ax[7][1].plot(t, sol[:, 15])

### траектория y-x
fig1, ax1 = plt.subplots(1, 1)
ax1.set_xlabel('x, [m]')
ax1.set_ylabel('y, [m]', rotation="horizontal")
ax1.plot(sol[:, 0], sol[:, 2])

#
# ### на одном графике φ, β, x, y
# fig1, ax2 = plt.subplots(1, 1)
# ax2.plot(t, sol[:, 4], 'r', linewidth=3, label='β')
# ax2.plot(t, sol[:, 10], 'g', linewidth=2.1, label='φ')
# ax2.plot(t, sol[:, 8], 'b', linewidth=1.5, label='γ')
# # ax2.plot(t, sol[:, 0], 'g', linewidth=1.6, label='x')
# # ax2.plot(t, sol[:, 2], 'm', linewidth=1.1, label='y')
#
# ax2.legend(loc='best')
# ax2.set_xlabel('t, [s]', loc='center')
# ax2.set_ylabel('[rad]', loc='center', rotation="horizontal")
# ax2.set_title('φ, β, y')
# ax2.grid()
#
# fig3, ax3 = plt.subplots(1, 1)
# ax3.set_xlabel('t, [s]')
# ax3.set_ylabel('y, [m]', rotation="horizontal")
# ax3.plot(t, sol[:, 0], label='x', linewidth=3)
# ax3.plot(t, sol[:, 2], label='y')
# ax3.legend(loc='best')


plt.show()
