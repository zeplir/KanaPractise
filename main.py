# Author Leo Katakalidis Rydh, 2025. @Zeplir on Github

# imports
import json

# <------------ TODO ------------>
# Add a limit to how many characters that want to be practiced
# Press q to quit anytime
# Handle incorrect input on gamemode 
# Handel incorrect input on answer check.
# <------------------------------>

# Global consts
class Global:
    #KATAKANA_CSV: str = './csv/katakana.csv'
    #HIRAGANA_CSV: str = './csv/hiragana.csv'
    KATAKANA_JSON: str = './json/katakana.json'
    HIRAGANA_JSON: str = './json/hiragana.json'

def main():
    data: list[dict[str, str]] = get_json(gamemode_choice()) # is accesed with data[index_num][key] prints value of key
    print(data[0]['katakana'])

# We read it all to a list, might not be the best for memory management, but the list is not so long
# but it makes handeling the data a lot easier, so I ma going with that anyway
def get_json(path: str) -> list[dict[str, str]]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def gamemode_choice() -> str:
    print("ようこそ / Youkoso!\n\nWelcome to my japanese quiz! Please select what you want to practise!")
    user_choice = input("For hiragana enter 'h' and for katakana enter 'k': ")
    match user_choice:
        case 'h':
            return Global.HIRAGANA_JSON
        case 'k':
            return Global.KATAKANA_JSON
        case _: # loop until 'q' quit or right accepted answer is found.
            return 

if __name__ == '__main__':
    main()