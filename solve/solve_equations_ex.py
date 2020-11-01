import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from scipy.integrate import odeint

q = Symbol('q')

a = Symbol('a')
b = Symbol('b')

x = Function('x')(q)
x1 = Function('x1')(q)
y = Function('y')(q)
x2 = Function('x2')(q)
l1 = Function('l1')(q)
l2 = Function('l2')(q)

print(k)

x_ = lambdify(q, x)
x1_ = lambdify(q, x1)
y_ = lambdify(q, y)
x2_ = lambdify(q, x2)
l1_ = lambdify(q, l1)
l2_ = lambdify(q, l2)

def system_eq(y1, t, x, x1, y, x2, l1, l2):
    (x, x1, y, x2, l1, l2) = y1
    dy1dx = [x1,
             5 * x1 * x2 - 2 * l1 - 9 * l2,
             x2,
             7 * x1 * x2 - 4 * l1 + 8 * l2,
             -2 * x1 - 4 * x2,
             -9 * x1 + 8 * x2
             ]
    return dy1dx

t = np.linspace(0, 10, 1000)
y1 = [1, 1, 1, 1, 0, 0]

sol = odeint(system_eq, y1, t, args=(x_, x1_, y_, x2_, 0, 0))

fig = plt.figure(1, figsize=(14, 6), frameon=False)

# ax1 = fig.add_subplot(211)
# ax1.set_xlabel('t')
# ax1.set_xlabel('x')
# ax1.plot(t, sol[:, 0])
#
# ax2 = fig.add_subplot(212)
# ax2.set_xlabel('t')
# ax2.set_xlabel('x1')
# ax2.plot(t, sol[:, 1])
#
# ax2 = fig.add_subplot(213)
# ax2.set_xlabel('t')
# ax2.set_xlabel('y')
# ax2.plot(t, sol[:, 2])
#
# ax2 = fig.add_subplot(214)
# ax2.set_xlabel('t')
# ax2.set_xlabel('x2')
# ax2.plot(t, sol[:, 3])

ax2 = fig.add_subplot(211)
ax2.set_xlabel('t')
ax2.set_xlabel('l1')
ax2.plot(t, sol[:, 4])

ax2 = fig.add_subplot(212)
ax2.set_xlabel('t')
ax2.set_xlabel('x2')
ax2.plot(t, sol[:, 3])
plt.show()
