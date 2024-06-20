from cydr import CYD
import time
import math
import random

class CYD_Telearn:
    def __init__(self):
        self.cyd = CYD()
        self.colors = {
            "BLACK": self.color565(0, 0, 0),
            "RED": self.color565(255, 0, 0),
            "GREEN": self.color565(0, 255, 0),
            "CYAN": self.color565(0, 255, 255),
            "BLUE": self.color565(0, 0, 255),
            "PURPLE": self.color565(255, 0, 255),
            "WHITE": self.color565(255, 255, 255),
            "ORANGE": self.color565(255, 165, 0),
            "YELLOW": self.color565(255, 255, 0),
            "PINK": self.color565(255, 192, 203),
            "BROWN": self.color565(165, 42, 42)
        }
        self.width = self.cyd.display.width
        self.height = self.cyd.display.height
        self.current_color_index = 0

    def color565(self, r, g, b):
        """Convert RGB888 to RGB565"""
        return ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)

    def draw_pixel(self, x, y, color):
        self.cyd.display.draw_pixel(x, y, color)

    def draw_line(self, x1, y1, x2, y2, color):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.draw_pixel(x1, y1, color)
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def draw_triangle(self, x1, y1, x2, y2, x3, y3, color):
        self.draw_line(x1, y1, x2, y2, color)
        self.draw_line(x2, y2, x3, y3, color)
        self.draw_line(x3, y3, x1, y1, color)

    def fill_triangle(self, x1, y1, x2, y2, x3, y3, color):
        def draw_line_y(x0, y0, x1, y1):
            if y0 > y1:
                y0, y1, x0, x1 = y1, y0, x1, x0
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            sx = 1 if x0 < x1 else -1
            sy = 1 if y0 < y1 else -1
            err = dx - dy

            while y0 <= y1:
                self.draw_pixel(x0, y0, color)
                e2 = err * 2
                if e2 > -dy:
                    err -= dy
                    x0 += sx
                if e2 < dx:
                    err += dx
                    y0 += sy

        def edge_function(x0, y0, x1, y1, x2, y2):
            return (y2 - y1) * (x0 - x1) - (x2 - x1) * (y0 - y1)

        def barycentric(p, a, b, c):
            w0 = edge_function(p[0], p[1], b[0], b[1], c[0], c[1])
            w1 = edge_function(p[0], p[1], c[0], c[1], a[0], a[1])
            w2 = edge_function(p[0], p[1], a[0], a[1], b[0], b[1])
            return w0, w1, w2

        def inside_triangle(p, a, b, c):
            w0, w1, w2 = barycentric(p, a, b, c)
            return w0 >= 0 and w1 >= 0 and w2 >= 0

        min_x = min(x1, x2, x3)
        max_x = max(x1, x2, x3)
        min_y = min(y1, y2, y3)
        max_y = max(y1, y2, y3)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if inside_triangle((x, y), (x1, y1), (x2, y2), (x3, y3)):
                    self.draw_pixel(x, y, color)

    def touch_to_display(self, x, y):
        """Convert touch coordinates to display coordinates"""
        display_x = min(max((self.cyd.display.width - 1) - x, 0), self.cyd.display.width - 1)
        display_y = min(max((self.cyd.display.height - 1) - y, 0), self.cyd.display.height - 1)
        return display_x, display_y

    def touch_draw(self):
        self.clear_screen()
        last_x = last_y = None

        while True:
            x, y = self.cyd.touches()
            if x == 0 and y == 0:
                continue

            x, y = self.touch_to_display(x, y)

            if last_x is not None and last_y is not None:
                self.draw_line(last_x, last_y, x, y, self.random_color())

            last_x, last_y = x, y

            if self.cyd.button_boot():  # Check if the boot button is pressed to exit
                print("Boot button pressed. Exiting.")
                break

    def random_color(self):
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        return self.colors[list(self.colors.keys())[self.current_color_index]]
    
    def touches(self):
        return self.cyd.touches()
    
    def double_tap(self,x, y):
        return self.cyd.double_tap(x, y)
    # 顯示文字功能
    def display_text(self, text, x=10, y=10, color=None):
        if color is None:
            color = self.colors["WHITE"]
        self.cyd.display.draw_text8x8(x, y, text, color)

    # 繪製和填充形狀的函數
    def draw_rectangle(self, x, y, w, h, color):
        self.cyd.display.draw_rectangle(x, y, w, h, color)

    def fill_rectangle(self, x, y, w, h, color):
        self.cyd.display.fill_rectangle(x, y, w, h, color)

    def draw_circle(self, x, y, r, color):
        self.cyd.display.draw_circle(x, y, r, color)

    def fill_circle(self, x, y, r, color):
        self.cyd.display.fill_circle(x, y, r, color)
    def draw_star(self, x_center, y_center, radius, color):
        points = []
        for i in range(5):
            outer_angle = math.radians(i * 72 - 90)  # Start from the top
            inner_angle = math.radians(i * 72 + 36 - 90)  # Adjust to inner point
            outer_x = x_center + radius * math.cos(outer_angle)
            outer_y = y_center + radius * math.sin(outer_angle)
            inner_x = x_center + (radius / 2.5) * math.cos(inner_angle)
            inner_y = y_center + (radius / 2.5) * math.sin(inner_angle)
            points.append((outer_x, outer_y))
            points.append((inner_x, inner_y))

        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            self.draw_line(int(x1), int(y1), int(x2), int(y2), color)

    def fill_star(self, x_center, y_center, radius, color):
        points = []
        for i in range(5):
            outer_angle = math.radians(i * 72 - 90)  # Start from the top
            inner_angle = math.radians(i * 72 + 36 - 90)  # Adjust to inner point
            outer_x = x_center + radius * math.cos(outer_angle)
            outer_y = y_center + radius * math.sin(outer_angle)
            inner_x = x_center + (radius / 2.5) * math.cos(inner_angle)
            inner_y = y_center + (radius / 2.5) * math.sin(inner_angle)
            points.append((outer_x, outer_y))
            points.append((inner_x, inner_y))

        # Use a simple fill algorithm
        min_x = int(min([p[0] for p in points]))
        max_x = int(max([p[0] for p in points]))
        min_y = int(min([p[1] for p in points]))
        max_y = int(max([p[1] for p in points]))

        def point_in_star(px, py):
            crossings = 0
            for i in range(len(points)):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % len(points)]
                if ((y1 <= py < y2) or (y2 <= py < y1)) and (px < ((x2 - x1) * (py - y1) / (y2 - y1) + x1)):
                    crossings += 1
            return crossings % 2 == 1

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if point_in_star(x, y):
                    self.draw_pixel(x, y, color)


    def shutdown(self):
        self.cyd.shutdown()

    def menu_options(self, options):
        self.clear_screen()
        y = 10
        for option in options:
            self.display_text(option, 10, y)
            y += 20

    def check_menu_touch(self, num_options):
        while True:
            x, y = self.cyd.touches()
            x, y = self.touch_to_display(x, y)  # Correct the coordinates
            if x and y:
                for i in range(num_options):
                    button_y = 40 + i * 40
                    if button_y <= y <= button_y + 30:
                        return i + 1

    def clear_screen(self):
        self.cyd.display.fill_rectangle(0, 0, self.cyd.display.width, self.cyd.display.height, self.colors["BLACK"])
    
    # 問答遊戲相關函數
    def custom_shuffle(self, lst):
        """Implementing a simple shuffle algorithm"""
        for i in range(len(lst) - 1, 0, -1):
            j = random.randint(0, i)
            lst[i], lst[j] = lst[j], lst[i]

    def display_question(self, question, choices_start_y):
        self.clear_screen()
        question_text = self.wrap_text(question['question'], 25)
        y = 10
        for line in question_text:
            self.display_text(line, 10, y, self.colors["WHITE"])
            y += 10
        button_y = choices_start_y
        for index, choice in enumerate(question['choices']):
            self.fill_rectangle(10, button_y, 220, 30, self.colors["RED"])
            choice_text = f"{index + 1}. {choice}"
            self.display_text(choice_text, 15, button_y + 10, self.colors["WHITE"])
            button_y += 40
        return choices_start_y

    def wrap_text(self, text, max_chars):
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 > max_chars:
                lines.append(current_line)
                current_line = word
            else:
                current_line += " " + word
        if current_line:
            lines.append(current_line)
        return lines

    def check_touch(self, num_choices, choices_start_y):
        while True:
            x, y = self.cyd.touches()
            x, y = self.touch_to_display(x, y)  # Correct the coordinates
            if x and y:
                if 10 <= x <= 230:
                    for i in range(num_choices):
                        button_y = choices_start_y + i * 40
                        if button_y <= y <= button_y + 30:
                            return i

    def run_quiz(self, questions):
        self.custom_shuffle(questions)
        questions = questions[:10]

        total_score = 0
        start_time = time.time()

        for question in questions:
            choices_start_y = self.display_question(question, 60)
            choice = self.check_touch(len(question['choices']), choices_start_y)
            #self.clear_screen()  # Clear the screen
            if choice == question['answer']:
                self.display_text("Correct!", 10, 250, self.colors["GREEN"])
                total_score += 1
            else:
                self.display_text("Wrong!", 10, 250, self.colors["RED"])
            time.sleep(2)

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.clear_screen()
        self.display_text(f"Score: {total_score}/10", 10, 10, self.colors["WHITE"])
        self.display_text(f"Time: {int(elapsed_time)}s", 10, 30, self.colors["WHITE"])
        time.sleep(5)

    # 繪製圖形慢慢畫的函數
    def draw_line_slowly(self, x1, y1, x2, y2, color, delay=0.01):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.draw_pixel(x1, y1, color)
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
            time.sleep(delay)

    def draw_square_slowly(self, start_x, start_y, side_length, color, delay=0.01):
        for i in range(side_length):
            self.draw_pixel(start_x + i, start_y, color)
            time.sleep(delay)
        for i in range(side_length):
            self.draw_pixel(start_x + side_length, start_y + i, color)
            time.sleep(delay)
        for i in range(side_length):
            self.draw_pixel(start_x + side_length - i, start_y + side_length, color)
            time.sleep(delay)
        for i in range(side_length):
            self.draw_pixel(start_x, start_y + side_length - i, color)
            time.sleep(delay)

    def draw_circle_slowly(self, center_x, center_y, radius, color, delay=0.01):
        for angle in range(0, 360, 5):
            x = int(center_x + radius * math.cos(math.radians(angle)))
            y = int(center_y + radius * math.sin(math.radians(angle)))
            self.draw_pixel(x, y, color)
            time.sleep(delay)

    def draw_star_slowly(self, x_center, y_center, radius, color, delay=0.01):
        # 繪製五角星的頂點
        points = []
        for i in range(5):
            outer_angle = math.radians(i * 72)
            inner_angle = math.radians(i * 72 + 36)
            outer_x = x_center + radius * math.cos(outer_angle)
            outer_y = y_center + radius * math.sin(outer_angle)
            inner_x = x_center + (radius / 2.5) * math.cos(inner_angle)
            inner_y = y_center + (radius / 2.5) * math.sin(inner_angle)
            points.append((outer_x, outer_y))
            points.append((inner_x, inner_y))
        
        # 繪製星形的邊
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            self.draw_line_slowly(int(x1), int(y1), int(x2), int(y2), color, delay)


    def draw_triangle_slowly(self, x1, y1, x2, y2, x3, y3, color, delay=0.01):
        self.draw_line_slowly(x1, y1, x2, y2, color, delay)
        self.draw_line_slowly(x2, y2, x3, y3, color, delay)
        self.draw_line_slowly(x3, y3, x1, y1, color, delay)


    def draw_circle_pattern(self, fixed_x, fixed_y, radius=2, increment=3, start_angle=0, change_angle=60, colors=None, color_index=0, speed=0.2):
        if radius > 130:
            return
        if colors is None:
            colors = [self.colors["RED"], self.colors["GREEN"], self.colors["BLUE"]]
        
        # 確保新中心點的計算是正確的
        new_center_x = int(fixed_x + radius * math.cos(math.radians(start_angle)))
        new_center_y = int(fixed_y + radius * math.sin(math.radians(start_angle)))

        # 使用顏色索引來繪製圓形
        self.draw_circle_slowly(new_center_x, new_center_y, radius, colors[color_index], speed)
        time.sleep(speed)

        # 遞歸調用來繼續繪製圖案
        self.draw_circle_pattern(fixed_x, fixed_y, radius + increment, increment, (start_angle + change_angle) % 360, change_angle, colors, (color_index + 1) % len(colors), speed)