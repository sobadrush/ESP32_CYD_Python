from cyd_telearn import CYD_Telearn
import time

cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

print(f">>> 螢幕寬：{ cyd_telearn.width }") # 240
print(f">>> 螢幕高：{ cyd_telearn.height }") # 320

cyd_telearn.display_text("Hello World", 50, 50)

time.sleep(5)

cyd_telearn.shutdown()
