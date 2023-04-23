from sympy import Symbol, Matrix

# ускорение свободного падения
g = Symbol('g')

# радиус сферической оболочки
R = Symbol('R')  # 0.081 m or 16.2 cm diametr

# радиус колесика
r = Symbol('r')  # 0.026

# радиус платформы
R_p = Symbol('R_p')

# расстояние от т.O до т.B
l: Symbol = Symbol('l')

# расстояние от т.O до т. P
# TODO изменить на C_Mz
l_p: Symbol = Symbol('l_p')  # центр платформы
l_w: Symbol = Symbol('l_w')  # центр колеса

# масса сферической оболочки
M = Symbol('M')  # 137.5 g ()

# масса платформы с установленными на ней приборами
M_p = Symbol('M_p')  # 656 g

# масса колеса
m = Symbol('m')  # 0.05

# константы, появлющиеся, когда возникает смещение ц.м. вычисляются непосредственно перед решением диффуров
sin_x20 = Symbol('sin_x20')
cos_x20 = Symbol('cos_x20')
sin_x30 = Symbol('sin_x30')
cos_x30 = Symbol('cos_x30')
sin_x70 = Symbol('sin_x70')
cos_x70 = Symbol('cos_x70')
sin_x80 = Symbol('sin_x80')
cos_x80 = Symbol('cos_x80')

# координаты ц.м. платформы по оси O_x1 , O_x2 и O_x3
C_Mx = Symbol('C_Mx')
C_My = Symbol('C_My')
C_Mz = Symbol('C_Mz')

# координаты ц.м. колеса по оси O_x1, O_x2 и O_x3
C_mx = Symbol('C_mx')
C_my = Symbol('C_my')
C_mz = Symbol('C_mz')

# радиус-вектор центра масс платформы в с.к. C_x1_x2_x3
R_cm_p = Matrix([[C_Mx],
                 [C_My],
                 [C_Mz]])

# радиус-вектор центра масс колеса в с.к. C_x1_x2_x3
R_cm_w = Matrix([[0],
                 [0],
                 [C_mz]])

# моменты инерции платформы относитльно главных осей инерции
J_px = Symbol('J_px')
J_py = Symbol('J_py')
J_pz = Symbol('J_pz') # Symbol('J_pz')

# моменты инерции колеса относитльно главных осей инерции
J_wx = Symbol('J_wx')
J_wy = Symbol('J_wy')
J_wz = Symbol('J_wz')

# тензор инерции для сферической оболочки
J_s = Matrix([[2 / 3 * M * R ** 2, 0, 0],
              [0, 2 / 3 * M * R ** 2, 0],
              [0, 0, 2 / 3 * M * R ** 2]])

# тензор инерции для платформы
J_p = Matrix([[J_px, 0, 0],
              [0, J_py, 0],
              [0, 0, J_pz]])

# тензор инерции колеса
J_w = Matrix([[J_wx, 0, 0],
              [0, J_wy, 0],
              [0, 0, J_wz]])

# J_w = Matrix([[m * r**2/4 + m * l**2, 0,                     0],
#               [0,                     m * r**2/2 + m * l**2, 0],
#               [0,                     0,                     m * r**2/4]])
