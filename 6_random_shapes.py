from cyd_telearn import CYD_Telearn
import random
import time

# 創建 CYD_Telearn 類的實例
cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()
count = 0

while True:
    # 隨機選擇形狀
    shape_type = random.choice(['square', 'circle', 'triangle'])

    # 隨機位置和大小
    x = random.randint(10, cyd_telearn.width - 60)
    y = random.randint(10, cyd_telearn.height - 60)
    size = random.randint(20, 50)

    # 隨機顏色
    color = cyd_telearn.random_color()

    # 根據形狀類型繪製形狀
    if shape_type == 'square':
        cyd_telearn.draw_square_slowly(x, y, size, color)
    elif shape_type == 'circle':
        cyd_telearn.draw_circle_slowly(x + size // 2, y + size // 2, size // 2, color)
    elif shape_type == 'triangle':
        # 計算三角形的三個頂點
        x1, y1 = x, y
        x2, y2 = x + size, y
        x3, y3 = x + size // 2, y - int(size * 0.866)  # 等邊三角形的高度
        cyd_telearn.draw_triangle_slowly(x1, y1, x2, y2, x3, y3, color)
    count+=1
    if count >= 30:
        break
    # 等待一秒鐘再繪製下一個形狀
    time.sleep(0.5)

cyd_telearn.shutdown()
