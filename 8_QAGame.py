from cyd_telearn import CYD_Telearn
import time

cyd_telearn = CYD_Telearn()

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
cyd_telearn.clear_screen()
cyd_telearn.run_quiz(questions)
time.sleep(5)
cyd_telearn.shutdown()
