from cyd_telearn import CYD_Telearn
import time

cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

# 繪製緩慢的圖形
cyd_telearn.draw_square_slowly(20, 20, 50, color = cyd_telearn.colors["RED"], delay = 0.02)
time.sleep(2)
cyd_telearn.clear_screen()

cyd_telearn.draw_circle_slowly(120, 120, 40, cyd_telearn.colors["GREEN"], 0.03)
time.sleep(2)
cyd_telearn.clear_screen()

cyd_telearn.draw_star_slowly(120, 120, 50, cyd_telearn.colors["BROWN"])
time.sleep(2)
cyd_telearn.clear_screen()

cyd_telearn.draw_triangle_slowly(60, 180, 180, 180, 120, 60, cyd_telearn.colors["YELLOW"], 0.02)
time.sleep(2)
cyd_telearn.clear_screen()

cyd_telearn.shutdown()
