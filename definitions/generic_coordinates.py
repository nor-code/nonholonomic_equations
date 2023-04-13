from sympy import Symbol, Function, symbols, diff
import itertools

# время
t = Symbol('t')

# координаты центра сферической оболочки
x, y = symbols('x y')
x = Function('x')(t)
y = Function('y')(t)

# углы Крылова для платформы
x1 = Function('α')(t)
x2 = Function('β')(t)
x3 = Function('γ')(t)

# углы поворота колеса относительно с.к. связанной с платформой
x4 = Function('φ')(t)
x5 = Function('ψ')(t)

# углы Крылова для сферической оболочки
x6 = Function('δ')(t)
x7 = Function('ε')(t)
x8 = Function('τ')(t)

x20 = Symbol('β_')
x30 = Symbol('γ_')
x70 = Symbol('ε_')
x80 = Symbol('τ_')

# список обобщённых координат
generic_vars = [x, y, x1, x2, x3, x4, x5, x6, x7, x8]

first_diff_generic_vars = [diff(var, t) for var in generic_vars]


# попарные произведения первых производных координат
def build_mixed_diff():
    i = 0
    list = []
    for var in itertools.combinations([diff(var, t) for var in generic_vars], 2):
        list.insert(i, var[0] * var[1])
        i = i + 1

    for var in [diff(var, t) * diff(var, t) for var in generic_vars]:
        list.insert(i, var)
        i = i + 1
    return list


mixed_diff_of_generic_coordinates = build_mixed_diff()

# вторые производные обобщённых координат
second_diff_generic_coord = [diff(diff(var, t), t) for var in generic_vars]

print(mixed_diff_of_generic_coordinates)
