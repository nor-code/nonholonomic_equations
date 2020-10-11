from Kinematics import *

# кинетическая энергия сферической оболочки
T_s = 1/2 * M * V_O.T * V_O + 1/2 * (J_s * Matrix([[p_s], [q_s], [r_s]])).T * Matrix([[p_s], [q_s], [r_s]])

# кинетическа энергия платформы
T_p = 1/2 * M_p * V_C.T * V_C + 1/2 * (J_p * Matrix([[p_p], [q_p], [r_s]])).T * Matrix([[p_p], [q_p], [r_s]])

# кинетическая энергия колеса
T_w = 1/2 * m * V_B.T * V_B + 1/2 * (J_w * Matrix([[p_w], [q_w], [r_w]])).T * Matrix([[p_w], [q_w], [r_w]])

