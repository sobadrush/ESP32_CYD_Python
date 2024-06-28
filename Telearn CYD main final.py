from cyd_telearn import CYD_Telearn
import time
import random

cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

# 定義按鈕文本
button_texts = ["Circle", "Star", "Exit"]

# 顯示按鈕
y = 40
cyd_telearn.display_text("Please choose a shape:", 10, 20, cyd_telearn.colors["YELLOW"])
for text in button_texts:
    cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
    cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
    y += 40

while True:
    choice = cyd_telearn.check_menu_touch(len(button_texts))
    cyd_telearn.clear_screen()
    if choice == 3:
        cyd_telearn.shutdown()

    elif choice == 1:
        cyd_telearn.clear_screen()
        cyd_telearn.display_text("TOUCH ME", cyd_telearn.cyd.display.width // 2 - 32, 10, cyd_telearn.colors["WHITE"])

        # List of color choices
        colors = [cyd_telearn.colors["RED"], cyd_telearn.colors["GREEN"], cyd_telearn.colors["BLUE"]]
        c = 0  # Initial color choice
        r = 5  # Radius of circles
        cyd_telearn.fill_rectangle(220, 300, 20, 20, cyd_telearn.colors["BLUE"])
        while True:
            time.sleep(0.05)
            x, y = cyd_telearn.touches()

            if x == 0 and y == 0:
                continue

            x, y = cyd_telearn.touch_to_display(x, y)
            
            if x > 220 and y > 300:
                break

            print("Touches:", x, y)

            # Prevent circles from appearing off-screen.
            y = min(max(y, r + 1), cyd_telearn.height - (r + 1))
            x = min(max(x, r + 1), cyd_telearn.width - (r + 1))

            # Create circle
            cyd_telearn.fill_circle(x, y, r, colors[c])

            c = (c + 1) % len(colors)

    elif choice == 2:
        cyd_telearn.clear_screen()
        cyd_telearn.display_text("TOUCH ME", cyd_telearn.cyd.display.width // 2 - 32, 10, cyd_telearn.colors["WHITE"])

        # List of color choices
        colors = [cyd_telearn.colors["RED"], cyd_telearn.colors["GREEN"], cyd_telearn.colors["BLUE"]]
        c = 0  # Initial color choice
        r = 10  # Radius of circles
        cyd_telearn.fill_rectangle(220, 300, 20, 20, cyd_telearn.colors["BLUE"])
        while True:
            time.sleep(0.05)
            x, y = cyd_telearn.touches()

            if x == 0 and y == 0:
                continue

            x, y = cyd_telearn.touch_to_display(x, y)

            if x > 220 and y > 300:
                break

            print("Touches:", x, y)

            # Prevent circles from appearing off-screen.
            y = min(max(y, r + 1), cyd_telearn.height - (r + 1))
            x = min(max(x, r + 1), cyd_telearn.width - (r + 1))

            # Create circle
            cyd_telearn.fill_star(x, y, r, colors[c])

            c = (c + 1) % len(colors)

    
    # 重新顯示按鈕
    cyd_telearn.clear_screen()
    y = 40
    cyd_telearn.display_text("Please choose a shape:", 10, 20, cyd_telearn.colors["YELLOW"])
    for text in button_texts:
        cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
        cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
        y += 40
