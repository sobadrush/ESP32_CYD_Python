from cyd_telearn import CYD_Telearn
import time

cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

# 定義按鈕文本
button_texts = [ "Show Text", "Draw Shapes", "Exit" ]
cyd_telearn.display_text("Please choose a button:", 10, 20, cyd_telearn.colors["YELLOW"])

print(f"top_menu_y : { cyd_telearn.top_menu_y }")

# 顯示按鈕
y = cyd_telearn.top_menu_y # 要固定為 40

for text in button_texts:
    cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
    cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
    y += cyd_telearn.top_menu_y

while True:
    choice = cyd_telearn.check_menu_touch(len(button_texts))
    cyd_telearn.clear_screen()
    
    if choice == 1:
        cyd_telearn.display_text("Hello World!", 10, 50)
        time.sleep(2)
    elif choice == 2:
        cyd_telearn.draw_rectangle(20, 20, 100, 60, cyd_telearn.colors["RED"])
        cyd_telearn.fill_rectangle(140, 20, 100, 60, cyd_telearn.colors["GREEN"])
        cyd_telearn.draw_circle(70, 150, 30, cyd_telearn.colors["BLUE"])
        cyd_telearn.fill_circle(190, 150, 30, cyd_telearn.colors["YELLOW"])
        cyd_telearn.draw_triangle(50, 220, 20, 260, 80, 260, cyd_telearn.colors["PINK"])
        cyd_telearn.fill_triangle(150, 220, 120, 260, 180, 260, cyd_telearn.colors["ORANGE"])
        time.sleep(2)
    elif choice == 3:
        cyd_telearn.shutdown()
        break
    
    # 重新顯示按鈕
    cyd_telearn.clear_screen()
    y = cyd_telearn.top_menu_y # 要固定為40
    for text in button_texts:
        cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
        cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
        y += cyd_telearn.top_menu_y
