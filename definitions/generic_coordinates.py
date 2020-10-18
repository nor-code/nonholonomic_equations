from sympy import Symbol, Function, symbols

# время
t = Symbol('t')

# координаты центра сферической оболочки
x, y = symbols('x y')
x = Function('x')(t)
y = Function('y')(t)

# углы Крылова для платформы
# x1 = Symbol('α')
x1 = Function('α')(t)

# x2 = Symbol('β')
x2 = Function('β')(t)

# x3 = Symbol('γ')
x3 = Function('γ')(t)

# углы поворота колеса относительно с.к. связанной с платформой
# x4 = Symbol('φ')
x4 = Function('φ')(t)

# x5 = Symbol('ψ')
x5 = Function('ψ')(t)

# углы Крылова для сферической оболочки
# x6 = Symbol('δ')
x6 = Function('δ')(t)

# x7 = Symbol('ε')
x7 = Function('ε')(t)

# x8 = Symbol('τ')
x8 = Function('τ')(t)