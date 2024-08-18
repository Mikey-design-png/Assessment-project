from question import *
import random


def display_rules():
    print("\nDisplay the rules briefly:")
    print("\n--Start: Choose a difficulty level and enter a name.")
    print("--Lives: Start with lives based on difficulty. Lose a life if score hits 0.")
    print("--Questions: Answer multiple-choice questions to earn points.")
    print("--Wagering: After a correct answer, wager points to potentially gain more or lose points.")
    print("--Scoring: Points vary by difficulty. Score below 0 is set to 0.")
    print("--Rewards: Earn a reward if score reaches 20")
    print("--Game End: The game ends if you run out of lives or answer 5 questions(minimum).")





def mysterious_reward(user_name: str):
    print("\nA mysterious reward:")
    if not user_name:
        print("You have not done any games yet")
    else:
        user_score = user_information[user_name]
        if user_score>= 20:
            thumb =  [
                "          __  ",
                "         /  | ",
                "        /   | ",
                "   ____/    | ",
                "  /         | ",
                " /          | ",
                "|           | ",
                "|           | ",
                "|           | ",
                "|___________| "
            ]
            for line in thumb:
                print(line)
        else:
            print("Sorry!You don't have enough score for this reward!")


def view_history():
    print("\nView history:")
    if not user_information:
        print("No records")
    else:
        for place, (name, final_score) in enumerate(user_information.items(), start = 1):
            print(f"{place})---({name})---final score:{final_score}")



def wager_system(score: int) -> int:
    while True:
        try:
            wager_amount = int(input(f"\nHow many points you wanna wager Max:{score} :"))
            if wager_amount <= 0 or wager_amount > score:
                print(f"Invalid wager. Enter a value between 1 and {score}.")
            else:
                return wager_amount
        except ValueError:
            print(f"Invalid input. Please enter a valid number.")


def life_system(life: int):
    life_deduction = 1
    life -= life_deduction
    print(f"⚠️ You have lost one life! Remaining lives: {life}")
    return life


def scoring_system(answer_correct: bool, level: str, score: int):
    if answer_correct:
        score += SCORE_RULES[level]["increment"]
        print(f"Correct!You have gained {SCORE_RULES[level]['increment']} points.")
    else:
        score -= SCORE_RULES[level]["deduction"]
        if score < 0:
            score = 0
        point_lost = SCORE_RULES[level]["deduction"]
        print(f"Incorrect!You have lost {point_lost} points")
    print(f"Your current score: {score} points at {level})")
    return score


def display_options(menu_option: dict) -> str:
    print("\nchoose an item:")
    options_list.clear()
    for menu_choice, menu_content in menu_option.items():
        options_list.append(menu_choice)
        if menu_content in SCORE_RULES:
            level_description = SCORE_RULES[menu_content]["description"]
            print(f"-({menu_choice}){menu_content}-----{level_description}")
        else:
            print(f"-({menu_choice}) {menu_content}")
    minimum_valid_range = options_list[0]
    maximum_valid_range = options_list[len(options_list) - 1]
    print(f"\nYou can select by entering {minimum_valid_range} to {maximum_valid_range}")
    choice: str = input("Enter your choice: ").upper().strip()
    while choice not in options_list:
        print(f"\nInvalid selection the input must be between {minimum_valid_range} and {maximum_valid_range}")
        choice: str = input("Enter your choice again: ").upper().strip()
    return choice


def ask_question(difficulty: str, number: int) -> bool and int:
    question = random.choice(questions[difficulty])
    while question in question_list:
        question = random.choice(questions[difficulty])
    question_display = question["question"]
    print(f"\n{number}:{question_display}")
    for options in question["options"]:
        print(options)
    correct_answer = question["answer"]
    print(f"correct answer is {correct_answer} ")
    answer = input("what is your answer:").upper().strip()
    number += 1
    question_list.append(question)
    return answer == correct_answer, number


def difficulty_selection() :
    score = 0
    question_number = 1
    while True:
        difficulty_choice = display_options(menu_option_difficulty)
        if difficulty_choice in menu_option_difficulty:
            level = menu_option_difficulty[difficulty_choice]
            player_life = SCORE_RULES[level]["life_number"]
            user_name = input(
                f"What is your name (length needs to be between {MINIMUM_CHARACTERS} and {MAXIMUM_CHARACTERS}):").strip()
            while len(user_name) < MINIMUM_CHARACTERS or len(user_name) > MAXIMUM_CHARACTERS:
                user_name = input(f"\nInput your name again between {MINIMUM_CHARACTERS} and {MAXIMUM_CHARACTERS} length:").strip()
            print(f"\nHello {user_name}!Your selected {level}, you start with {player_life} lives ")
            while True:
                if player_life > 0:
                    correct, question_number = ask_question(level, question_number)
                    score = scoring_system(correct, level, score)
                    if correct:
                        wager_option = input("Do you wanna wager your socre? (Y/N)").upper()
                        if wager_option == "Y":
                            wager_amount = wager_system(score)
                            correct, question_number = ask_question(level, question_number)
                            if correct:
                                score += wager_amount
                                print(f"Congratulation!You have gained your wager points,the current score is {score}")
                            elif not correct:
                                score -= wager_amount
                                print(f"Unlucky!You lost your wagered points. Your new score is {score} points.")
                        else:
                            print("Wager cancelled")
                    if score == 0:
                        print(f"\nWarning: Your score is {score}.")
                        print("You are gonna lose one life instead of points")
                        player_life = life_system(player_life)
                        print("Be careful! If your lives reach 0, the game is over")

                else:
                    print(f"You don't have enough life {player_life}, Game over!")
                    user_information[user_name] = score
                    return user_name
                if question_number >= 5:
                    user_information[user_name] = score
                    print(f"Congratulations you have finished all the questiosn round, your final score is {score}")
                    return user_name
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
    "3": "Redeem a mysterious reward (require 20 points)",
    "4": "Rules",
    "5": "Quit the game"

}

menu_option_difficulty: dict[str:str] = {
    "1": "Beginner level",
    "2": "Medium level",
    "3": "Hard level",
    "4": "Mixed level"
}
SCORE_RULES = {
    "Beginner level": {"increment": 4, "deduction": 2, "life_number": 4
                       ,"description":"Start with 4 lives, gain 4 points for correct answers, lose 2 points for incorrect answers."},
    "Medium level": {"increment": 3, "deduction": 3, "life_number": 3
                    ,"description":"Start with 3 lives, gain 3 points for correct answers, lose 3 points for incorrect answers."},
    "Mixed level": {"increment": 3, "deduction": 3, "life_number": 3
                    ,"description":"Start with 3 lives, gain 3 points for correct answers, lose 3 points for incorrect answers."},
    "Hard level": {"increment": 2, "deduction": 4, "life_number": 2,
                   "description": "Start with 2 lives, gain 2 points for correct answers, lose 4 points for incorrect answers."
                   }
}

options_list = []
question_list = []
user_information = {}
MAXIMUM_CHARACTERS = 8
MINIMUM_CHARACTERS = 1
running = True
user_name = None
while running:
    option_choice = display_options(menu_option)
    if option_choice == "1":
        user_name = difficulty_selection()
    if option_choice == "2":
        view_history()
    if option_choice =="3":
        mysterious_reward(user_name)
    if option_choice == "4":
        display_rules()
    if option_choice == "5":
        print("Game is quitting.........")
        running = False



