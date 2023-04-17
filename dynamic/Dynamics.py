from utils.common import *
from Kinematics import *
from definitions.moments import *
from definitions.lagrangian_multipliers import *
import time
from sympy.solvers.solveset import linsolve, linear_eq_to_matrix
from utils.Wolfram import Wolfram
from utils.to_sympy_expression import transform_to_simpy
from sympy import expand
from utils.latex_converter import print_in_latex

t0 = time.time()
# кинетическая энергия сферической оболочки
T_s = 1 / 2 * M * V_O.T * V_O + 1 / 2 * (J_s * Matrix([[p_s], [q_s], [r_s]])).T * Matrix([[p_s], [q_s], [r_s]])
print("T_s = ", print_in_latex(T_s))
# кинетическа энергия платформы
# в с.к. O_x1_x2_x3
T_p = 1 / 2 * M_p * V_C.T * V_C + 1 / 2 * (J_p * Matrix([[p_p], [q_p], [r_p]])).T * Matrix([[p_p], [q_p], [r_p]])
print("T_p = ", print_in_latex(T_p))
# кинетическая энергия колеса
# в с.к. O_x1_x2_x3
T_w = 1 / 2 * m * V_B.T * V_B + 1 / 2 * (J_w * Matrix([[p_w], [q_w], [r_w]])).T * Matrix([[p_w], [q_w], [r_w]])
print("T_w = ", print_in_latex(T_w))
# кинетическая энергия системы
T = T_s + T_p + T_w

# силовая функция силы тяжести для платформы
U_p = - (M_p * g) * (R - (P_x_X * R_cm_p)[2])  # Matrix([[0], [0], [C_Mz]])

# силовая функция силы тяжести для колеса
U_w = - (m * g) * (R - (P_x_X * R_cm_w)[2])  # Matrix([[0], [0], [C_mz]])
print(print_in_latex(U_w))

# обобщённые силы
Q_x = 0  # diff(U_w, x) + diff(U_p, x)
Q_y = 0  # diff(U_w, y) + diff(U_p, y)
Q_α = diff(U_w, x1) + diff(U_p, x1)
Q_β = diff(U_w, x2) + diff(U_p, x2)
Q_γ = diff(U_w, x3) + diff(U_p, x3)
Q_φ = 0 #M_φ  # P_x_X * Matrix([[M_φ * cos(x5)], [M_φ * sin(x5)], [0]])
Q_ψ = 0 #M_ψ  # P_x_X * Matrix([[0], [0], [M_ψ]])
Q_δ = diff(U_w, x6) + diff(U_p, x6)
Q_ε = diff(U_w, x7) + diff(U_p, x7)
Q_τ = diff(U_w, x8) + diff(U_p, x8)

print("q delta ", Q_δ)
print("q eps   ", Q_ε)
print("q tau   ", Q_τ)

# Получаем матрицу для неголономных связей
B = build_matrix().T
t1 = time.time()
print("t1 - t0 = ", (t1 - t0)/60, " min")

# динамические уравнения
Eq1 = diff(diff(T, diff(x, t)), t)[0] - diff(T, x)[0] - Q_x - (B.row(0) * λ)[0]
print("Eq1 = ", print_in_latex(Eq1))
Eq2 = diff(diff(T, diff(y, t)), t)[0] - diff(T, y)[0] - Q_y - (B.row(1) * λ)[0]
print("Eq2 = ", print_in_latex(Eq2))
Eq3 = diff(diff(T, diff(x1, t)), t)[0] - diff(T, x1)[0] - Q_α - (B.row(2) * λ)[0]
print("Eq3 = ", print_in_latex(Eq3))
Eq4 = diff(diff(T, diff(x2, t)), t)[0] - diff(T, x2)[0] - Q_β - (B.row(3) * λ)[0]
print("Eq4 = ", print_in_latex(Eq4))
Eq5 = diff(diff(T, diff(x3, t)), t)[0] - diff(T, x3)[0] - Q_γ - (B.row(4) * λ)[0]
print("Eq5 = ", print_in_latex(Eq5))
Eq6 = diff(diff(T, diff(x4, t)), t)[0] - diff(T, x4)[0] - Q_φ - (B.row(5) * λ)[0]
print("Eq6 = ", print_in_latex(Eq6))
Eq7 = diff(diff(T, diff(x5, t)), t)[0] - diff(T, x5)[0] - Q_ψ - (B.row(6) * λ)[0]
print("Eq7 = ", print_in_latex(Eq7))
Eq8 = diff(diff(T, diff(x6, t)), t)[0] - diff(T, x6)[0] - Q_δ - (B.row(7) * λ)[0]
print("Eq8 = ", print_in_latex(Eq8))
Eq9 = diff(diff(T, diff(x7, t)), t)[0] - diff(T, x7)[0] - Q_ε - (B.row(8) * λ)[0]
print("Eq9 = ", print_in_latex(Eq9))
Eq10 = diff(diff(T, diff(x8, t)), t)[0] - diff(T, x8)[0] - Q_τ - (B.row(9) * λ)[0]
print("Eq10 = ", print_in_latex(Eq10))

equations = [Eq1, Eq2, Eq3, Eq4, Eq5, Eq6, Eq7, Eq8, Eq9, Eq10]
ORDER = 2
for i in range(len(equations)):
    with open('./dynamic/eq' + str(i + 1) + '.txt', 'w') as eq_i:
        eq_i_simplified = remove_required_and_above_smallness_from_expression(
            simplification_expression(expand(equations[i], deep=True)),
            order=ORDER
        )
        print(i, " = ", eq_i_simplified)
        eq_i.write(transform_to_simpy(str(simplify(eq_i_simplified, rational=True))))


print("Eq1 ", expand(Eq1))
print("Eq2 ", Eq2)
print("Eq3 ", Eq3)
print("Eq4 ", Eq4)
print("Eq5 ", Eq5)
print("Eq7 ", Eq7)

print("\n-----------------\n")

print("Eq6", Eq6)
print("Eq8", Eq8)
print("Eq9", Eq9)
print("Eq10", Eq10)


equations = [Eq1, Eq2, Eq3, Eq4, Eq5, Eq6, Eq7, Eq8, Eq9, Eq10]
print("eq 1: ", - (B.row(0) * λ)[0])
print("eq 1: ", - Q_x, "\n")

print("eq 2: ", - (B.row(1) * λ)[0])
print("eq 2: ", - Q_y, "\n")

print("eq 3: ", - (B.row(2) * λ)[0])
print("eq 3: ", - Q_α, "\n")

print("eq 4: ", - (B.row(3) * λ)[0])
print("eq 4: ", - Q_β, "\n")

print("eq 5: ", - (B.row(4) * λ)[0])
print("eq 5: ", Q_γ, "\n")

print("eq 6: ", - (B.row(5) * λ)[0])
print("eq 6: ", Q_φ, "\n")

print("eq 7: ", - (B.row(6) * λ)[0])
print("eq 7: ", Q_ψ, "\n")

print("eq 8: ", - (B.row(7) * λ)[0])
print("eq 8: ", Q_δ, "\n")

print("eq 9: ", - (B.row(8) * λ)[0])
print("eq 9: ", Q_ε, "\n")

print("eq 10: ", - (B.row(9) * λ)[0])
print("eq 10: ", Q_τ, "\n")

print("____________EQUATIONS_____________")
for eq in equations:
    print(eq, " \n")

def get_row_coef_before_second_diff(equation):
    row = Matrix([range(size_generic_vars)])
    parser = Wolfram()

    total_result = ""
    for second_diff in second_diff_generic_coord:
        coeff = collect(
            expand(equation, deep=True), second_diff
        ).coeff(second_diff) * second_diff

        position = second_diff_generic_coord.index(second_diff, 0, len(second_diff_generic_coord))

        wolfram_coef = parser.transformForWolframMathematica(str(coeff))

        total_result = total_result + " + " + wolfram_coef
        print(str(second_diff) + ": " + wolfram_coef)
        row[position] = coeff

    print("row: ", total_result)
    return row


def build_Matrix_A(equations):
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


def get_row_coeff_diff_mixed_coef(equation):
    parser = Wolfram()
    result = ""
    for mixed_diff in mixed_diff_of_generic_coordinates:
        coeff = trigsimp(
            collect(
                expand(equation), mixed_diff
            ).coeff(mixed_diff)
        ) * mixed_diff
        wolfram_coef = parser.transformForWolframMathematica(str(coeff))
        result += " + " + wolfram_coef
        print(str(mixed_diff) + ": " + wolfram_coef)
    print(result)

def print_equations_for_Wolfram_Mathematica():
    parser = Wolfram()

    qq = Matrix([[diff(x, t)], [diff(y, t)], [diff(x1, t)],
                 [diff(x2, t)], [diff(x3, t)], [diff(x4, t)],
                 [diff(x5, t)], [diff(x6, t)], [diff(x7, t)],
                 [diff(x8, t)]])

    ll = [
        (B.T.row(0) * qq)[0],
        (B.T.row(1) * qq)[0],
        (B.T.row(2) * qq)[0],
        (B.T.row(3) * qq)[0],
        (B.T.row(4) * qq)[0]
    ]
    i = 1
    for eq in equations:
        result = parser.transformForWolframMathematica(str(eq))
        print('eq' + str(i), ' = ', result + ';')
        i = i + 1

    for eq in ll:
        result = parser.transformForWolframMathematica(str(eq))
        print('eq' + str(i), ' = ', result + ';')
        i = i + 1

    print('nds', '=', 'First[NDSolve[{eq1 == 0, eq2 == 0, eq3 == 0, eq4 == 0, eq5 == 0,',
          ' eq6 == 0, eq7 == 0, eq8 == 0, eq9 == 0, eq10 == 0,',
          ' eq11 == 0, eq12 == 0, eq13 == 0, eq14 == 0, eq15 == 0,',
          'x[0] == 0, x\'[0] == 0,',
          'y[0] == 0, y\'[0] == 0,',
          'α[0] == 0, α\'[0] == 0,',
          'β[0] == 0, β\'[0] == 0,',
          'γ[0] == 0, γ\'[0] == 0,',
          'φ[0] == 0, φ\'[0] == 0,',
          'ψ[0] == 0, ψ\'[0] == 0,',
          'δ[0] == 0, δ\'[0] == 0,',
          'ε[0] == 0, ε\'[0] == 0,',
          'τ[0] == 0, τ\'[0] == 0',
          '},',
          '{t, x, y, α, β, γ, φ, ψ, δ, ε, τ, λ1, λ2, λ3, λ4, λ5},'
          ' {t, 0, 5}, '
          'Method -> {"IndexReduction" -> {Automatic, "ConstraintMethod" -> None}}, MaxSteps -> \[Infinity]]]')

    print('Plot[{x[t], x\'[t]} /. nds, {t, 0, 5}, PlotStyle -> {Thickness[0.001], RGBColor[0, 0, 0]}]')
    print('ParametricPlot[Evaluate[{x[t], y[t]} /. nds], {t, 0, 5}, PlotRange -> All]')
    print('Plot[Evaluate[{x[t]} /. nds], {t, 0, 5}, PlotRange -> All]')
    print('Plot[Evaluate[{y[t]} /. nds], {t, 0, 5}, PlotRange -> All]')