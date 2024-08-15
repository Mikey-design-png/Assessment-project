from question import *
import random

def life_system(life:int, level: str):
    life_deduction = 1
    life -= life_deduction
    print(f"You have lost one life, {life} left")\
    return life
def scoring_system(answer_correct:bool, level:str, score:int):
    if correct:
        score += SCORE_RULES[level]["increment"]
        print(f"Correct! Your score is now {score} points at the {level}.")
    else:
        score -= SCORE_RULES[level]["deduction"]
        print(f"Incorrect! Your score is now {score} points at the {level}.")

def display_options(menu_option: dict) -> str:
    print("\nchoose an item:")
    for menu_choice, menu_content in menu_option.items():
        print(f"-({menu_choice}) {menu_content}")
    choice: str = input("Enter your choice: ").upper()
    return choice


def ask_question(difficulty: str, number: int) -> bool:
    question = random.choice(questions[difficulty])
    question_display = question["question"]
    print(f"\n{number}:{question_display}")
    for options in question["options"]:
        print(options)
    correct_answer = question["answer"]
    print(f"correct answer is {correct_answer} ")
    answer = input("what is your answer:").upper()
    return answer == correct_answer


def difficulty_selection():
    score = 0
    question_number = 1
    while True:
        difficulty_choice = display_options(menu_option_difficulty)
        if difficulty_choice in menu_option_difficulty:
            level = menu_option_difficulty[difficulty_choice]
            player_life = SCORE_RULES[level]["life"]
            while True:
                if score >= 0:
                    correct = ask_question(questions, level, question_number)
                    question_number += 1
                    score = scoring_system(correct, level, score)
                elif score < 0:
                    print(f"You don't have enough score!{score}")
                    print("You will lose one life if you answer incorrectly")
                    
        else:
            print("Invalid selection, try again")
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
SCORE_RULES = {
    "Beginner level": {"increment": 4, "deduction": 2, "life_number": 4},
    "Medium level": {"increment": 3, "deduction": 3, "life_number": 3},
    "Mixed level": {"increment": 3, "deduction": 3, "life_number": 3},
    "Hard level": {"increment": 2, "deduction": 4,"life_number": 2},
}

running = True
while running:
    option_choice = display_options(menu_option)
    if option_choice == "1":
        difficulty_selection(questions)
    else:
        print("\n Invalid selection. Please try again.")



