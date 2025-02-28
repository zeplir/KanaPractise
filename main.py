# Author Leo Katakalidis Rydh, 2025. @Zeplir on Github

# imports
import json
import random

# <------------ TODO ------------>
# Add 'practise all' option
# Press q to quit anytime
# Handle incorrect input on gamemode 
# Handel incorrect input on answer check.
# Implement train a specific column
# <------------------------------>

# Global consts
class Global:
    #KATAKANA_CSV: str = './csv/katakana.csv'
    #HIRAGANA_CSV: str = './csv/hiragana.csv'
    KATAKANA_JSON: str = './json/katakana.json'
    HIRAGANA_JSON: str = './json/hiragana.json'

def main():
    chosen_gamemode: list[str] = gamemode_choice()
    data: list[dict[str, str]] = get_json(chosen_gamemode[1]) # is accesed with data[index_num][key] prints value of key
    max_limit: int = char_limit()
    game_loop(chosen_gamemode[0], max_limit, data)

# We read it all to a list, might not be the best for memory management, but the list is not so long
# but it makes handeling the data a lot easier, so I ma going with that anyway
def get_json(path: str) -> list[dict[str, str]]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def gamemode_choice() -> list[str]:
    print("\nようこそ / Youkoso!\n\nWelcome to my japanese quiz! Please select what you want to practise!")
    print("You can quit anytime you want be entering 'q!'")
    user_choice = input("For hiragana enter 'h' and for katakana enter 'k': ")
    while True:
        match user_choice:
            case 'h':
                return ['hiragana', Global.HIRAGANA_JSON]
            case 'k':
                return ['katakana',Global.KATAKANA_JSON]
            case 'q!':
                print("Exiting the program, thanks for playing!")
                exit()
            case _: # loop until 'q' quit or right accepted answer is found.
                user_choice = input("Incorrect input, please try again, 'h'/'k': ")

# Improve error checking.
def char_limit() -> int:
    user_choice: str = input("How many characters do you want to train?: ")
    if user_choice.isdigit():
        return int(user_choice)
    else:
        return 1

def game_loop(game_mode: str, max_len: int, data:list[dict[str, str]]):
    order = list(range(len(data)))
    random.shuffle(order)
    correct_counter: int = 0

    if max_len > len(data):
        max_len = len(data)

    for index, num in enumerate(order):
        if index == max_len:
            print(f"\nYou got {correct_counter} out of {index}, well done!")
            print("Thank you for playing!")
            exit()
        user_answer = input(f"{data[num][game_mode]}: ")
        if user_answer.lower() == data[num]['romanji']:
            correct_counter += 1
            print("Correct!\n")
        elif user_answer.lower() == 'q!':
            print("Quitting…")
            exit()
        else:
            print(f"Incorrect, {data[num][game_mode]}: {data[num]['romanji']}\n")

if __name__ == '__main__':
    main()