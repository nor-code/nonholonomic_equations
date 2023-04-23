from sympy import expand, sin, cos, trigsimp, collect, symbols
from sympy.polys.polyoptions import Symbols
from sympy.solvers.ode.systems import linear_ode_to_matrix

from definitions.generic_coordinates import *
from definitions.constants import *
from utils.Wolfram import Wolfram
from sympy.solvers.solveset import linsolve, linear_eq_to_matrix
from sympy import Derivative
import sympy as sym
from utils.latex_converter import print_in_latex

size_generic_vars = len(generic_vars)

# абсолютные угловые скорости платформы в проекциях на подвижные оси
p_p = diff(x2, t) * cos(x3) - diff(x1, t) * sin(x3) * cos(x2)
print("p_p = ", print_in_latex(p_p))
q_p = diff(x1, t) * sin(x2) + diff(x3, t)
print("q_p = ", print_in_latex(q_p))
r_p = diff(x2, t) * sin(x3) + diff(x1, t) * cos(x3) * cos(x2)
print("r_p = ", print_in_latex(r_p))

# абсолютные угловые скорости колеса в проекциях на подвижные оси связанные с платформой
p_w = p_p  # - diff(x4, t) * sin(x5)
q_w = q_p  # + diff(x4, t) * cos(x5)
r_w = r_p  # + diff(x5, t)

# абсолютные угловые скорости сферы в проекции на подвижные оси
p_s = diff(x7, t) * cos(x8) - diff(x6, t) * sin(x8) * cos(x7)
print("p_s = ", print_in_latex(p_s))
q_s = diff(x6, t) * sin(x7) + diff(x8, t)
print("q_s = ", print_in_latex(q_s))
r_s = diff(x7, t) * sin(x8) + diff(x6, t) * cos(x8) * cos(x7)
print("r_s = ", print_in_latex(r_s))

P_alpha = Matrix([[cos(x1),  sin(x1), 0],
                  [-sin(x1), cos(x1), 0],
                  [0,        0,       1]])

P_beta = Matrix([[1, 0,        0],
                 [0, cos(x2),  sin(x2)],
                 [0, -sin(x2), sin(x2)]])

P_gamma = Matrix([[cos(x3), 0, -sin(x3)],
                  [0,       1, 0],
                  [sin(x3), 0, sin(x3)]])
# матрица перехода от O_x1_x2_x3  к CXYZ
P_x_X = Matrix([[cos(x1) * cos(x3) - sin(x1) * sin(x2) * sin(x3), -sin(x1) * cos(x2),
                 cos(x1) * sin(x3) + cos(x3) * sin(x1) * sin(x2)],
                [sin(x1) * cos(x3) + cos(x1) * sin(x2) * sin(x3), cos(x1) * cos(x2),
                 sin(x1) * sin(x3) - cos(x1) * sin(x2) * cos(x3)],
                [-cos(x2) * sin(x3), sin(x2), cos(x2) * cos(x3)]])
    #P_alpha.transpose() * P_beta.transpose() * P_gamma.transpose()  # (P_gamma * P_beta * P_alpha).transpose()

P_delta = Matrix([[cos(x6),  sin(x6),  0],
                  [-sin(x6), cos(x6),  0],
                  [0,        0,        1]])

P_epsilon = Matrix([[1, 0,        0],
                    [0, cos(x7),  sin(x7)],
                    [0, -sin(x7), sin(x7)]])

P_tau = Matrix([[cos(x8), 0,  -sin(x8)],
                [0,       1,  0],
                [sin(x8), 0,  sin(x8)]])
# матрица перехода от O_y1_y2_y3 к CXYZ
P_y_Y = Matrix([[cos(x6) * cos(x8) - sin(x6) * sin(x7) * sin(x8), -sin(x6) * cos(x7),
                 cos(x6) * sin(x8) + cos(x8) * sin(x6) * sin(x7)],
                [sin(x6) * cos(x8) + cos(x6) * sin(x7) * sin(x8), cos(x6) * cos(x7),
                 sin(x6) * sin(x8) - cos(x6) * sin(x7) * cos(x8)],
                [-cos(x7) * sin(x8), sin(x7), cos(x7) * cos(x8)]])
#P_alpha.transpose() * P_beta.transpose() * P_gamma.transpose()  # (P_tau * P_epsilon * P_delta).transpose()

# скорость точки касания колеса и сферической оболочки (принадлежащей колесу) в с.к. СXYZ
# x'e_x + y'e_y не учитывается т.к. все равно сократится
e_x1 = Matrix([[1], [0], [0]])
e_x2 = Matrix([[0], [1], [0]])
e_x3 = Matrix([[0], [0], [1]])
V_T_w = expand(P_x_X * (Matrix([[p_p], [q_p], [r_p]]).cross(Matrix([[0], [0], [-(R-r)]])) + Matrix([[p_w], [q_w], [r_w]]).cross(Matrix([[0], [0], [-r]]))), deep=True)
# P_x_X * ((-(R-r) * q_p - r * diff(x4, t) * sin(x5)) * e_x1 + (p_p * (R-r) + r * diff(x4, t) * cos(x5)) * e_x2)

# скорость точки касания колеса и сферической оболочки (принадлежащей сферической оболочке) в с.к. СXYZ
# x'e_x + y'e_y не учитывается т.к. все равно сократится
Omega_S = P_y_Y * Matrix([[p_s], [q_s], [r_s]])
R_s = P_x_X * Matrix([[0], [0], [-R]])

V_T_s = Omega_S.cross(R_s)

# скорость т.O (абсолютная скорость цетра сферической оболочки) в проекции на с.к. CXYZ
V_O = diff(x, t) * Matrix([[1], [0], [0]]) + diff(y, t) * Matrix([[0], [1], [0]])

# скорость центра масс платформы в проекции на неподвижные оси,
# т.е. в с.к. С_x1_x2_x3
V_C = V_O + P_x_X * Matrix([[p_p], [q_p], [r_p]]).cross(R_cm_p)

# скорость центра масс колеса, т.е. скорость т. B в проекции на неподвижные оси,
# т.е. в с.к. С_x1_x2_x3
V_B = V_O + P_x_X * Matrix([[p_w], [q_w], [r_w]]).cross(R_cm_w)

# условия равенства скоростей V_T_w = V_T_s
# колесо движется без проскальзывания по сферической оболочке
V_X = expand(V_T_w[0] - V_T_s[0])
V_Y = expand(V_T_w[1] - V_T_s[1])
V_Z = expand(V_T_w[2] - V_T_s[2])

# Rr = Matrix([[0], [0], [-R]])
# V_S = V_O + Matrix([[p_s], [q_s], [r_s]]).cross(Rr)
# сферическая оболочка движется без проскальзывания по поверхности
V_S_X = expand(diff(x, t) - R * q_s)
V_S_Y = expand(diff(y, t) + R * p_s)

# угловая скорость колеса = угловой скорости оболочки TODO пока не вводим эту гипотезу
# sphere_angular_velocity = P_y_Y * (r_s * e_x3)
# wheel_angular_velocity = P_x_X * (r_w * e_x3)
# A_X = expand(sphere_angular_velocity[0] - wheel_angular_velocity[0])
# A_Y = expand(sphere_angular_velocity[1] - wheel_angular_velocity[1])
# A_Z = expand(sphere_angular_velocity[2] - wheel_angular_velocity[2])
# список неголономных связей
nonholonomic_links = [V_S_X, V_S_Y, V_X, V_Y, V_Z]
size_nonholonomic_links = len(nonholonomic_links)


def group_by_coordinate(var, expression):
    return collect(expression, diff(var, t)).coeff(diff(var, t))


def build_row(link, parser):
    row = Matrix([range(size_generic_vars)])

    for coordinate in generic_vars:
        coefficient = group_by_coordinate(coordinate, link)
        print(coordinate, ": ", parser.transformForWolframMathematica(str(coefficient)))
        position = generic_vars.index(coordinate, 0, size_generic_vars)
        row[position] = coefficient

    return row


def build_matrix():
    B = Matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    parser = Wolfram()

    print("___________NONHOLONOMIC__LINKS__MATRIX___________")

    count = 0
    for link in nonholonomic_links:
        print("link #", count, ": ", link)
        count += 1
        print("\nrow number ", count)
        row = build_row(link, parser)
        print(row)
        B = B.row_insert(nonholonomic_links.index(link, 0, size_nonholonomic_links) + 1, row)

    B.row_del(0)
    # print("ранг матрицы B = ", B.rank(), " количество строк = ", B.rows)
    B.row_del(4)
    return B
