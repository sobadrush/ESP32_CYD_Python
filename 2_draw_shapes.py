from cyd_telearn import CYD_Telearn
import time

cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

# 繪製和填充矩形
# cyd_telearn.draw_rectangle(20, 20, 100, 60, cyd_telearn.colors["RED"])
# cyd_telearn.fill_rectangle(140, 20, 100, 60, cyd_telearn.colors["GREEN"])

# 繪製和填充圓形
# cyd_telearn.draw_circle(70, 150, 30, cyd_telearn.colors["BLUE"])
# cyd_telearn.fill_circle(190, 150, 30, cyd_telearn.colors["YELLOW"])

# 繪製和填充三角形
# cyd_telearn.draw_triangle(50, 220, 20, 260, 80, 260, cyd_telearn.colors["PINK"])
# cyd_telearn.fill_triangle(150, 220, 120, 260, 180, 260, cyd_telearn.colors["ORANGE"])

# 繪製和填充星形
cyd_telearn.draw_star(20, 20, 15, cyd_telearn.colors["BLUE"])
cyd_telearn.fill_star(70, 30, 30, cyd_telearn.colors["PINK"])

time.sleep(5)
cyd_telearn.shutdown()

