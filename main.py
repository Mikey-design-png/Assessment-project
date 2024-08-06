from question import *
import random


running = True
def get_choice() -> str:
    while running:
        print("\nChoose an item")
        menu_option: dict[str:str] = {
            "1":"Difficulty selection",
            "2":"View history",
            "3": "Quit the game"
        }
        while True:
            try:
                for menu_choice, menu_content in menu_option.items():
                    print(f"-{menu_choice} {menu_content}")
                choice = input("Enter your choice(Press the enter to cancel):").upper()
                if not choice:
                    print("cancel!")
                    break
                if choice not in menu_option:
                    print("Choice is not in options!")
                else:
                    return choice
            except ValueError:
                print("Invalid input")
        break

choice = get_choice()

def difficulty_selection():
    print("1: Beginner level")
    print("2: medium level")
    print("3: Hard level")
    print("4: Mixed level ")
    print("")