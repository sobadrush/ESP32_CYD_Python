from cyd_telearn import CYD_Telearn
import random
import time

# 建立 CYD_Telearn Class
cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

x = cyd_telearn.width // 2
y = cyd_telearn.height // 2
radius = 2
increment = 3
start_angle = 0
change_angle = 30
colors = [cyd_telearn.colors["RED"], cyd_telearn.colors["ORANGE"], cyd_telearn.colors["YELLOW"],cyd_telearn.colors["GREEN"],cyd_telearn.colors["BLUE"],cyd_telearn.colors["PURPLE"]]

# 繪製圓形圖案
cyd_telearn.draw_circle_pattern(x, y, radius, increment, start_angle, change_angle, colors, color_index=0, speed=0.001)

# 關閉螢幕
cyd_telearn.shutdown()
