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
    x, u, y1, v, x1, p, x4, q, x6, r, x2, x3, x7, x8 = y

    g = 10

    # det = 3.75451870672486e-14
    # eq1 = (7.71695371941208e-16*g*x1 - 4.53479797209057e-15*g*x3 - 5.11300796937512e-16*g) / det
    # eq2 = (7.47623962963641e-16*g*x1 + 4.77710431413173e-15*g*x2 - 7.4762396296364e-16*g) / det
    # eq3 = (5.55670212301249e-14*g*x2 + 5.76519936043361e-14*g*x3) / det
    # eq4 = (1.00151759616806e-14*g*x1 + 5.16456555178129e-13*g*x3 + 9.44469667192718e-14*g) / det
    # eq5 = -0.00195*g*x2 - 0.00195*g*x3

    # смещение ц.м. только по оси x
    det = 3.75451870672486e-14
    eq1 = (-4.53479797209057e-15*g*x3 - 5.11300796937512e-16*g)/det
    eq2 = (7.47623962963641e-16*g*x1 + 4.77710431413173e-15*g*x2)/det #-8.30693292181823e-17*g*x1 + 5.30789368236859e-16*g*x2 + 8.30693292181823e-17*g*x6
    eq3 = (5.55670212301249e-14*g*x2)/det
    eq4 = (5.16456555178129e-13*g*x3 + 9.44469667192718e-14*g)/det
    eq5 = -0.0039*g*x2

    # смещение ц.м. только по оси y TODAY
    # det = 3.75451870672486e-14
    #
    # eq1 = 0.205537761886496 * x1 - 1.20782404518804 * x3
    # eq2 = 1.27236130308135 * x2 - 0.199126445055273
    # eq3 = 15.3553619272354 * x3
    # eq4 = 2.6674992839274 * x1 + 137.555994661335 * x3
    # eq5 = -0.0039*g*x3

    # det = 4.19690438759902e-15
    # eq1 = (8.6012971956809e-17*g*x1 - 5.0241727150491e-16*g*x3) / det
    # eq2 = (5.30789368236859e-16*g*x2 - 8.30693292181823e-17*g) / det
    # eq3 = (-6.4363157334803e-15*g*x3) / det
    # eq4 = (1.13097843882775e-15*g*x1 + 5.7439798987939e-14*g*x3) / det
    # eq5 = -0.0039 * g * x3


    eq7 = - 12.35 * v  # β
    eq8 = -0.32 * q + 12.34 * u  # γ
    eq9 = - 12.35 * v  # ε
    eq10 = + 12.35 * u  # τ

    dydx = [u,     # 0  x
             eq1,  # 1  u

             v,    # 2  y
             eq2,  # 3  v

             p,    # 4  α
             eq3,  # 5  p

             q,    # 6  φ
             eq4,  # 7  q

             r,    # 8  δ
             eq5,  # 9  r

             eq7,  # 8  β
             eq8,  # 9  γ
             eq9,  # 10 ε
             eq10  # 11 τ
    ]
    return dydx


t = np.linspace(0, 50, 10000)

y0 = [0, 0,
      0, 0,
      0, 0,
      0, 0,
      0, 0,
      pi/4,
      pi/4,
      0,
      0
]

sol = odeint(system_eq, y0, t)

fig, ax = plt.subplots(7, 2)

#### x
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

### φ
ax[3][0].set_xlabel('t')
ax[3][0].set_ylabel('φ, [rad]')
ax[3][0].plot(t, sol[:, 6])

ax[3][1].set_xlabel('t')
ax[3][1].set_ylabel(r"$\dot φ$, [rad/s]")
ax[3][1].plot(t, sol[:, 7])

### δ
ax[4][0].set_xlabel('t')
ax[4][0].set_ylabel('δ, [rad]')
ax[4][0].plot(t, sol[:, 8])

ax[4][1].set_xlabel('t')
ax[4][1].set_ylabel(r"$\dot δ$, [rad/s]")
ax[4][1].plot(t, sol[:, 8])

### γ
ax[5][0].set_xlabel('t')
ax[5][0].set_ylabel('β, [rad]')
ax[5][0].plot(t, sol[:, 10])

### φ
ax[5][1].set_xlabel('t')
ax[5][1].set_ylabel('γ, [rad]')
ax[5][1].plot(t, sol[:, 11])

### ε
ax[6][0].set_xlabel('t')
ax[6][0].set_ylabel('ε, [rad]')
ax[6][0].plot(t, sol[:, 12])

### τ
ax[6][1].set_xlabel('t')
ax[6][1].set_ylabel('τ, [rad]')
ax[6][1].plot(t, sol[:, 13])

### траектория y-x
fig1, ax1 = plt.subplots(1, 1)
ax1.set_xlabel('x, [m]')
ax1.set_ylabel('y, [m]', rotation="horizontal")
ax1.plot(sol[:, 0], sol[:, 2])
ax1.grid()

#
### на одном графике β, γ
fig2, ax2 = plt.subplots(1, 1)
ax2.plot(t, sol[:, 10], 'r', linewidth=3, label='β')
ax2.plot(t, sol[:, 11], 'b', linewidth=1.5, label='γ')
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
ax4.plot(t, sol[:, 8], 'g', linewidth=2.1, label='δ')
ax4.legend(loc='best')
ax4.set_xlabel('t, [s]', loc='center')
ax4.set_ylabel('[rad]', loc='center', rotation="horizontal")
ax4.set_title('α, δ')
ax4.grid()

### на одном графике δ
fig5, ax4 = plt.subplots(1, 1)
ax4.plot(t, sol[:, 8], 'g', linewidth=2.1, label='δ')
ax4.legend(loc='best')
ax4.set_xlabel('t, [s]', loc='center')
ax4.set_ylabel('[rad]', loc='center', rotation="horizontal")
ax4.set_title('δ')
ax4.grid()


plt.show()