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
        
        while True:
            time.sleep(0.05)
            x, y = cyd_telearn.touches()

            if x == 0 and y == 0: # 若螢幕沒有被「觸控」，x 及 y 都會是 0, 不做任何事
                continue

            x, y = cyd_telearn.touch_to_display(x, y)

            # Double tap to exit
            if cyd_telearn.double_tap(x, y):
                break

            print("Touches:", x, y)

            # Prevent circles from appearing off-screen.
            y = min(max(y, r + 1), cyd_telearn.height - (r + 1))
            x = min(max(x, r + 1), cyd_telearn.width - (r + 1))

            # Create circle
            cyd_telearn.fill_circle(x, y, r, colors[c])
            cyd_telearn.fill_rectangle(x, y, 10, 10, colors[c])
            
            c = (c + 1) % len(colors) # index 是 0,1,2，除以多少會是 0,1,2 ?
        
        
    elif choice == 2:
        print("選擇 Star")
        