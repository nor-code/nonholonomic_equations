from sympy import Symbol, Matrix

# ускорение свободного падения
g = Symbol('g')

# радиус сферической оболочки
R = Symbol('R')

# радиус колесика
r = Symbol('r')

# расстояние от т.O до т.B
l: Symbol = Symbol('l')

# масса сферической оболочки
M = Symbol('M')

# масса платформы с установленными на ней приборами
M_p = Symbol('M_p')

# масса колеса
m = Symbol('m')

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

# радиус-вектор центра масс платформы в с.к. C_x1_x2_x3
R_cm_w = Matrix([[C_mx],
                 [C_my],
                 [C_mz]])

# моменты инерции платформы относитльно главных осей инерции
J_px = Symbol('J_px')
J_py = Symbol('J_py')
J_pz = Symbol('J_pz')

# моменты инерции колеса относитльно главных осей инерции
J_wx = Symbol('J_wx')
J_wy = Symbol('J_wy')
J_wz = Symbol('J_wz')

# тензор инерции для сферической оболочки
J_s = Matrix([[2/3 * M * R**2,   0,              0],
             [0,                 2/3 * M * R**2, 0],
             [0,                 0,              2/3 * M * R**2]])

# тензор инерции для платформы
J_p = Matrix([[J_px, 0,    0],
              [0,    J_py, 0],
              [0,    0,    J_pz]])

# тензор инерции колеса
J_w = Matrix([[J_wx, 0,     0],
              [0,    J_wy,  0],
              [0,    0,     J_wz]])

# J_w = Matrix([[m * r**2/4 + m * l**2, 0,                     0],
#               [0,                     m * r**2/2 + m * l**2, 0],
#               [0,                     0,                     m * r**2/4]])