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

    det = 6.53087553265475e-14
    eq1 = (3.69655282205437e-16*g*x1 + 5.429320817293e-15*g*x2 - 1.70817909202007e-15*g*x3 - 3.69655282205437e-16*g*x6 - 7.02050018543132e-16*g) / det
    eq2 = (1.89386726787535e-16*g*x1 - 7.15100644235474e-15*g*x2 - 5.23716128758005e-15*g*x3 - 1.89386726787535e-16*g*x6 - 1.41830573108954e-15*g) / det
    eq3 = (-9.179232243503e-14*g*x1 + 4.63032877225614e-13*g*x2 - 3.81850034446444e-13*g*x3 + 9.17923224350299e-14*g*x6 - 1.27814273960649e-13*g) / det
    eq4 = (2.24680226240754e-12*g*x1 - 8.85361214565921e-12*g*x2 + 7.61335206428454e-12*g*x3 - 2.24680226240754e-12*g*x6 + 2.52013179935455e-12*g) / det

    # det = -1.10807131424325e-13
    # eq1 = (6.65172551691775e-15*g*x1 + 1.51366292465507e-13*g*x2 + 1.52411352671768e-13*g*x3 - 6.65172551691775e-15*g*x6 + 2.28523620822782e-14*g) / det
    # eq2 = (1.0359991529522e-14*g*x1 - 1.70045763995611e-13*g*x2 - 1.58607722903397e-13*g*x3 - 1.0359991529522e-14*g*x6 - 5.06960286511912e-15*g) / det
    # eq3 = (3.38569864780856e-12*g*x1 - 1.12514420611463e-12*g*x2 - 1.62139797053828e-12*g*x3 - 3.38569864780856e-12*g*x6 - 1.00461986130818e-12*g) / det
    # eq4 = 0

    # eq1 =(2.07301048323755e-13*g*x1 - 1.4103622914403e-13*g*x2 + 3.89169019256306e-13*g*x3 - 2.07301048323755e-13*g*x6 ) / det  # x
    # eq2 = (4.20844725337248e-14*g*x1 - 9.09431223392208e-14*g*x2 - 1.02624908996616e-13*g*x3 - 4.20844725337248e-14*g*x6 ) / det  # y
    # eq3 = (1.85913438195807e-12*g*x1 + 3.01429457260026e-12*g*x2 + 1.38086993392422e-11*g*x3 - 1.85913438195807e-12*g*x6 ) / det  # α
    # eq4 = (9.12509171526431e-11*g*x1 - 3.56348508552872e-11*g*x2 - 5.12680190367201e-11*g*x3 - 9.12509171526431e-11*g*x6 + 3.6482164964458e-13*g ) / det  # δ

    eq7 = - 12.3456790123457*v  # β
    eq8 = + 12.3456790123457*u  # γ
    eq9 = - 12.3456790123457*v  # ε
    eq10 = + 12.3456790123457*u  # τ

    dydx = [u,    # 0  x
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
    return dydx


t = np.linspace(0, 10, 10000)

y0 = [0, 0.1,
      0, 0,
      0, 0,
      0, 0,
      pi/5,
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