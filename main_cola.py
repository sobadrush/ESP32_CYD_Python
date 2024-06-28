from cyd_telearn import CYD_Telearn
import time
import random

cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

###########################################

# 定義按鈕文本
button_texts = ["Circle", "Star", "Exit"]

# 顯示按鈕
y = 40
cyd_telearn.display_text("Please choose a shape:", 10, 20, cyd_telearn.colors["YELLOW"])
for text in button_texts:
    cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
    cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
    y += 40

###########################################

while True:
    choice = cyd_telearn.check_menu_touch(len(button_texts))
    print(f"choice = {choice}")
    
    if choice == 3:
        cyd_telearn.shutdown()
        
        
    elif choice == 1:
        print("選擇 Circle")
        cyd_telearn.clear_screen()
        
        # List of color choices
        colors = [cyd_telearn.colors["RED"], cyd_telearn.colors["GREEN"], cyd_telearn.colors["BLUE"]]
        c = 0  # Initial color choice
        r = 5  # Radius of circles
        
        # 右下角畫一個小正方形，當作離開標記
        cyd_telearn.fill_rectangle(220, 300, 20, 20, cyd_telearn.colors["BLUE"])
        
        while True:
            time.sleep(0.05)
            x, y = cyd_telearn.touches()

            if x == 0 and y == 0: # 若螢幕沒有被「觸控」，x 及 y 都會是 0, 不做任何事
                continue

            x, y = cyd_telearn.touch_to_display(x, y)
            print("Touches:", x, y)
            
            if x > 220 and y > 300:
                print(f"Click Exit Button, escape while loop.")
                break

            # Prevent circles from appearing off-screen.
            y = min(max(y, r + 1), cyd_telearn.height - (r + 1))
            x = min(max(x, r + 1), cyd_telearn.width - (r + 1))

            # Create circle
            cyd_telearn.fill_circle(x, y, r, colors[c])
            cyd_telearn.fill_rectangle(x, y, 10, 10, colors[c])
            
            c = (c + 1) % len(colors) # index 是 0,1,2，除以多少會是 0,1,2 ?
        
        
    elif choice == 2:
        print("選擇 Star")
        
        cyd_telearn.clear_screen()
        
        # List of color choices
        colors = [cyd_telearn.colors["RED"], cyd_telearn.colors["GREEN"], cyd_telearn.colors["BLUE"]]
        c = 0  # Initial color choice
        r = 5  # Radius of circles
        
        # 右下角畫一個小正方形，當作離開標記
        cyd_telearn.fill_rectangle(220, 300, 20, 20, cyd_telearn.colors["BLUE"])
        
        while True:
            time.sleep(0.05)
            x, y = cyd_telearn.touches()

            if x == 0 and y == 0: # 若螢幕沒有被「觸控」，x 及 y 都會是 0, 不做任何事
                continue

            x, y = cyd_telearn.touch_to_display(x, y)
            print("Touches:", x, y)
            
            if x > 220 and y > 300:
                print(f"Click Exit Button, escape while loop.")
                break

            # Prevent circles from appearing off-screen.
            y = min(max(y, r + 1), cyd_telearn.height - (r + 1))
            x = min(max(x, r + 1), cyd_telearn.width - (r + 1))

            # Create circle
            cyd_telearn.draw_star(x, y, 15, colors[c])

            c = (c + 1) % len(colors) # index 是 0,1,2，除以多少會是 0,1,2 ?
        
            
    # 重新顯示選單按鈕
    y = 40
    cyd_telearn.display_text("Please choose a shape:", 10, 20, cyd_telearn.colors["YELLOW"])
    for text in button_texts:
        cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
        cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
        y += 40
