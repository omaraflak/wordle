from game.words import WORDS
from game.wordle import LetterStatus
from solver.solver import get_best_word, filter_words

_STATUS_MAPPING = {
    "1": LetterStatus.GOOD_LETTER_GOOD_POSITION,
    "2": LetterStatus.GOOD_LETTER_WRONG_POSITION,
    "3": LetterStatus.WRONG_LETTER
}

while True:
    words = WORDS
    string = ""
    while string != "1" * len(WORDS[0]):
        guess = get_best_word(words)
        print(f"guess: {guess}")
        string = input("result (1=green, 2=yellow, 3=grey): ")
        result = [_STATUS_MAPPING[c] for c in string]
        words = filter_words(words, guess, result)
    print()
    print("-" * 30)
    print()