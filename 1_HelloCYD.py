from cyd_telearn import CYD_Telearn
import time


cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

text = "Hello, CYD!"

print(f">>> CYD 螢幕寬度: {cyd_telearn.width}")
print(f">>> CYD 螢幕高度: {cyd_telearn.height}")

x = cyd_telearn.width // 2
y = cyd_telearn.height // 2

print(f">>> x 座標: {x}")
print(f">>> y 座標: {y}")

color = cyd_telearn.colors['YELLOW']
cyd_telearn.display_text(text, x, y, color)

time.sleep(5)
cyd_telearn.clear_screen()
cyd_telearn.shutdown()
