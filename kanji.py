"""
Struct that handles the storing of the kanji data for usablity.
"""

class Kanji:
    """
    Class for handeling the Kanji data.
    """
    def __init__(self, kanji_char, on_reading, kun_reading, meaning):
        self.kanji_char = kanji_char
        self.on_reading = on_reading
        self.kun_reading = kun_reading
        self.meaning = meaning
