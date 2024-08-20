"""
Created by Mikey chen.
Created on 2024-07-25
"""

"""
Import statements for the quiz game script.

Imports:
- `question` module: Contains data and functions related to quiz questions.(question bank)
- `random`: Provides functions for generating random numbers, used to select random quiz questions.
"""
from question import *
import random

# functions:
def recognition_message(player_name: str) -> None:
    """
    Displays a recognition message and badge for players who score 20 points at the Hard level.

    Arguments:
    ---------
        player_name(str): The name of player receiving recognition
    """
    #Display the player's name and his achievements!
    print(f"\n🎉 Congratulations, {player_name}! 🎉")
    print("You've achieved an incredible feat by scoring 20 points at the Hard level!")
    print("Your dedication and skill have set you apart as a top player.")
    print("Here's a special badge just for you:")

    #Define a badge with some lines to recognize player achivements
    badge: list = [
        "    _____",
        "   /     \\",
        "  | () () |",
        "   \\  ^  /",
        "    |||||",
        "    |||||",
    ]

    # Print each line of the badge to display the recognition award
    for line in badge:
        print(line)
    print("\nKeep up the great work and continue to conquer the challenges!")


def get_valid_name() -> str:
    """
       Prompts the user for their name and ensures it is within the valid length range.
        This function requests the user to input their name, ensuring that the length of the name
        within the specified minimum(1) and maximum(8) character limits. If the user’s input does not
        meet these length requirements, the function provides feedback and requests the input again
        until a valid name is entered.

       Returns:
           name(str): The valid name entered by the user.
       """
    # Prompt the user for their name with length constraints and strip any leading/trailing whitespace.
    name = input(
        f"What is your name (length needs to be between {MINIMUM_CHARACTERS} and {MAXIMUM_CHARACTERS}):"
    ).strip()

    # Check if the entered name length is within the valid range.
    # if the length of the enter name is within the invalid range
    # This while loop will loop to ask the name again
    # Until the name is within the valid range
    # The while loop will stop and proceed
    while len(name) < MINIMUM_CHARACTERS or len(name) > MAXIMUM_CHARACTERS:
        # As length of the entered name is less than minimum range(1) it will raise a message to inform too short
        if len(name) < MINIMUM_CHARACTERS:
            # Inform the users minimum valid range for the length of the name
            print(f"Name too short, at least longer than {MINIMUM_CHARACTERS} length")
        # As the length of the name is more than the maximum range(8) it will raise a message
        elif len(name) > MAXIMUM_CHARACTERS:
            # Inform the users the name is too long and remind them the maximum valid range.
            print(f"Name too long, at least shorter than {MAXIMUM_CHARACTERS} length")
        # Prompt the user to input their name again until it meets the length requirements.
        name: str = input(
            f"\nInput your name again between {MINIMUM_CHARACTERS} and {MAXIMUM_CHARACTERS} length:"
        ).strip()  # .strip() to trim the blank from the input
    # Return the valid name entered by the user.
    return name


def display_rules():
    """
        Briefly display the rules and instructions for the game.

        This function prints out a summary of the game's rules and instructions to guide the user.
        It provides information on how to start the game, manage lives, answer questions, wager points,
        and how scoring and rewards work. Additionally, it explains the conditions under which the game ends.
        """
    # Print a heading to indicate the display of game rules.
    print("\nDisplay the rules briefly:")

    # Print instructions on how to start the game.
    print("\n--Start: Choose a difficulty level and enter a name.")

    # Print instructions on managing lives based on the selected difficulty level.
    print("--Lives: Start with lives based on difficulty. Lose a life if score hits 0.")

    #  Print instructions on how to answer questions to earn points.
    print("--Questions: Answer multiple-choice questions to earn points.")

    # Print instructions on the wagering system available after answering a question correctly.
    print(
        "--Wagering: After a correct answer, wager points to potentially gain more or lose points."
    )

    # Print instructions on how scoring varies with difficulty and how negative scores are handled.
    print("--Scoring: Points vary by difficulty. Score below 0 is set to 0.")

    # Print instructions on earning rewards and conditions for receiving them.
    print("--Rewards: Earn a reward if score reaches 20")

    # Print instructions on the conditions under which the game ends.
    print(
        "--Game End: The game ends if you run out of lives or answer 5 questions(minimum)."
    )


def continue_function(question_amount: int) -> bool:
    """
        Prompts the user to decide whether to continue the game or not.

        This function asks the user if they want to continue playing after answering every 5 questions
        It validates the user's input to ensure it is either 'Y' or 'N'. If the input is invalid, it prompts the user
        again until the input is within the valid range.

        Arguments:
        ---------
        question_amount(int):  The number of questions the user has answered so far

        Returns:
            bool: True if the user chooses to continue(y), False otherwise(n).
        """
    # prompts the user to decide whether continuing the game.Informing the number of questions done.
    continue_game: str = (
        input(
            f"\nYou have answered {question_amount} questions, do you still wanna continue(Y/N):"
        )
        .strip()  # Remove the whitespace from the input
        .upper()  # Convert the input to uppercase for the uniform type
    )

    # If the input is not either Y or N(VALID_WAGER_OPTIONS)
    # The while loop will loop and ask them again
    # Until they meet the requirements the loop will stop
    while continue_game not in VALID_WAGER_OPTIONS:
        # Raise an error message to inform the users about the valid range
        print("\nInvalid input. Only Y and N")
        # Prompt the user again for a valid input.Informing the number of questions done.
        continue_game: str = (
            input(
                f"\nYou have answered {question_amount} questions, do you still wanna continue(Y/N):"
            )
            .strip()  # Remove the whitespace from the input
            .upper() # Convert the input to uppercase for the uniform type
        )

    # Return True if the user wants to continue (input 'Y'), False(input "N")
    # By using variable == to determine the bool type
    return continue_game == "Y"


def mysterious_reward(player_name: str) -> None:
    """
        Displays a mysterious reward based on the player's score.

        This function checks the player's score to determine if they are eligible for a reward.
        If the player's score is 20 or more, it displays a congratulatory message and a visual picture
        of a thumb-up by printing. If the player is at the "Hard level", it calls a recognition function.
        If the player has not achieved the required score, it informs them of their ineligibility.
        If not user_name is provided, they will be informed they haven't done any games yet

        Arguments:
        ----------
        player_name (str): The name of the player whose score is gonna be checked.
        """
    # Display the mysterious reward functions
    print("\nA mysterious reward:")
    # Check if the play-name is provided if they have done any games
    # if not the player_name will be None, which means False in if conditions
    # No None is No False means True
    # As it is True, raising a message to inform them
    if not player_name:
        print("You have not done any games yet")

    # If they have done games, player_name will be provided
    else:
        # By using player_name and score as keys to take out the user_score
        user_score: int = user_information[player_name]["score"]
        # Check if the score is enough for redeeming the reward(20 at least)
        if user_score >= 20:
            # Define the thumb with some lines
            thumb: list = [
                "          __  ",
                "         /  | ",
                "        /   | ",
                "   ____/    | ",
                "  /         | ",
                " /          | ",
                "|           | ",
                "|           | ",
                "|           | ",
                "|___________| ",
            ]

            # Congratulate the player and print the thumb-up
            print(f"Congratulations! {player_name}")
            for line in thumb:
                print(line)
            # Check the player's level and provide additional recognition if it meets
            # If the level is hard and earned 20 score, they can redeem a recognition.
            level = user_information[player_name]["level"]
            if level == "Hard level":
                recognition_message(player_name)
        # Check the score is less than 20
        else:
            # Inform the player they are not eligible for the reward
            print("Sorry!You don't have enough score for this reward!")


def view_history():
    """
        Displays the history of player scores and levels.

        This function prints a list of all players along with their final scores and levels.
        If no player information is available, it informs the user that no records exist.

        """
    print("\nView history:")
    # if no player information is available,it informs the user that no records exist.
    if not user_information:
        print("No records(You have not done any games)")
    else:
        # Enumerate through the user information and display each player's details
        # `enumerate` starts counting from 1, providing the index (place) and the player's name
        for place, name in enumerate(user_information.keys(), start=1):

            # Retrieve the final score and level by these keys.
            final_score: int = user_information[name]["score"]
            level: str = user_information[name]["level"]
            # Display the user information with name, score, level
            print(f"{place})---({name})---final score:{final_score}----Level:{level}")


def wager_system(score: int, level: str, player_life: int) -> int:
    """
        The wagering system where the player can choose to wager points.

        This function prompts the player to decide if they want to wager their points.
        If the player chooses to wager, they are asked to enter the amount they wish to wager,
        which must be within a specified range and not exceed their current score.

        The function validates the input to ensure it is within the valid range and handles any
        invalid inputs by prompting the user again. If the player answers the wager question correctly,
        their score is increased by the wagered amount. If they answer incorrectly, their score is decreased
        by the wagered amount. The function returns the updated score.

        Arguments:
        ---------
        score (int): The player's current score.
        level (str): The difficulty level chosen
        player_life (int): The number of lives the player has.

        Returns:
        -------
        score(int): The updated score after wagering.
        """
    while True:
        # Inform the player of the consequences of a wrong wager
        print(
            "\nIf you answer the wager question incorrect, you will lose your wager points"
        )
        # Prompt the user to choose whether to wager.
        wager_option: str = input("Do you wanna wager your socre? (Y/N)").upper().strip()

        # Check if the wager_option is in the valid range
        # If not the loop will keep asking the wager_option
        # Until the wager option is in the valid range.
        while wager_option not in VALID_WAGER_OPTIONS:
            # Raise an error message to infrom the users about the valid range
            print("\nInvalid input! The valid input is Y or N")
            # Prompt the users to enter an valid value
            wager_option = input("Do you wanna wager you score?(Y/N)").upper().strip()
        # 
        if wager_option == "Y":
            while True:
                try:
                    wager_amount = int(
                        input(
                            f"\nHow many points you wanna wager between {MINIMUM_WAGER_AMOUNT} and {score}(Max):"
                        )
                    )
                    while wager_amount <= 0 or wager_amount > score:
                        print(
                            f"\nInvalid wager. Enter a value between {MINIMUM_WAGER_AMOUNT} and {score}."
                        )
                        wager_amount = int(
                            input(
                                f"\nHow many points you wanna wager between {MINIMUM_WAGER_AMOUNT} and {score}(Max):"
                            )
                        )
                    correct, question_number = ask_question(level, score, player_life)
                    if correct:
                        score += wager_amount
                        print(
                            f"Congratulation!You have gained your wager points,the current score is {score}"
                        )
                    elif not correct:
                        score -= wager_amount
                        print(
                            f"Unlucky!You lost your wagered points. Your new score is {score} points."
                        )
                    return score
                except ValueError:
                    print(
                        f"\nInvalid input. Please enter a valid number between {MINIMUM_WAGER_AMOUNT} and {score}."
                    )
        else:
            print("Wager cancelled")
            return score


def life_system(life: int):
    life_deduction = 1
    life -= life_deduction
    print(f"⚠️ You have lost one life! Remaining lives: {life}")
    return life


def scoring_system(answer_correct: bool, level: str, score: int):
    if answer_correct:
        score += SCORE_RULES[level]["increment"]
        print(f"\nCorrect!You have gained {SCORE_RULES[level]['increment']} points.")
    else:
        score -= SCORE_RULES[level]["deduction"]
        if score < 0:
            score = 0
        point_lost = SCORE_RULES[level]["deduction"]
        print(f"\nIncorrect!You have lost {point_lost} points")
    print(f"Your current score: {score} points at {level})")
    return score


def display_options(menu_selection: dict) -> str:
    print("\nchoose an item:")
    options_list.clear()
    for menu_choice, menu_content in menu_selection.items():
        options_list.append(menu_choice)
        if menu_content in SCORE_RULES:
            level_desription = SCORE_RULES[menu_content]["description"]
            print(f"-({menu_choice}){menu_content}-----{level_desription}")
        else:
            print(f"-({menu_choice}) {menu_content}")
    minimum_valid_range = options_list[0]
    maximum_valid_range = options_list[len(options_list) - 1]
    print(
        f"\nYou can select by entering {minimum_valid_range} to {maximum_valid_range}"
    )
    choice: str = input("Enter your choice: ").upper().strip()
    while choice not in options_list:
        print(
            f"\nInvalid selection the input must be between {minimum_valid_range} and {maximum_valid_range}"
        )
        choice: str = input("Enter your choice again: ").upper().strip()
    return choice


def ask_question(difficulty: str, score: int, player_life: int) -> bool and int:
    question = random.choice(questions[difficulty])
    while question in question_list:
        question = random.choice(questions[difficulty])
    question_display = question["question"]
    question_list.append(question)
    question_number = len(question_list)
    print(f"\n{question_number}:{question_display}")
    for options in question["options"]:
        print(options)
    correct_answer = question["answer"]
    print(f"You current score is {score}")
    print(f"Remaining lives: {player_life}")
    print(f"correct answer is {correct_answer} ")
    answer = input("\nwhat is your answer(a,b,c,d):").upper().strip()
    while answer not in questions_options:
        answer = (
            input("\nInvalid input Enter your answer again(a,b,c,d):").strip().upper()
        )
    return answer == correct_answer, question_number


def difficulty_selection():
    score = 0
    while True:
        difficulty_choice = display_options(menu_option_difficulty)
        if difficulty_choice in menu_option_difficulty:
            level = menu_option_difficulty[difficulty_choice]
            player_life = SCORE_RULES[level]["life_number"]
            user_name = get_valid_name()
            print(
                f"\nHello {user_name}!Your selected {level}, you start with {player_life} lives "
            )
            while True:
                if player_life > 0:
                    correct, question_number = ask_question(level, score, player_life)
                    score = scoring_system(correct, level, score)
                    if (
                        question_number % 5 == 0
                        and question_number != 0
                        and question_number != 15
                    ):
                        continue_option = continue_function(question_number)
                        if not continue_option:
                            print(
                                f"\nCongratulations ({user_name}) have finished the game, your final score is {score}"
                            )
                            if score >= 20:
                                print("You can redeem a reward in the menu.")
                            user_information[user_name] = {
                                "score": score,
                                "level": level,
                            }
                            return user_name
                    if question_number >= TOTAL_QUESTION:
                        user_information[user_name] = {"score": score, "level": level}
                        print(
                            f"\nCongratulations ({user_name}) have finished all the questiosn round, your final score "
                            f"is {score}"
                        )
                        return user_name
                    if correct:
                        score = wager_system(score, level, player_life)
                    if score == 0:
                        print(f"\nWarning: Your score is {score}.")
                        print("You are gonna lose one life instead of points")
                        player_life = life_system(player_life)
                        print("Be careful! If your lives reach 0, the game is over")
                else:
                    print(f"You don't have enough life ({player_life}), Game over!")
                    user_information[user_name] = {"score": score, "level": level}
                    return user_name

        else:
            print("Invalid selection, try again")


questions: dict = {
    "Beginner level": beginner_questions,
    "Medium level": medium_level_questions,
    "Hard level": hard_level_questions,
    "Mixed level": mixed_level_questions,
}

menu_option: dict[str:str] = {
    "1": "Difficulty selection",
    "2": "View history",
    "3": "Redeem a mysterious reward (require 20 points)",
    "4": "Rules",
    "5": "Quit the game",
}

menu_option_difficulty: dict[str:str] = {
    "1": "Beginner level",
    "2": "Medium level",
    "3": "Hard level",
    "4": "Mixed level",
}
SCORE_RULES = {
    "Beginner level": {
        "increment": 4,
        "deduction": 2,
        "life_number": 4,
        "description": "Start with 4 lives, gain 4 points for correct answers, lose 2 points for incorrect answers.",
    },
    "Medium level": {
        "increment": 3,
        "deduction": 3,
        "life_number": 3,
        "description": "Start with 3 lives, gain 3 points for correct answers, lose 3 points for incorrect answers.",
    },
    "Mixed level": {
        "increment": 3,
        "deduction": 3,
        "life_number": 3,
        "description": "Start with 3 lives, gain 3 points for correct answers, lose 3 points for incorrect answers.",
    },
    "Hard level": {
        "increment": 2,
        "deduction": 4,
        "life_number": 2,
        "description": "Start with 2 lives, gain 2 points for correct answers, lose 4 points for incorrect answers.",
    },
}

questions_options = ["A", "B", "C", "D"]
VALID_WAGER_OPTIONS = ["Y", "N"]
MINIMUM_WAGER_AMOUNT = 1
options_list = []
question_list = []
user_information = {}
MAXIMUM_CHARACTERS = 8
MINIMUM_CHARACTERS = 1
running = True
user_name = None
TOTAL_QUESTION = 15
while running:
    option_choice = display_options(menu_option)
    if option_choice == "1":
        user_name = difficulty_selection()
    if option_choice == "2":
        view_history()
    if option_choice == "3":
        mysterious_reward(user_name)
    if option_choice == "4":
        display_rules()
    if option_choice == "5":
        print("Game is quitting.........")
        running = False
