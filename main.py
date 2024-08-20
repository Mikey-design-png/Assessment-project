"""
An Uncertain Reward Game

Created by Mikey Chen.
Created on 2024-07-25
"""

from question import *
import random

"""
Import statements for the quiz game script.

Imports:
- `question` module: Contains data and functions
  related to quiz questions (question bank).

- `random`: Provides functions for generating random
  numbers, used to select random quiz questions.
"""


# Functions:
def recognition_message(player_name: str) -> None:
    """
    Displays a recognition message and badge for players who score
    20 points at the Hard level.

    Arguments:
    ---------
        player_name (str): The name of player receiving recognition.
    """
    # Display the player's name and achievements!
    print(f"\n🎉 Congratulations, {player_name}! 🎉")
    print("You've achieved an incredible feat by scoring 20 points at the"
          " Hard level!")
    print("Your dedication and skill have set you apart as a top player.")
    print("Here's a special badge just for you:")

    # Define a badge with some lines to recognize player achievements.
    badge: list = [
        "    _____",
        "   /     \\",
        "  | () () |",
        "   \\  ^  /",
        "    |||||",
        "    |||||",
    ]

    # Print each line of the badge to display the recognition award.
    for line in badge:
        print(line)
    print("\nKeep up the great work and continue to conquer the challenges!")


def get_valid_name() -> str:
    """
    Prompts the user for their name and ensures it is within the valid
    length range. This function requests the user to input their name,
    ensuring that the length of the name is within the specified minimum
    (1) and maximum (8) character limits. If the user’s input does not
    meet these length requirements, the function provides feedback and
    requests the input again until a valid name is entered.

    Returns:
        name (str): The valid name entered by the user.
    """
    # Prompt the user for their name with length constraints and strip any
    # leading/trailing whitespace.
    name: str = input(
        f"What is your name (length needs to be between {MINIMUM_CHARACTERS}"
        f" and {MAXIMUM_CHARACTERS}):"
    ).strip()

    # Check if the entered name length is within the valid range.
    while len(name) < MINIMUM_CHARACTERS or len(name) > MAXIMUM_CHARACTERS:
        # Inform the user if the name is too short.
        if len(name) < MINIMUM_CHARACTERS:
            print(f"Name too short, at least {MINIMUM_CHARACTERS} characters")
        # Inform the user if the name is too long.
        elif len(name) > MAXIMUM_CHARACTERS:
            print(f"Name too long, at most {MAXIMUM_CHARACTERS} characters")
        # Prompt the user to input their name again until it meets the
        # length requirements.
        name: str = input(
            f"\nInput your name again between {MINIMUM_CHARACTERS} and"
            f" {MAXIMUM_CHARACTERS} characters:"
        ).strip()  # .strip() to trim any leading/trailing whitespace
    return name


def display_rules():
    """
    Briefly display the rules and instructions for the game.

    This function prints out a summary of the game's rules and
    instructions to guide the user. It provides information on how
    to start the game, manage lives, answer questions, wager points,
    and how scoring and rewards work. Additionally, it explains the
    conditions under which the game ends.
    """
    # Print a heading to indicate the display of game rules.
    print("\nDisplay the rules briefly:")

    # Print instructions on how to start the game.
    print("\n--Start: Choose a difficulty level and enter a name.")

    # Print instructions on managing lives based on the selected
    # difficulty level.
    print("--Lives: Start with lives based on difficulty. Lose a life if"
          " score hits 0.")

    # Print instructions on how to answer questions to earn points.
    print("--Questions: Answer multiple-choice questions to earn points.")

    # Print instructions on the wagering system available after
    # answering a question correctly.
    print(
        "--Wagering: After a correct answer, wager points to potentially"
        " gain more or lose points."
    )

    # Print instructions on how scoring varies with difficulty and how
    # negative scores are handled.
    print("--Scoring: Points vary by difficulty. Score below 0 is set to 0.")

    # Print instructions on earning rewards and conditions for receiving them.
    print("--Rewards: Earn a reward if score reaches 20")

    # Print instructions on the conditions under which the game ends.
    print(
        "--Game End: The game ends if you run out of lives or answer"
        " 5 questions (minimum)."
    )


def continue_function(question_amount: int) -> bool:
    """
    Prompts the user to decide whether to continue the game or not.

    This function asks the user if they want to continue playing after
    answering every 5 questions. It validates the user's input to ensure
    it is either 'Y' or 'N'. If the input is invalid, it prompts the
    user again until the input is within the valid range.

    Arguments:
    ---------
    question_amount (int): The number of questions the user has answered
    so far.

    Returns:
        bool: True if the user chooses to continue (Y), False otherwise (N).
    """
    # Prompt the user to decide whether to continue the game, informing
    # the number of questions answered.
    continue_game: str = (
        input(
            f"\nYou have answered {question_amount} questions, do you still"
            " want to continue (Y/N):"
        )
        .strip()  # Remove the whitespace from the input.
        .upper()  # Convert the input to uppercase for uniformity.
    )

    # If the input is not either 'Y' or 'N' (VALID_WAGER_OPTIONS),
    # the while loop will loop and ask them again.
    while continue_game not in VALID_WAGER_OPTIONS:
        # Raise an error message to inform the user about the valid range.
        print("\nInvalid input. Only Y and N.")
        # Prompt the user again for a valid input, informing the number
        # of questions answered.
        continue_game: str = (
            input(
                f"\nYou have answered {question_amount} questions, do you"
                " want to continue (Y/N):"
            )
            .strip()  # Remove the whitespace from the input.
            .upper()  # Convert the input to uppercase for uniformity.
        )

    # Return True if the user wants to continue (input 'Y'), False (input 'N').
    return continue_game == "Y"


def mysterious_reward(player_name: str) -> None:
    """
    Displays a mysterious reward based on the player's score.

    This function checks the player's score to determine if they are
    eligible for a reward. If the player's score is 20 or more, it
    displays a congratulatory message and a visual picture of a thumb-up
    by printing. If the player is at the "Hard level", it calls a
    recognition function. If the player has not achieved the required
    score, it informs them of their ineligibility. If no player_name is
    provided, they will be informed that they haven't played any games yet.

    Arguments:
    ----------
    player_name (str): The name of the player whose score is to be checked.
    """
    # Display the mysterious reward functions.
    print("\nA mysterious reward:")

    # Check if the player_name is provided (indicating they have played games).
    if not player_name:
        print("You have not done any games yet")
    else:
        # Retrieve the user's score using player_name as the key.
        user_score: int = user_information[player_name]["score"]

        # Check if the score is enough for redeeming the reward (20 at least).
        if user_score >= 20:
            # Define the thumb-up with some lines.
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

            # Congratulate the player and print the thumb-up.
            print(f"Congratulations! {player_name}")
            for line in thumb:
                print(line)

            # Check the player's level and provide additional recognition if
            # they meet the criteria.
            level: str = user_information[player_name]["level"]
            if level == "Hard level":
                recognition_message(player_name)
        else:
            # Inform the player they are not eligible for the reward.
            print("Sorry! You don't have enough score for this reward!")


def view_history():
    """
    Displays the history of player scores and levels.

    This function prints a list of all players along with their final scores
    and levels. If no player information is available, it informs the user
    that no records exist.
    """
    print("\nView history:")
    # If no player information is available, it informs the user that
    # no records exist.
    if not user_information:
        print("No records (You have not done any games)")
    else:
        # Enumerate through the user information and display each player's
        # details. `enumerate` starts counting from 1, providing the index
        # (place) and the player's name.
        for place, name in enumerate(user_information.keys(), start=1):
            # Retrieve the final score and level by these keys.
            final_score: int = user_information[name]["score"]
            level: str = user_information[name]["level"]
            # Display the user information with name, score, level.
            print(f"{place})--({name})---final score: {final_score}-"
                  f"Level: {level}")


def wager_system(score: int, level: str, player_life: int) -> int:
    """
    The wagering system where the player can choose to wager points.

    This function prompts the player to decide if they want to wager their
    points. If the player chooses to wager, they are asked to enter the amount
    they wish to wager, which must be within a specified range and not exceed
    their current score.The function validates the input to ensure it is within
    the valid range and handles any invalid inputs by prompting the user again.
    If the player answers the wager question correctly,their score is increased
    by the wagered amount. If they answer incorrectly,their score is decreased
    by the wagered amount.The function returns the updated score.

    Arguments:
    ---------
    score (int): The player's current score.
    level (str): The difficulty level chosen.
    player_life (int): The number of lives the player has.

    Returns:
    -------
    score (int): The updated score after wagering.
    """
    while True:
        # Inform the player of the consequences of a wrong wager.
        print(
            "\nIf you answer the wager question incorrectly, you will lose"
            " your wager points."
        )
        # Prompt the user to choose whether to wager.
        wager_option: str = (
            input("Do you want to wager your score? (Y/N)").upper().strip()
        )

        # Check if the wager_option is in the valid range. If not, the
        # loop will keep asking until the wager option is valid.
        while wager_option not in VALID_WAGER_OPTIONS:
            # Raise an error message to inform the user about the valid range.
            print("\nInvalid input! The valid input is Y or N.")
            # Prompt the user to enter a valid value.
            wager_option: str = input(
                "Do you want to wager your score? (Y/N)").upper().strip()

        # Validate the wager option.
        if wager_option == "Y":
            while True:
                try:
                    # Prompt the player to enter the amount they want to wager
                    # and inform them of the valid range based on their score.
                    wager_amount: int = int(
                        input(
                            f"\nHow many points do you want to wager "
                            f"between"
                            f" {MINIMUM_WAGER_AMOUNT} and {score} (Max):"
                        )
                    )
                    # If wager amount is within the invalid range, the loop
                    # will keep asking until a valid number is entered.
                    while wager_amount <= 0 or wager_amount > score:
                        # Raise an error message and inform the valid range.
                        print(
                            f"\nInvalid wager. Enter a value between"
                            f" {MINIMUM_WAGER_AMOUNT} and {score}."
                        )
                        # Prompt the user to enter a valid wager amount.
                        wager_amount: int = int(
                            input(
                                f"\nHow many points do you want to "
                                f"wager between"
                                f" {MINIMUM_WAGER_AMOUNT} and {score} (Max):"
                            )
                        )

                    # Ask a question and determine if the answer is correct.
                    correct, question_number= ask_question(level, score, player_life)
                    # If the answer is correct,
                    # the 'correct' variable will be True.
                    if correct:
                        # Add the wager points to their score and print it
                        score += wager_amount
                        print(
                            f"Congratulations! You have gained your "
                            f"wager points,"
                            f" the current score is {score}."
                        )
                    # If the answer is incorrect,
                    # the 'correct' variable will be False.
                    elif not correct:
                        # Subtract the wager points
                        # from their score and print the new score.
                        score -= wager_amount
                        print(
                            f"Unlucky! You lost your wagered points. "
                            f"Your new score is"
                            f" {score} points."
                        )
                    # Return the updated score.
                    return score
                except ValueError:
                    # If a float or string is entered,
                    # raise an error message and
                    # prompt the user again for a valid wager amount.
                    print(
                        f"\nInvalid input. Please enter a valid number between"
                        f" {MINIMUM_WAGER_AMOUNT} and {score}."
                    )
        else:
            print("Wager cancelled")
            return score


def life_system(life: int) -> int:
    """
    Deducts a life from the player's total and prints the remaining lives.

    This function reduces the player's life count
    by a fixed amount (1) and prints
    a message indicating the number of lives remaining.

    Arguments:
    ---------
    life (int): The current number of lives the player has.

    Returns:
    -------
    int: The updated number of lives after deduction.
    """
    life_deduction: int = 1  # Amount of life to be deducted
    life -= life_deduction  # Deduct life
    print(f"⚠️ You have lost one life! Remaining lives: {life}")
    return life


def scoring_system(answer_correct: bool, level: str, score: int) -> int:
    """
    Updates the player's score based on the correctness of the answer and the
    difficulty level.

    This function adjusts the player's score according to whether their answer
    was correct or not.It increases the score
    based on the level's increment rule if the answer is correct,
    or decreases it based on the level's deduction rule
     if the answer is incorrect.
    The function ensures that the score does not drop
    below zero and prints the updated score.

    Arguments:
    ---------
    answer_correct (bool): Indicates if the player's answer was correct.
    level (str): The difficulty level affecting the score
                 increment or deduction.
    score (int): The current score of the player.

    Returns:
    -------
    int: The updated score after applying the scoring rules.
    """
    # The answer is correct,
    # their score will increase with the increment at their level
    if answer_correct:
        # Increase score based on the level's increment rule
        score += SCORE_RULES[level]["increment"]
        # Print out the message to inform of their current score
        print(f"\nCorrect! You have gained"
              f" {SCORE_RULES[level]['increment']} points.")
    else:
        # Decrease score based on the level's deduction rule
        score -= SCORE_RULES[level]["deduction"]
        # Ensure the score does not drop below zero
        if score < 0:
            score = 0
        point_lost: int = SCORE_RULES[level]["deduction"]
        # Print out the message to inform of their current score
        print(f"\nIncorrect! You have lost {point_lost} points.")

    print(f"Your current score: {score} points at {level}.")
    # Return updated score
    return score


def display_options(menu_selection: dict) -> str:
    """
    Displays a list of menu options and prompts the user to select one.

    This function prints out all the available options from the provided menu
    selection dictionary, including descriptions for each option if available.
    It prompts the user to enter a choice, validates that the choice is within
    the valid range, and returns the selected option.

    Arguments:
    ---------
    menu_selection (dict): A dictionary where keys are option identifiers and
                           values are option names or descriptions.

    Returns:
    -------
    choice (str): The selected menu option.
    """
    print("\nChoose an item:")
    # Clear any previous options from the list
    options_list.clear()

    # Display menu options and their descriptions
    for menu_choice, menu_content in menu_selection.items():
        # Add the option identifier
        # to the options list for subsequent functions
        options_list.append(menu_choice)

        # Validates if this menu content
        # (value in the dictionary) is in SCORE_RULES
        if menu_content in SCORE_RULES:
            # Print the description along with the different levels
            level_description: str = SCORE_RULES[menu_content]["description"]
            print(f"-({menu_choice}) {menu_content} ----- {level_description}")
        else:
            # Print out as usual like menu
            print(f"-({menu_choice}) {menu_content}")

    # Define the valid range for options
    minimum_valid_range: int = options_list[0]
    maximum_valid_range: int = options_list[-1]
    print(f"\nYou can select by entering "
          f"{minimum_valid_range} to {maximum_valid_range}")

    # Prompt user for a choice and validate input
    choice: str = input("Enter your choice: ").upper().strip()
    while choice not in options_list:
        # Inform the users about the valid range
        print(f"\nInvalid selection. The input must be between "
              f"{minimum_valid_range} and {maximum_valid_range}.")
        choice: str = input("Enter your choice again: ").upper().strip()

    # Return the choice
    return choice


def ask_question(difficulty: str, score: int, player_life: int) -> (bool, int):
    """
    Selects and presents a random question from the given difficulty level,
    and processes the user's answer.

    This function randomly selects a question from the
    specified difficulty level
    that has not been asked yet, displays it along with its options,
    and prompts the user to answer.
    It validates the user's input and returns whether the
    answer was correct and the number of questions asked.

    Arguments:
    ----------
    difficulty (str): The difficulty level of the questions to select from.
    score (int): The current score of the player.
    player_life (int): The remaining lives of the player.

    Returns:
    -------
    tuple: (bool, int)
        answer == correct_answer (bool): The correctness of the answer.
        question_number (int): The number of questions the user has been asked.
    """
    # Select a random question from the specified difficulty level
    question: dict = random.choice(questions[difficulty])
    # Ensure the selected question has not been asked before
    while question in question_list:
        question = random.choice(questions[difficulty])

    # Store the question into the question_display for subsequent functions
    question_display: str = question["question"]

    # Add the question to the list of asked questions
    question_list.append(question)

    # Determine the current question number
    question_number: int = len(question_list)

    # Display the question number and question
    print(f"\n{question_number}: {question_display}")

    # Display the options
    for options in question["options"]:
        print(options)

    correct_answer: str = question["answer"]
    print(f"\nYour current score is {score}")

    # Provide textual feedback to inform players about their current status
    print(f"Remaining lives: {player_life}")
    print(f"Correct answer is {correct_answer}")

    # Get the user's answer and validate it
    answer: str = input(
        "\nWhat is your answer (a, b, c, d): "
    ).upper().strip()
    # Loop until user enters a valid option
    while answer not in QUESTIONS_OPTIONS:
        answer = input(
            "\nInvalid input. Enter your answer again (a, b, c, d): "
        ).strip().upper()
    print(f"Correct answer is {correct_answer}")

    # Return whether the user's answer was correct and the question number
    return answer == correct_answer, question_number


def difficulty_selection() -> str:
    """
    Manages the game flow by allowing the user to select a difficulty level,
    start the game, and handle game progression.

    This function prompts the user to select a difficulty level
    and provides a name.It then starts the game by asking questions
    based on the selected difficulty.
    The function handles scoring, life management, and user choices
    after every 5 questions. The game continues until the user
    runs out of lives, answers all questions, or chooses to stop.


    Returns:
    -------
    str: The name of the user who played the game.
    """
    # Initially define the score as 0
    score: int = 0

    while True:
        # Display difficulty options and get user's choice
        difficulty_choice: str = display_options(menu_option_difficulty)
        # Get the level from the difficulty choice
        level: str = menu_option_difficulty[difficulty_choice]
        # Get initial lives based on difficulty
        player_life: int = SCORE_RULES[level]["life_number"]
        # Prompt the user for their name
        user_name: str = get_valid_name()
        # Provide these messages to inform them about their current status
        print(f"\nHello {user_name}! You selected {level}, and start with "
              f"{player_life} lives.")

        while True:
            # Check if the player_life is > 0
            if player_life > 0:
                # Call the function and answer the question
                correct, question_number \
                    = ask_question(level, score, player_life)
                # Update the score
                score = scoring_system(correct, level, score)

                # Check if it's time to ask if the user wants to continue
                if (question_number % 5 == 0 and
                        question_number != 0 and
                        question_number != 15):
                    # Receive the continue option from continue_function
                    continue_option: bool = continue_function(question_number)
                    # If the continue_option is False, end the game
                    if not continue_option:
                        print(f"\nCongratulations ({user_name})! You have "
                              f"finished the game. "
                              f"Your final score is {score}.")
                        if score >= 20:
                            print("You can redeem a reward in the menu.")
                        user_information[user_name]\
                            = {"score": score, "level": level}
                        return user_name

                # Check if all questions have been answered
                if question_number >= TOTAL_QUESTION:
                    user_information[user_name] \
                        = {"score": score, "level": level}
                    print(f"\nCongratulations ({user_name})! "
                          f"You have finished "
                          f"all the questions. "
                          f"Your final score is {score}.")
                    return user_name

                # Handle wagering if the answer was correct
                if correct:
                    score = wager_system(score, level, player_life)

                # Deduct life if score is zero
                if score == 0:
                    print(f"\nWarning: Your score is {score}.")
                    print("You are going to lose one life instead of points.")
                    player_life = life_system(player_life)
                    print("Be careful!"
                          " If your lives reach 0, the game is over.")
            # End the game if lives are exhausted
            else:
                print(f"You don't have enough "
                      f"lives ({player_life}). Game over!")
                user_information[user_name] = {"score": score, "level": level}
                return user_name


# Dictionary mapping difficulty levels to their specific question bank
questions: dict = {

    # Questions for the Beginner difficulty
    "Beginner level": beginner_questions,

    # Questions for the Medium difficulty
    "Medium level": medium_level_questions,
    "Hard level": hard_level_questions,  # Questions for the Hard difficulty
    "Mixed level": mixed_level_questions,  # Questions for the Mixed difficulty
}

# Dictionary mapping menu options to their actions
menu_option: dict[str, str] = {
    "1": "Difficulty selection",  # Option to select the difficulty level
    "2": "View history",  # Option to view game history

    # Redeem it if socre >= 20
    "3": "Redeem a mysterious reward (require 20 points)",
    "4": "Rules",  # Option to display the rules of the game
    "5": "Quit the game",  # Option to quit the game
}

# Dictionary mapping menu selection numbers to difficulty levels
menu_option_difficulty: dict[str, str] = {
    "1": "Beginner level",  # Difficulty level for Beginners
    "2": "Medium level",  # Difficulty level for Medium
    "3": "Hard level",  # Difficulty level for Hard
    "4": "Mixed level",  # Difficulty level for Mixed
}

# Dictionary containing scoring rules for each difficulty level
SCORE_RULES: dict[str, dict[str, int | str]] = {
    "Beginner level": {
        "increment": 4,  # Points gained for a correct answer
        "deduction": 2,  # Points lost for an incorrect answer
        "life_number": 4,  # Number of lives at the start
        "description": "Start with 4 lives, "
                       "gain 4 points for correct answers, "
                       "lose 2 points for incorrect answers.",
    },
    "Medium level": {
        "increment": 3,  # Points gained for a correct answer
        "deduction": 3,  # Points lost for an incorrect answer
        "life_number": 3,  # Number of lives at the start
        "description": "Start with 3 lives,"
                       " gain 3 points for correct answers, "
                       "lose 3 points for incorrect answers.",
    },
    "Mixed level": {
        "increment": 3,  # Points gained for a correct answer
        "deduction": 3,  # Points lost for an incorrect answer
        "life_number": 3,  # Number of lives at the start
        "description": "Start with 3 lives, "
                       "gain 3 points for correct answers, "
                       "lose 3 points for incorrect answers.",
    },
    "Hard level": {
        "increment": 2,  # Points gained for a correct answer
        "deduction": 4,  # Points lost for an incorrect answer
        "life_number": 2,  # Number of lives at the start
        "description": "Start with 2 lives, gain 2 points"
                       " for correct answers, "
                       "lose 4 points for incorrect answers.",
    },
}

# List of valid answer options for questions
QUESTIONS_OPTIONS: list = ["A", "B", "C", "D"]

# List of valid options for wagering and continue option
VALID_WAGER_OPTIONS: list = ["Y", "N"]

# Minimum amount of points that can be wagered
MINIMUM_WAGER_AMOUNT: int = 1

# List to store options displayed in the menu
options_list: list = []

# List to track the questions that have been asked
question_list: list = []

# Dictionary to store user information, including scores and levels
user_information: dict = {}

# Constants for username length validation
MAXIMUM_CHARACTERS: int = 8
MINIMUM_CHARACTERS: int = 1

# Flag to control the main game loop
running: bool = True

# Variable to store the current user's name
user_name = None

# Total number (constant) of questions in the game
TOTAL_QUESTION: int = 15

# Main game loop
while running:
    # Display the menu options and get the user's choice
    option_choice: str = display_options(menu_option)

    # Carrying out corresponding function based on the user's choice
    if option_choice == "1":
        # Start the game with difficulty selection
        user_name = difficulty_selection()
    elif option_choice == "2":
        view_history()  # Display the game history
    elif option_choice == "3":
        # Redeem a mysterious reward if applicable
        mysterious_reward(user_name)
    elif option_choice == "4":
        display_rules()  # Display the rules of the game
    elif option_choice == "5":
        print("Game is quitting.........")  # Print a quitting message
        running = False  # End the main game loop
