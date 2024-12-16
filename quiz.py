import random
import json
import time

questions_db = {
    "General Knowledge": [
        {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"}
    ],
    "Science": [
        {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "NaCl"], "answer": "H2O"},
        {"question": "What is the speed of light?", "options": ["3x10^8 m/s", "5x10^6 m/s", "1x10^5 m/s", "2x10^8 m/s"], "answer": "3x10^8 m/s"}
    ]
}

class Player:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.score = 0

def fetch_questions(category):
    if category in questions_db:
        return random.sample(questions_db[category], len(questions_db[category]))
    else:
        print("Invalid category selected!")
        return []

def start_quiz(player):
    print("\nWelcome to the Quiz Game,", player.name)
    print("Available categories: ", ", ".join(questions_db.keys()))
    category = input("Choose a category: ")
    questions = fetch_questions(category)

    if not questions:
        print("No questions available. Exiting quiz.")
        return

    for i, question_data in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question_data['question']}")
        for idx, option in enumerate(question_data['options'], 1):
            print(f"{idx}. {option}")

        try:
            answer_idx = int(input("Enter the option number: "))
            selected_option = question_data['options'][answer_idx - 1]
        except (ValueError, IndexError):
            print("Invalid input! Moving to next question.")
            continue

        if selected_option == question_data['answer']:
            print("Correct Answer!")
            player.score += 1
        else:
            print(f"Wrong Answer! The correct answer was: {question_data['answer']}")

    print("\nQuiz Completed!")
    print(f"Final Score for {player.name}: {player.score}")

if __name__ == "__main__":
    print("Welcome to the Quiz Game System!")
    name = input("Enter your name: ")
    identifier = input("Enter a unique identifier (email/username): ")
    player = Player(name, identifier)

    start_quiz(player)

    print("\nThank you for playing!")






