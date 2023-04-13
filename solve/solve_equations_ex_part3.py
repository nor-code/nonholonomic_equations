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
    det = -7.42832185376219e-23

    eq1 = 0.02925494890483 * x1 + 0.113792292013571 * x2 - 0.806578320195878 * x3 - 0.03 * x6 - 0.17
    eq2 = (0.0376586701754965 * x1 - 5.75922361715805 * x2 - 0.12629193561169 * x3 - 0.04 * x6 + 0.18)
    eq3 = (8.70922158425717 * x1 - 32.9165769808499 * x2 - 3.08853972373326 * x3 - 8.71 * x6 + 0.51)
    eq4 = (43.9796295168398 * x1 - 195.12898551432 * x2 + 0.368364122578258 * x3 - 43.98 * x6 + 6.93)
    eq5 = -0.0585 * x2 - 0.00975 * x3
    eq6 = 0 #(-0.826229324689839 * x1 - 460.556915680347 * x2 - 75.5485961948929 * x3 + 0.83 * x6 - 1.87 * x5 + 0.26)

    # eq1 = (-2.17315176280445e-24*x1 - 8.45285769554097e-24*x2 + 5.99152336268184e-23*x3 + 2.17315176280445e-24*x6 + 1.29277712781996e-23) / det
    # eq2 = (-2.79740722648263e-24*x1 + 4.27813666560385e-22*x2 + 9.38137145258243e-24*x3 + 2.79740722648263e-24*x6  - 1.30535964648204e-23) / det
    # eq3 = (-6.46949010235949e-22*x1 + 2.44514928137893e-21*x2 + 2.29426671260204e-22*x3 + 6.46949010235949e-22*x6 - 3.75450278368382e-23) / det
    # eq4 = (-3.26694843060306e-21*x1 + 1.44948090739847e-20*x2 - 2.73632726189001e-23*x3 + 3.26694843060306e-21*x6  - 5.15045549259663e-22) / det
    # eq5 = -0.0585*x2 - 0.00975*x3
    # eq6 = (6.13749734881271e-23*x1 + 3.42116500164963e-20*x2 + 5.61199288135578e-21*x3 - 6.13749734881271e-23*x6 + 1.39258239262595e-22*x5 - 1.8962176942436e-23) / det
    eq7 = 12.3456790123457*u
    eq8 = -12.3456790123457*v
    eq9 = -3.11538461538462*p - 38.4615384615385*v
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


t = np.linspace(0, 20, 10000)

y0 = [0, 0,
      0, 0,
      0, 0,
      pi/5, 0,
      0, 0,
      0, 0,
      pi/5,
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
