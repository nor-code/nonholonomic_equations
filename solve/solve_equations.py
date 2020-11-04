from Dynamics import *

for link in nonholonomic_links:
    print(link.subs([(r, 0.02), (R, 0.09)]))

for eq in equations:
    print(eq.subs([(r, 0.02),
                   (R, 0.09),
                   (J_px, 1),
                   (J_py, 1),
                   (J_pz, 1),
                   (J_wx, 1),
                   (J_wy, 1),
                   (J_wz, 1),
                   (M_p, 0.2),
                   (M, 0.05),
                   (m, 0.05),
                   (g, 10),
                   (C_mx, 0),
                   (C_my, 0),
                   (C_mz, -0.07),
                   (C_Mx, 0),
                   (C_My, 0),
                   (C_Mz, -0.03)]
                  )
          )
    
