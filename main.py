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
    print(f"correct answer is {correct_answer} ")
    answer = input("what is your answer:").upper()
    return answer == correct_answer


def difficulty_selection(questions: dict):
    score = 0
    question_number = 1
    while True:
        difficulty_choice = display_options(menu_option_difficulty)
        if difficulty_choice in menu_option_difficulty:
            level = menu_option_difficulty[difficulty_choice]
            while True:
                if score >= 0:
                    correct = ask_question(questions, level, question_number)
                    question_number += 1
                    if correct:
                        if level == "Beginner level":
                            score += SCORE_INCREMENT_BEGINNER
                        elif level == "Medium level" or level == "Mixed level":
                            score += SCORE_INCREMENT_Medium_MIXED
                        elif level == "Hard level":
                            score += SCORE_INCREMENT_HARD
                        print(f"Correct! Your score is now {score} points at the {level}.")
                    else:
                        if level == "Beginner level":
                            score -= SCORE_DEDUCTION_BEGINNER
                        elif level == "Medium level" or level == "Mixed level":
                            score -= SCORE_DEDUCTION_Medium_MIXED
                        elif level == "Hard level":
                            score -= SCORE_DEDUCTION_HARD
                        print(
                            f"INcorrect! Your score is now {score} points at the {level}.(The score is less than 0 will game over)")
                elif score < 0:
                    print(f"Game over your score is {score}")
                    return














        else:
            print("Invalid selection, try again")


SCORE_INCREMENT_BEGINNER = 4
SCORE_INCREMENT_Medium_MIXED = 3
SCORE_INCREMENT_HARD = 2

SCORE_DEDUCTION_BEGINNER = 2
SCORE_DEDUCTION_Medium_MIXED = 3
SCORE_DEDUCTION_HARD = 4
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



