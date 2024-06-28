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