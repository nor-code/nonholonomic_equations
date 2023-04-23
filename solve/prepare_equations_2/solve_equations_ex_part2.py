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
    det = -4.66579888334879e-9

    eq1 = (-1.048872329505e-10*g*x1 + 2.03212351424116e-9*g*x2 + 2.26506363357354e-9*g*x3 + 1.048872329505e-10*g*x6 + 1.6368765142275e-10*g) / det # x
    eq2 = (1.048872329505e-10*g*x1 - 2.26698202560477e-9*g*x2 - 2.0340419062724e-9*g*x3 - 1.048872329505e-10*g*x6 + 1.6368765142275e-10*g) / det # y
    eq3 = (5.1232628877885e-8*g*x1 - 3.64908580666256e-8*g*x2 - 3.64571541230569e-8*g*x3 - 5.1232628877885e-8*g*x6 + 2.36838522375e-11*g) / det# α
    eq4 = -0.0195*g*x2 - 0.0195*g*x3  # δ

    eq7 = -12.3456790123457*v # β
    eq8 = 12.3456790123457*u # γ
    eq9 = -12.3456790123457*v # ε
    eq10 = 12.3456790123457*u # τ

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


t = np.linspace(0, 10, 10000)

y0 = [0, 0.01,
      0, 0,
      0, 0,
      0, 0.01,
      0,
      pi/3,
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
ax[2][1].set_ylabel('p')
ax[2][1].plot(t, sol[:, 5])

### δ
ax[4][0].set_xlabel('t')
ax[4][0].set_ylabel('δ')
ax[4][0].plot(t, sol[:, 6])

ax[4][1].set_xlabel('t')
ax[4][1].set_ylabel('q')
ax[4][1].plot(t, sol[:, 7])

### γ
ax[6][0].set_xlabel('t')
ax[6][0].set_ylabel('β')
ax[6][0].plot(t, sol[:, 8])

### φ
ax[6][1].set_xlabel('t')
ax[6][1].set_ylabel('γ')
ax[6][1].plot(t, sol[:, 9])

### ε
ax[7][0].set_xlabel('t')
ax[7][0].set_ylabel('ε')
ax[7][0].plot(t, sol[:, 10])

### τ
ax[7][1].set_xlabel('t')
ax[7][1].set_ylabel('τ')
ax[7][1].plot(t, sol[:, 11])

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