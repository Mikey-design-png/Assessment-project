from question import *
import random
def display_options(menu_option: dict) -> str:
    print("\nchoose an item:")
    for menu_choice, menu_content in menu_option.items():
        print(f"-({menu_choice}) {menu_content}")
    choice: str = input("Enter your choice: ").upper()
    return choice


def ask_question(questions: dict, difficulty: str, number: int) -> bool:
    question = random.choice(questions[difficulty])
    question_display = question["question"]
    print(f"\n{number}:{question_display}")
    for options in question["options"]:
        print(options)
    correct_answer = question["answer"]
    answer = input("what is your answer:").upper()
    print(f"correct answer is {correct_answer} ")
    return answer == correct_answer


def difficulty_selection(questions: dict):
    score = 0
    question_number = 1
    while True:
        difficulty_choice = display_options(menu_option_difficulty)
        if difficulty_choice in menu_option_difficulty:
            level = menu_option_difficulty[difficulty_choice]
            while True:
                correct = ask_question(questions, level, question_number)
                question_number += 1
                if correct:
                    score += SCORE_INCREMENT
                    print(f"Correct! Your score is now {score} points.")










        else:
            print("Invalid selection, try again")

SCORE_INCREMENT = 2

questions: dict = {
    "Beginner level": beginner_questions,
    "Medium level": medium_level_questions,
    "Hard level": hard_level_questions,
    "Mixed level": mixed_level_questions
}

menu_option: dict[str:str] = {
    "1": "Difficulty selection",
    "2": "View history",
    "3": "Quit the game"
}

menu_option_difficulty: dict[str:str] = {
    "1": "Beginner level",
    "2": "Medium level",
    "3": "Hard level",
    "4": "Mixed level"
}

running = True
while running:
    option_choice = display_options(menu_option)
    if option_choice == "1":
        difficulty_selection(questions)
    else:
        print("\n Invalid selection. Please try again.")



