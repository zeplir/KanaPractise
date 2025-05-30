"""
File for the kanij gamemode logic.
"""

import json
import random
import os
import platform
from pathlib import Path
from src.kanji import Kanji

class PlayKanji:
    """
    I decided that it should be OOP idk, what to say other than that :P
    """

    def __init__(self):
        """
        Init class for kanji game mode which itself triggers the game.
        """
        self.path_to_json = Path(__file__).resolve().parent / "json/kanji.json"
        self.kanji_data: list[Kanji] = []
        self.correct_guesses: int = 0
        self.amount_of_kanjis: int = self.get_user_choise()
        self.play_game()

    def get_user_choise(self) -> int:
        """
        Asks the user how many kanji they want to practise and returns it as an integer.
        """
        tries: int = input("Please enter how many Kanji you want to practise: ")
        return int(tries)

    def get_json_data(self) -> list[dict]:
        """
        Simply reads the JSON file and returns its content as a list of dictionaries.
        """
        with open(self.path_to_json, 'r', encoding='utf-8') as f:
            return json.load(f)

    def parse_json_data(self, raw_json_data):
        """
        Parses the raw JSON data and creates Kanji objects from it.
        This is mostly done to make the code cleaner and more readable.
        """
        for data in raw_json_data:
            self.kanji_data.append(Kanji(data["kanji"],
                                    data["on-readings"],
                                    data["kun-readings"],
                                    data["meaning"]))
            random.shuffle(self.kanji_data)

    @staticmethod
    def clear_screen():
        """
        Clears the console screen based on the operating system.
        """
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def print_guess_res(self, guess: bool, kanji: Kanji):
        """
        Prints the result of the user's guess for the current kanji.
        """
        if guess:
            print(f"\033[92mCorrect\033[0m, {kanji.kanji_char} has the meaning(s) {kanji.meaning}\n"
                  f"On-readings: {kanji.on_reading}\n"
                  f"Kun-readings: {kanji.kun_reading}\n")
        else:
            print(f"\033[91mIncorrect\033[0m, {kanji.kanji_char} has the meaning(s) {kanji.meaning}\n"
                  f"On-readings: {kanji.on_reading}\n"
                  f"Kun-readings: {kanji.kun_reading}\n")

    def print_final_res(self, correct_counter: int, index: int):
        """
        Prints the final result of the game, showing how many kanji were answered correctly.
        """
        percentage: float = (correct_counter / self.amount_of_kanjis) * 100
        print(f"\nYou got {correct_counter}/{index}, ({round(percentage, 1)}%) well done!")
        print("Thank you for playing!")

    def play_game(self):
        """
        Main game loop that handles the kanji training.
        """
        PlayKanji.clear_screen()
        raw_data = self.get_json_data()
        self.parse_json_data(raw_data)
        correct_counter: int = 0
        was_correct: bool = False

        if self.amount_of_kanjis > len(self.kanji_data):
            self.amount_of_kanjis = len(self.kanji_data)

        for index, kanji in enumerate(self.kanji_data):
            if index == self.amount_of_kanjis:
                self.print_final_res(correct_counter, index)
                exit()
            user_answer = input(f"{kanji.kanji_char}: ")
            for meaning in kanji.meaning:
                if user_answer.lower() == meaning.lower():
                    correct_counter += 1
                    was_correct = True
                    break
            if user_answer.lower() == 'q':
                print("Quitting…")
                exit()
            self.print_guess_res(was_correct, kanji)
            was_correct = False
