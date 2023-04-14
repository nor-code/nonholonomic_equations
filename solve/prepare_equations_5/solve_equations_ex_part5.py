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
    x, u, y1, v, x1, p, x4, q, x5, s1, x6, w1, x2, x3, x7, x8 = y

    g = 10
    det = -2.72618614015244e-15

    eq1 = (-3.47186944350596e-17*x1 + 5.35168824430658e-16*x2 + 2.07483824262588e-14*x3 + 3.47186944350596e-17*x6 + 6.89254533937012e-16*x5 + 4.35518009332592e-15) / det # x
    eq2 = (4.10473510242872e-16*x1 - 5.21744871383172e-15*x2 - 5.12350349066898e-16*x3 - 4.10473510242872e-16*x6 + 8.34066815398982e-19*x5 + 7.53067731151201e-17) / det # y
    eq3 = (4.14756245024708e-14*x1 - 2.18331242525383e-13*x2 - 4.85378344826863e-14*x3 - 4.14756245024707e-14*x6 - 4.28760811666116e-16*x5 - 2.56120253194472e-15) / det# α
    eq4 = (2.63173128094084e-14*x1 - 7.10149729706774e-15*x2 - 8.96477333147012e-13*x3 - 2.63173128094084e-14*x6 - 4.9411305522153e-15*x5 - 1.88737601407041e-13) / det# φ
    eq5 = -0.0585*x2 - 0.00975*x3 # δ
    eq6 = (5.50698214450942e-16*x1 - 2.06533429856855e-12*x2 - 3.51254205477793e-13*x3 - 5.50698214450941e-16*x6 - 2.36147643240879e-16*x5 - 1.48238417804507e-15) / det# ψ

    eq7 = -12.3456790123457*v # β
    eq8 = -0.320987654320988*q + 12.3456790123457*u # γ
    eq9 = -12.3456790123457*v # ε
    eq10 = 12.3456790123457*u # τ

    dy1dx = [u,    # 0  x
             eq1,  # 1  u

             v,    # 2  y
             eq2,  # 3  v

             p,    # 4  α
             eq3,  # 5  p

             q,    # 6  φ
             eq4,  # 7  q

             w1,   # 8  δ
             eq5,  # 9  w1

             s1,   # 10 ψ
             eq6,  # 11 s1

             eq7,  # 12 β
             eq8,  # 13 γ
             eq9,  # 14 ε
             eq10  # 15 τ
    ]
    return dy1dx


t = np.linspace(0, 20, 10000)

y0 = [0, 0,
      0, 0,
      0, 0,
      0, 0,
      0, 0,
      0, 0,
      0,
      pi/5,
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

### β
ax[3][0].set_xlabel('t')
ax[3][0].set_ylabel('φ')
ax[3][0].plot(t, sol[:, 6])

ax[3][1].set_xlabel('t')
ax[3][1].set_ylabel('q')
ax[3][1].plot(t, sol[:, 7])

### δ
ax[4][0].set_xlabel('t')
ax[4][0].set_ylabel('δ')
ax[4][0].plot(t, sol[:, 8])

ax[4][1].set_xlabel('t')
ax[4][1].set_ylabel('w1')
ax[4][1].plot(t, sol[:, 9])

### ψ
ax[5][0].set_xlabel('t')
ax[5][0].set_ylabel('ψ')
ax[5][0].plot(t, sol[:, 10])

ax[5][1].set_xlabel('t')
ax[5][1].set_ylabel('s1')
ax[5][1].plot(t, sol[:, 11])

### γ
ax[6][0].set_xlabel('t')
ax[6][0].set_ylabel('β')
ax[6][0].plot(t, sol[:, 12])

### φ
ax[6][1].set_xlabel('t')
ax[6][1].set_ylabel('γ')
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