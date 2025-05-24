"""
File for the kanij gamemode logic.
"""

import json
import random
import os
import platform
from pathlib import Path
from kanji import Kanji

class PlayKanji:
    """
    I decided that it should be OOP idk, what to say other than that :P
    """

    def __init__(self):
        self.path_to_json = Path(__file__).resolve().parent / "json/kanji.json"
        self.kanji_data: list[Kanji] = []
        self.correct_guesses: int = 0
        self.amount_of_kanjis: int = self.get_user_choise()
        self.play_game()

    def get_user_choise(self) -> int:
        tries: int = input("Please enter how many Kanji you want to practise: ")
        return int(tries)

    def get_json_data(self) -> str:
        with open(self.path_to_json, 'r', encoding='utf-8') as f:
            return json.load(f)

    def parse_json_data(self, raw_json_data):
        for data in raw_json_data:
            self.kanji_data.append(Kanji(data["kanji"],
                                    data["on-readings"],
                                    data["kun-readings"],
                                    data["meaning"]))
            random.shuffle(self.kanji_data)

    @staticmethod
    def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def play_game(self):
        PlayKanji.clear_screen()
        raw_data = self.get_json_data()
        self.parse_json_data(raw_data)
        correct_counter: int = 0

        if self.amount_of_kanjis > len(self.kanji_data):
            self.amount_of_kanjis = len(self.kanji_data)

        for index, kanji in enumerate(self.kanji_data):
            if index == self.amount_of_kanjis:
                percentage: float = (correct_counter / self.amount_of_kanjis) * 100
                print(f"\nYou got {correct_counter}/{index}, ({round(percentage, 1)}%) well done!")
                print("Thank you for playing!")
                exit()
            user_answer = input(f"{kanji.kanji_char}: ")
            if user_answer.lower() == kanji.meaning:
                correct_counter += 1
                print("Correct!\n")
            elif user_answer.lower() == 'q':
                print("Quitting…")
                exit()
            else:
                print(f"Incorrect, {kanji.kanji_char} has the meaning {kanji.meaning}\n")
