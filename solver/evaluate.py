from game.words import WORDS
from game.wordle import Wordle, LetterStatus
from solver.solver import get_best_word, filter_words

def evaluate(iterations: int = 100, verbose: bool = True) -> float:
    wordle = Wordle(WORDS)
    score = 0
    for i in range(iterations):
        wordle.start()
        result = [LetterStatus.WRONG_LETTER] * wordle.word_size
        words = WORDS
        while not all(r == LetterStatus.GOOD_LETTER_GOOD_POSITION for r in result):
            guess = get_best_word(words)
            result = wordle.guess(guess)
            words = filter_words(words, guess, result)
        
        score += wordle.number_of_guesses
        if verbose:
            print(f"Game {i+1}/{iterations} - guesses={wordle.number_of_guesses}, avg={score / (i + 1):.2f}")

    return score / iterations