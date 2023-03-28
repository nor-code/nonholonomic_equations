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
    x, u, y, v, x1, s1, x2, p, x5, q, x6, w1, x3, x4, x7, x8 = y

    g = 10
    det = - 1.90851778423831e-31

    eq1 = (-1.97691353227865e-31*x1 - 3.82303622092819e-30*x2 - 5.53079647595135e-30*x3 + 1.97691353227865e-31*x6 + 4.21534638775867e-33*x7 - 1.5777680732415e-34*x8 - 5.56266418986307e-32*x5 + 8.90948983600028e-32) / det
    eq2 = (-2.48925491476809e-31*x1 - 3.0704252134923e-29*x2 - 2.04934187722853e-29*x3 + 2.48925491476809e-31*x6 - 1.22063281540091e-30*x7 + 1.24735481581263e-32*x8 + 1.68059349894109e-30*x5 + 4.05421529860773e-30) / det
    eq3 = (-2.49201582209273e-30*x1 + 5.2044327855804e-28*x2 + 5.1915402936477e-28*x3 + 2.49201582209273e-30*x6 - 7.12971959567292e-30*x7 + 7.28113933758136e-32*x8 - 1.4242312856007e-28*x5 - 1.64864276595099e-28) / det
    eq4 = (-2.56310474617209e-29*x1 + 1.53693399181981e-28*x2 - 2.9200095981471e-28*x3 + 2.56310474617209e-29*x6 - 1.29562046697849e-31*x7 - 5.98394648472464e-34*x8 + 6.5196526483529e-29*x5 - 7.18487386453375e-30) / det
    eq5 = (2.91293769865105e-5*x1 - 0.00642178321401644*x2 - 0.00195558087339103*x3 - 2.91293769865105e-5*x6 + 5.49762612114189e-6*x7 - 5.33358684656883e-8*x8 + 8.85794729076537e-7*x5 + 0.00127448888060242) / det
    eq6 = 0
    eq7 = -0.862404227243338*s1 + 12.3456790123457*u
    eq8 = -15.0621714974648*v + 0.353806886246902*w1
    eq9 = -2.5535188248263*p + 0.903452544384642*s1 + 2.41613680080227e-15*u - 38.4615384615385*v
    eq10 = 12.3456790123457*u - 0.862404227243338*w1

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


t = np.linspace(0, 10, 10000)

y0 = [0, 0,
      0, 0,
      pi/3, 0,
      0, 0,
      0, 0,
      0, 0,
      0,
      0,
      0,
      0
]

sol = odeint(system_eq, y0, t, rtol=1e-11)

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
ax[2][1].set_ylabel('s1')
ax[2][1].plot(t, sol[:, 5])

### β
ax[3][0].set_xlabel('t')
ax[3][0].set_ylabel('β')
ax[3][0].plot(t, sol[:, 6])

ax[3][1].set_xlabel('t')
ax[3][1].set_ylabel('p')
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
