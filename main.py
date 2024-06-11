from cyd_telearn import CYD_Telearn
import time
import random

questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "Berlin", "Madrid", "Lisbon"], "answer": 0},
    {"question": "What is the hardest natural substance on Earth?", "choices": ["Gold", "Iron", "Diamond", "Silver"], "answer": 2},
    {"question": "What is the chemical symbol for gold?", "choices": ["Au", "Ag", "Pb", "Fe"], "answer": 0},
    {"question": "What planet is known as the Red Planet?", "choices": ["Mars", "Jupiter", "Mercury", "Saturn"], "answer": 0},
    {"question": "What is the largest mammal?", "choices": ["Elephant", "Blue Whale", "Giraffe", "Buffalo"], "answer": 1},
    {"question": "Which country hosted the 2016 Summer Olympics?", "choices": ["China", "Brazil", "Russia", "Japan"], "answer": 1},
    {"question": "What is the main ingredient in guacamole?", "choices": ["Tomato", "Avocado", "Onion", "Pepper"], "answer": 1},
    {"question": "Who wrote 'Hamlet'?", "choices": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"], "answer": 1},
    {"question": "What is the smallest country in the world?", "choices": ["Vatican City", "Monaco", "Nauru", "Liechtenstein"], "answer": 0},
    {"question": "What is the hottest planet in our solar system?", "choices": ["Mercury", "Venus", "Mars", "Jupiter"], "answer": 1},
    {"question": "What is the longest river in the world?", "choices": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": 1},
    {"question": "Who painted the Mona Lisa?", "choices": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], "answer": 1},
    {"question": "What is the hardest rock?", "choices": ["Granite", "Obsidian", "Diamond", "Quartz"], "answer": 2},
    {"question": "Which element has the highest melting point?", "choices": ["Iron", "Carbon", "Tungsten", "Gold"], "answer": 2},
    {"question": "Which country has the most natural lakes?", "choices": ["Australia", "Canada", "India", "USA"], "answer": 1},
    {"question": "What does the term 'piano' mean?", "choices": ["To be played softly", "To be played loudly", "To be played with feeling", "To be played quickly"], "answer": 0},
    {"question": "What year did the Titanic sink?", "choices": ["1912", "1905", "1898", "1923"], "answer": 0},
    {"question": "What is the symbol for potassium?", "choices": ["P", "K", "Pt", "Pa"], "answer": 1},
    {"question": "What is the capital of Australia?", "choices": ["Sydney", "Perth", "Canberra", "Melbourne"], "answer": 2},
    {"question": "Which is the largest planet in our solar system?", "choices": ["Jupiter", "Saturn", "Neptune", "Earth"], "answer": 0}
]

cyd_telearn = CYD_Telearn()
cyd_telearn.clear_screen()

# 定義按鈕文本
button_texts = ["Show Text", "Draw Shapes", "Touch Screen", "Random Shapes", "Circle Pattern", "QA Game", "Exit"]
cyd_telearn.display_text("Please choose a button:", 10, 20, cyd_telearn.colors["YELLOW"])

# 顯示按鈕
y = cyd_telearn.top_menu_y
for text in button_texts:
    cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
    cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
    y += cyd_telearn.top_menu_y

while True:
    choice = cyd_telearn.check_menu_touch(len(button_texts))
    cyd_telearn.clear_screen()
    
    if choice == 1:
        cyd_telearn.clear_screen()
        text = "Hello, CYD!"
        x = cyd_telearn.width//2
        y = cyd_telearn.height//2
        color = cyd_telearn.colors['YELLOW']
        cyd_telearn.display_text(text, x, y, color)
        time.sleep(3)
    elif choice == 2:
        cyd_telearn.clear_screen()
        cyd_telearn.draw_rectangle(20, 20, 100, 60, cyd_telearn.colors["RED"])
        cyd_telearn.fill_rectangle(140, 20, 100, 60, cyd_telearn.colors["GREEN"])
        cyd_telearn.draw_circle(70, 150, 30, cyd_telearn.colors["BLUE"])
        cyd_telearn.fill_circle(190, 150, 30, cyd_telearn.colors["YELLOW"])
        cyd_telearn.draw_triangle(50, 220, 20, 260, 80, 260, cyd_telearn.colors["PINK"])
        cyd_telearn.fill_triangle(150, 220, 120, 260, 180, 260, cyd_telearn.colors["ORANGE"])
        time.sleep(3)
    elif choice == 3:
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
            if cyd_telearn.cyd.double_tap(x, y):
                break

            print("Touches:", x, y)

            # Prevent circles from appearing off-screen.
            y = min(max(y, r + 1), cyd_telearn.height - (r + 1))
            x = min(max(x, r + 1), cyd_telearn.width - (r + 1))

            # Create circle
            cyd_telearn.fill_circle(x, y, r, colors[c])

            c = (c + 1) % len(colors)

    elif choice == 4:
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
    elif choice == 5:
        cyd_telearn.clear_screen()

        x = cyd_telearn.width // 2
        y = cyd_telearn.height // 2
        radius = 2
        increment = 3
        start_angle = 0
        change_angle = 30
        colors = [cyd_telearn.colors["RED"], cyd_telearn.colors["GREEN"], cyd_telearn.colors["BLUE"]]

        # 繪製圓形圖案
        cyd_telearn.draw_circle_pattern(x, y, radius, increment, start_angle, change_angle, colors, color_index=0, speed=0.02)
    elif choice == 6:
        cyd_telearn.clear_screen()
        cyd_telearn.run_quiz(questions)
        time.sleep(5)
                
    elif choice == 7:
        cyd_telearn.shutdown()
    
    # 重新顯示按鈕
    cyd_telearn.clear_screen()
    y = cyd_telearn.top_menu_y
    cyd_telearn.display_text("Please choose a button:", 10, 20, cyd_telearn.colors["YELLOW"])
    for text in button_texts:
        cyd_telearn.fill_rectangle(10, y, 220, 30, cyd_telearn.colors["BLUE"])
        cyd_telearn.display_text(text, 15, y + 10, cyd_telearn.colors["WHITE"])
        y += cyd_telearn.top_menu_y
