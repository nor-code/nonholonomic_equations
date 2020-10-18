from Kinematics import *
from definitions.moments import *
from definitions.lagrangian_multipliers import *

# вторые производные обобщённых координат
second_diff_generic_coord = [diff(diff(var, t), t) for var in generic_vars]

# кинетическая энергия сферической оболочки
T_s = 1/2 * M * V_O.T * V_O + 1/2 * (J_s * Matrix([[p_s], [q_s], [r_s]])).T * Matrix([[p_s], [q_s], [r_s]])

# кинетическа энергия платформы
T_p = 1/2 * M_p * V_C.T * V_C + 1/2 * (J_p * Matrix([[p_p], [q_p], [r_s]])).T * Matrix([[p_p], [q_p], [r_s]])

# кинетическая энергия колеса
T_w = 1/2 * m * V_B.T * V_B + 1/2 * (J_w * Matrix([[p_w], [q_w], [r_w]])).T * Matrix([[p_w], [q_w], [r_w]])

# кинетическая энергия системы
T = T_s + T_p + T_w

# силовая функция силы тяжести для колеса
U_w = m * g * P_x_X * Matrix([[0], [0], [-l]])

# силовая функция силы тяжести для платформы
U_p = M_p * g * P_x_X * Matrix([[C_mx], [C_my], [C_mz]])

# обобщённые силы
Q_x = 0
Q_y = 0
Q_α = diff(U_w, x1) + diff(U_p, x1)
Q_β = diff(U_w, x2) + diff(U_p, x2)
Q_γ = diff(U_w, x3) + diff(U_p, x3)
Q_φ = M_φ
Q_ψ = M_ψ
Q_δ = diff(U_w, x6) + diff(U_p, x6)
Q_ε = diff(U_w, x7) + diff(U_p, x7)
Q_τ = diff(U_w, x8) + diff(U_p, x8)

# Получаем матрицу для неголономных связей
B = build_matrix().T

# динамические уравнения
Eq1 = diff(diff(T, diff(x, t)), t)[0] - diff(T, x)[0] - Q_x - (B.row(0) * λ)[0]
Eq2 = diff(diff(T, diff(y, t)), t)[0] - diff(T, y)[0] - Q_y - (B.row(1) * λ)[0]
Eq3 = diff(diff(T, x1), diff(x1, t))[0] - diff(T, x1)[0] - Q_α[0] - (B.row(2) * λ)[0]
Eq4 = diff(diff(T, x2), diff(x2, t))[0] - diff(T, x2)[0] - Q_β[0] - (B.row(3) * λ)[0]
Eq5 = diff(diff(T, x3), diff(x3, t))[0] - diff(T, x3)[0] - Q_γ[0] - (B.row(4) * λ)[0]
Eq6 = diff(diff(T, x4), diff(x4, t))[0] - diff(T, x4)[0] - Q_φ - (B.row(5) * λ)[0]
Eq7 = diff(diff(T, x5), diff(x5, t))[0] - diff(T, x5)[0] - Q_ψ - (B.row(6) * λ)[0]
Eq8 = diff(diff(T, x6), diff(x6, t))[0] - diff(T, x6)[0] - Q_δ[0] - (B.row(7) * λ)[0]
Eq9 = diff(diff(T, x7), diff(x7, t))[0] - diff(T, x7)[0] - Q_ε[0] - (B.row(8) * λ)[0]
Eq10 = diff(diff(T, x8), diff(x8, t))[0] - diff(T, x8)[0] - Q_τ[0] - (B.row(9) * λ)[0]

equations = [Eq1, Eq2, Eq3, Eq4, Eq5, Eq6, Eq7, Eq8, Eq9, Eq10]

def get_row_coef_before_second_diff(equation):
    row = Matrix([range(size_generic_vars)])
    for second_diff in second_diff_generic_coord:
        coeff = trigsimp(
            collect(
                expand(equation), second_diff
            ).coeff(second_diff)
        )
        position = second_diff_generic_coord.index(second_diff, 0, len(second_diff_generic_coord))

        print(str(second_diff) + ": " + str(coeff))
        row[position] = coeff
    return row

def build_Matrix(equations):
    A = Matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    i = 0
    for equation in equations:
        i = i + 1
        print("equation #" + str(i))
        row = get_row_coef_before_second_diff(equation)
        A = A.row_insert(equations.index(equation, 0, len(equations)) + 1, row)
        print("--------------------")
    A.row_del(0)
    return A

