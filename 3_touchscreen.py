from cyd_telearn import CYD_Telearn
import time


cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()
cyd_telearn.display_text("TOUCH ME", cyd_telearn.cyd.display.width // 2 - 32, 10, cyd_telearn.colors["WHITE"])

# List of color choices
colors = [cyd_telearn.colors["RED"], cyd_telearn.colors["GREEN"], cyd_telearn.colors["BLUE"]]
c = 0  # Initial color choice
r = 4  # Radius of circles

while True:
    time.sleep(0.05)
    x, y = cyd_telearn.touches()

    if x == 0 and y == 0:
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

    c = (c + 1) % len(colors)

cyd_telearn.shutdown()
