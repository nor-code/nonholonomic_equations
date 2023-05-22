import symengine as se
from symengine import function_symbol


a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = se.symbols('a1, a2, a3, a4, a5, a6, a7, a8, a9')
b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9 = se.symbols('b1, b2, b3, b4, b5, b6, b7, b8, b9')
c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9 = se.symbols('c1, c2, c3, c4, c5, c6, c7, c8, c9')
d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9 = se.symbols('d1, d2, d3, d4, d5, d6, d7, d8, d9')
e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9 = se.symbols('e1, e2, e3, e4, e5, e6, e7, e8, e9')

d_phi_bot = se.Symbol('d_phi_bot')
d_del_bot = se.Symbol('d_del_bot')
d_eps_bot = se.Symbol('d_eps_bot')
d_tau_bot = se.Symbol('d_tau_bot')

d_d_phi_bot = se.Symbol('d_d_phi_bot')
d_d_del_bot = se.Symbol('d_d_del_bot')
d_d_eps_bot = se.Symbol('d_d_eps_bot')
d_d_tau_bot = se.Symbol('d_d_tau_bot')

# радиус сферической оболочки
# R = se.Symbol('R')  # 0.081 m or 16.2 cm diametr

# радиус колесика
r = se.Symbol('r')  # 0.026

# радиус платформы
R_p = se.Symbol('R_p')

# масса сферической оболочки
M = se.Symbol('M')  # 137.5 g ()

# масса платформы с установленными на ней приборами
M_p = se.Symbol('M_p')  # 656 g

# масса колеса
m = se.Symbol('m')  # 0.05

# координаты ц.м. платформы по оси O_x1 , O_x2 и O_x3
C_Mx = se.Symbol('C_Mx')
C_My = se.Symbol('C_My')
C_Mz = se.Symbol('C_Mz')

# константы, появлющиеся, когда возникает смещение ц.м. вычисляются непосредственно перед решением диффуров
sin_x20 = se.Symbol('sin_x20')
cos_x20 = se.Symbol('cos_x20')
sin_x30 = se.Symbol('sin_x30')
cos_x30 = se.Symbol('cos_x30')

x20 = se.Symbol('β_')
x30 = se.Symbol('γ_')
x70 = se.Symbol('ε_')
x80 = se.Symbol('τ_')

# координаты ц.м. колеса по оси O_x1, O_x2 и O_x3
C_mz = se.Symbol('C_mz')

timet = se.Symbol("t")
phi = function_symbol("φ", timet)
delta = function_symbol("δ", timet)
eps = function_symbol("ε", timet)
tau = function_symbol("τ", timet)

se_x = function_symbol("x", timet)
se_y = function_symbol("y", timet)
se_alpha = function_symbol("α", timet)
se_beta = function_symbol("β", timet)
se_gama = function_symbol("γ", timet)
se_psi = function_symbol("ψ", timet)