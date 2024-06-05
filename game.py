#implement error handling (can only use letters)
from string import ascii_letters

ASCII = str(ascii_letters)
MAX_NUMBER_OF_GUESSES = 5
GUESSES = {"incorrect": "🔴", "correct": "🟢", "partially": "🟠"}

class Game:
    """A simple wordle clone"""

    def __init__(self):
        """Random word selected, gues_list set to empty, set game word, set guesses to 0"""
        self.guesses = 0
        self.guess_list = []
        self.current_word = "test"
        self.current_pattern = "-----"
        self.game_over = False
    
    def guess(self):
        """Gets user input and validates it"""
        guess = input('\nGuess #{}: Enter a 5 letter word: '.format(self.guesses))
        guess.toLower()
        letters = guess.split()
        for letter in letters:
            if letter not in ASCII:
                raise ValueError("Invalid letter '{}'".format(letter))
        
        if guess in self.guess_list:
            raise ValueError("Word already guessed! Try again")
        else:
            self.guess_list.append(guess)
            return guess
