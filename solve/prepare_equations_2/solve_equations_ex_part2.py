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
    x, u, y1, v, x1, p, x6, q, x2, x3, x7, x8 = y

    g = 10

    det = 2.68e-8

    eq1 = -1.28 * x3 - 0.21  # x
    eq2 = 0.21 * x1 + 1.28 * x2 - 0.21 # y
    eq3 = 15.75 * x2 + 15.75 * x3  # α
    eq4 = -0.039 * x2 - 0.039 * x3  # δ

    # eq1 = (-3.44e-9*g*x3 - 5.68e-10*g) / det  # x
    # eq2 = (+5.69e-10*g*x1 + 3.44e-9*g*x2 - 5.68e-10*g) / det  # y
    # eq3 = (4.22e-8*g*x2 + 4.22e-8*g*x3) / det  # α
    # eq4 = -0.0039*g*x2 - 0.0039*g*x3 # δ

    eq7 = - 12.3456790123457*v  # β
    eq8 = 12.3456790123457*u  # γ
    eq9 = - 12.3456790123457*v  # ε
    eq10 = 12.3456790123457*u  # τ

    dy1dx = [u,    # 0  x
             eq1,  # 1  u

             v,    # 2  y
             eq2,  # 3  v

             p,    # 4  α
             eq3,  # 5  p

             q,   # 6  δ
             eq4,  # 7  q

             eq7,  # 8  β
             eq8,  # 9  γ
             eq9,  # 10 ε
             eq10  # 11 τ
    ]
    return dy1dx


t = np.linspace(0, 50, 10000)

y0 = [0, 0,         # 0 1
      0, 0,         # 2 3
      0, 0,         # 4 5
      0, 0,         # 6 7
      0,  # 0.1650625,  # 8
      0,  # -0.1650625, # 9
      0,            # 10
      0             # 11
]

sol = odeint(system_eq, y0, t)

fig, ax = plt.subplots(6, 2)
fig.subplots_adjust(wspace=0.4, hspace=0.4)

### x
ax[0][0].set_xlabel('t')
ax[0][0].set_ylabel('x, [m]')
ax[0][0].plot(t, sol[:, 0])

ax[0][1].set_xlabel('t')
ax[0][1].set_ylabel(r"$\dot x$, [m/s]")
ax[0][1].plot(t, sol[:, 1])

### y
ax[1][0].set_xlabel('t')
ax[1][0].set_ylabel('y, [m]')
ax[1][0].plot(t, sol[:, 2])

ax[1][1].set_xlabel('t')
ax[1][1].set_ylabel(r"$\dot y$, [m/s]")
ax[1][1].plot(t, sol[:, 3])

### α
ax[2][0].set_xlabel('t')
ax[2][0].set_ylabel('α, [rad]')
ax[2][0].plot(t, sol[:, 4])

ax[2][1].set_xlabel('t')
ax[2][1].set_ylabel(r"$\dot α$, [rad/s]")
ax[2][1].plot(t, sol[:, 5])

### δ
ax[3][0].set_xlabel('t')
ax[3][0].set_ylabel('δ, [rad]')
ax[3][0].plot(t, sol[:, 6])

ax[3][1].set_xlabel('t')
ax[3][1].set_ylabel(r"$\dot δ$, [rad/s]")
ax[3][1].plot(t, sol[:, 7])

### γ
ax[4][0].set_xlabel('t')
ax[4][0].set_ylabel('β, [rad]')
ax[4][0].plot(t, sol[:, 8])

### φ
ax[4][1].set_xlabel('t')
ax[4][1].set_ylabel('γ, [rad]')
ax[4][1].plot(t, sol[:, 9])

### ε
ax[5][0].set_xlabel('t')
ax[5][0].set_ylabel('ε, [rad]')
ax[5][0].plot(t, sol[:, 10])

### τ
ax[5][1].set_xlabel('t')
ax[5][1].set_ylabel('τ, [rad]')
ax[5][1].plot(t, sol[:, 11])

### траектория y-x
fig1, ax1 = plt.subplots(1, 1)
ax1.set_xlabel('x, [m]')
ax1.set_ylabel('y, [m]', rotation="horizontal")
ax1.plot(sol[:, 0], sol[:, 2])
ax1.grid()

#
### на одном графике β, γ
fig2, ax2 = plt.subplots(1, 1)
ax2.plot(t, sol[:, 8], 'r', linewidth=3, label='β')
ax2.plot(t, sol[:, 9], 'b', linewidth=1.5, label='γ')
ax2.legend(loc='best')
ax2.set_xlabel('t, [s]', loc='center')
ax2.set_ylabel('[rad]', loc='center', rotation="horizontal")
ax2.set_title('β, y')
ax2.grid()

fig3, ax3 = plt.subplots(1, 1)
ax3.set_xlabel('t, [s]')
ax3.set_ylabel('[m]', rotation="horizontal")
ax3.plot(t, sol[:, 0], label='x', linewidth=3)
ax3.plot(t, sol[:, 2], label='y')
ax3.legend(loc='best')
ax3.grid()

### на одном графике α, δ
fig4, ax4 = plt.subplots(1, 1)
ax4.plot(t, sol[:, 4], 'r', linewidth=3, label='α')
ax4.plot(t, sol[:, 6], 'g', linewidth=2.1, label='δ')
ax4.plot(t, sol[:, 4] - sol[:, 6], 'b',  linewidth=2.1, label='α - δ')
ax4.legend(loc='best')
ax4.set_xlabel('t, [s]', loc='center')
ax4.set_ylabel('[rad]', loc='center', rotation="horizontal")
ax4.set_title('α, δ')
ax4.grid()

### на одном графике δ
fig5, ax4 = plt.subplots(1, 1)
ax4.plot(t, sol[:, 6], 'g', linewidth=2.1, label='δ')
ax4.legend(loc='best')
ax4.set_xlabel('t, [s]', loc='center')
ax4.set_ylabel('[rad]', loc='center', rotation="horizontal")
ax4.set_title('δ')
ax4.grid()


plt.show()