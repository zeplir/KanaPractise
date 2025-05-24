# Author Leo Katakalidis Rydh, 2025. @Zeplir on Github

import json
import random
from play_kanji import PlayKanji

# Global consts
class Global:
    """
    Global constants for file paths.
    """
    KATAKANA_JSON: str = './json/katakana.json'
    HIRAGANA_JSON: str = './json/hiragana.json'
    KANJI_JSON: str = './json/kanji.json'

def main():
    """
    Main function to run the quiz game.
    """
    chosen_gamemode: list[str] = gamemode_choice()
    if chosen_gamemode[0] == "kanji":
        PlayKanji()
        return
    max_limit: int = char_limit()
    data: list[dict[str, str]] = get_json(chosen_gamemode[1])
    game_loop(chosen_gamemode[0], max_limit, data)


def get_json(path: str) -> list[dict[str, str]]:
    """
    Reads a JSON file and returns its content as a list of dictionaries."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def gamemode_choice() -> list[str]:
    """
    Asks the user to choose a gamemode and returns the chosen mode and the corresponding JSON file path.
    """
    print("\nようこそ / Youkoso!\n\nWelcome to my japanese quiz! Please select what you want to practise!")
    print("You can quit anytime you want be entering 'q!'")
    user_choice = input("For hiragana enter 'h' and for katakana enter 'k' \nor if you want to train kanji enter kanji: ")
    while True:
        match user_choice:
            case 'h':
                return ['hiragana', Global.HIRAGANA_JSON]
            case 'k':
                return ['katakana', Global.KATAKANA_JSON]
            case "kanji":
                return ["kanji", Global.KANJI_JSON]
            case 'q!':
                print("Exiting the program, thanks for playing!")
                exit()
            case _: # loop until 'q' quit or right accepted answer is found.
                user_choice = input("Incorrect input, please try again, 'h'/'k': ")

# Improve error checking.
def char_limit() -> int:
    """
    Asks the user for the number of characters to train and returns it as an integer.
    """
    user_choice: str = input("How many characters do you want to train?: ")
    if user_choice.isdigit():
        return int(user_choice)
    else:
        return 1

def kanji_game_loop():
    pass

def game_loop(game_mode: str, max_len: int, data:list[dict[str, str]]):
    """
    Main game loop that shuffles the data and asks the user for answers.
    Currently only supports hiragana and katakana.
    """
    order: list[str] = list(range(len(data)))
    random.shuffle(order)
    correct_counter: int = 0

    if max_len > len(data):
        max_len = len(data)

    for index, num in enumerate(order):
        if index == max_len:
            percentage: float = (correct_counter / max_len) * 100
            print(f"\nYou got {correct_counter}/{index}, ({round(percentage, 1)}%) well done!")
            print("Thank you for playing!")
            exit()
        user_answer = input(f"{data[num][game_mode]}: ")
        if user_answer.lower() == data[num]['romanji']:
            correct_counter += 1
            print("Correct!\n")
        elif user_answer.lower() == 'q':
            print("Quitting…")
            exit()
        else:
            print(f"Incorrect, {data[num][game_mode]}: {data[num]['romanji']}\n")

if __name__ == '__main__':
    main()
