# import Kinematics as k
from definitions.generic_coordinates import *
from sympy import *
from utils.Wolfram import Wolfram
import re

str = 'αβγφψδετ'


if __name__ == "__main__":
    parser = Wolfram()

    print('nds', '=', 'NDSolve[{eq1 == 0, eq2 == 0, eq3 == 0, eq4 == 0, eq5 == 0,',
          ' eq6 == 0, eq7 == 0, eq8 == 0, eq9 == 0, eq10 == 0,',
          ' eq11 == 0, eq12 == 0, eq13 == 0, eq14 == 0, eq15 == 0,',
          'x\'\'[0] == x[0] == 0',
          'y\'\'[0] == y[0] == 0',
          'α\'\'[0] == α[0] == 0',
          'β\'\'[0] == β[0] == 0',
          'γ\'\'[0] == γ[0] == 0',
          'φ\'\'[0] == φ[0] == 0',
          'ψ\'\'[0] == ψ[0] == 0',
          'δ\'\'[0] == δ[0] == 0',
          'ε\'\'[0] == ε[0] == 0',
          'τ\'\'[0] == τ[0] == 0',
          '},',
          '{t, x, y, α, β, γ, φ, ψ, δ, ε, τ, λ1, λ2, λ3, λ4, λ5},'
          ' {t, 0, 5}])')
