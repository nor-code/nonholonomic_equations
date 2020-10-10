from sympy import *

# время
t = Symbol('t')

# радиус сферической оболочки
R = Symbol('R')

# радиус колесика
r = Symbol('r')

# координаты центра сферической оболочки
x, y = symbols('x y')
x = Function('x')(t)
y = Function('y')(t)

# углы Крылова для платформы
x1 = Symbol('α')
x1 = Function('α')(t)

x2 = Symbol('β')
x2 = Function('β')(t)

x3 = Symbol('γ')
x3 = Function('γ')(t)

# углы поворота колеса относительно с.к. связанной с платформой
x4 = Symbol('φ')
x4 = Function('φ')(t)

x5 = Symbol('ψ')
x5 = Function('ψ')(t)

# углы Крылова для сферической оболочки
x6 = Symbol('δ')
x6 = Function('δ')(t)

x7 = Symbol('ε')
x7 = Function('ε')(t)

x8 = Symbol('τ')
x8 = Function('τ')(t)

# список обобщённых координат
generic_vars = [x, y, x1, x2, x3, x4, x5, x6, x7, x8]
size_generic_vars = len(generic_vars)

# абсолютные угловые скорости платформы в проекциях на подвижные оси
p_p = diff(x2, t) * cos(x3) - diff(x1, t) * sin(x3) * cos(x2)
q_p = diff(x1, t) * sin(x2) + diff(x3, t)
r_p = diff(x2, t) * sin(x3) + diff(x1, t) * cos(x3) * sin(x2)

# абсолютные угловые скорости колеса в проекциях на подвижные оси связанные с платформой
p_k = p_p + diff(x4, t) * cos(x5)
q_k = q_p + diff(x4, t) * sin(x5)
r_k = r_p + diff(x5, t)

# абсолютные угловые скорости сферы в проекции на подвижные оси
p_s = diff(x7, t) * cos(x8) - diff(x6, t) * sin(x8) * cos(x7)
q_s = diff(x6, t) * sin(x7) + diff(x8, t)
r_s = diff(x7, t) * sin(x8) + diff(x6, t) * cos(x8) * sin(x7)

# матрица перехода от O_x1_x2_x3  к CXYZ
P_x_X = Matrix([[cos(x1) * cos(x3) - sin(x1) * sin(x2) * sin(x3), -sin(x1) * cos(x2),
                 cos(x1) * sin(x3) + cos(x3) * sin(x1) * sin(x2)],
                [sin(x1) * cos(x3) + cos(x1) * sin(x2) * sin(x3), cos(x1) * cos(x2),
                 sin(x1) * sin(x3) - cos(x1) * sin(x2) * cos(x3)],
                [-cos(x2) * sin(x3), sin(x2), cos(x2) * cos(x3)]])

# матрица перехода от O_y1_y2_y3 к CXYZ
P_y_Y = Matrix([[cos(x6) * cos(x8) - sin(x6) * sin(x7) * sin(x8), -sin(x6) * cos(x7),
                 cos(x6) * sin(x8) + cos(x8) * sin(x6) * sin(x7)],
                [sin(x6) * cos(x8) + cos(x6) * sin(x7) * sin(x8), cos(x6) * cos(x7),
                 sin(x6) * sin(x8) - cos(x6) * sin(x7) * cos(x8)],
                [-cos(x7) * sin(x8), sin(x7), cos(x7) * cos(x8)]])

# скорость точки касания колеса и сферической оболочки (принадлежащей колесу) в с.к. СXYZ
# x'e_x + y'e_y не учитывается т.к. все равно сократится
e_x1 = Matrix([[1], [0], [0]])
e_x2 = Matrix([[0], [1], [0]])
V_T_w = P_x_X * ((-R * q_p - r * diff(x4, t) * sin(x5)) * e_x1 + (p_s * R + r * diff(x4, t) * cos(x5)) * e_x2)

# скорость точки касания колеса и сферической оболочки (принадлежащей сферической оболочке) в с.к. СXYZ
# x'e_x + y'e_y не учитывается т.к. все равно сократится
Omega_S = P_y_Y * Matrix([[p_s], [q_s], [r_s]])
R_s = P_x_X * Matrix([[0], [0], [-R]])

V_T_s = Matrix([[Omega_S[1] * R_s[2] - Omega_S[2] * R_s[1]],
                [- (Omega_S[0] * R_s[2] - Omega_S[2] * R_s[0])],
                [Omega_S[0] * R_s[1] - Omega_S[1] * R_s[0]]])

# условия равенства скоростей V_T_w = V_T_s
# колесо движется без проскальзывания по сферической оболочке
V_X = expand(V_T_w[0] - V_T_s[0])
V_Y = expand(V_T_w[1] - V_T_s[1])
V_Z = expand(V_T_w[2] - V_T_s[2])

# сферическая оболочка движется без проскальзывания по поверхности
V_S_X = expand(diff(x, t) - R * q_s)
V_S_Y = expand(diff(y, t) - R * p_s)

# список неголономных связей
nonholonomic_links = [V_S_X, V_S_Y, V_X, V_Y, V_Z]
size_nonholonomic_links = len(nonholonomic_links)

def group_by_coordinate(var, expression):
    return collect(expression, diff(var, t)).coeff(diff(var, t))

def build_row(link):
    row = Matrix([range(size_generic_vars)])

    for coordinate in generic_vars:
        coefficient = trigsimp(group_by_coordinate(coordinate, link))
        position = generic_vars.index(coordinate, 0, size_generic_vars)
        row[position] = coefficient

    return row

def build_matrix():
    B = Matrix([range(size_generic_vars)])

    for link in nonholonomic_links:
        row = build_row(link)
        print(row)
        B.row_insert(nonholonomic_links.index(link, 0, size_nonholonomic_links) + 1, row)

    B.row_del(0)
    return B