from math import log2
from collections import defaultdict
from game.wordle import Wordle, LetterStatus

def _get_words_entropy(words: list[str]) -> list[float]:
    wordle = Wordle(words)
    total_words = len(words)
    entropy: list[float] = [0] * total_words

    for i, target in enumerate(words):
        wordle.start(target)
        frequencies: dict[tuple(LetterStatus), int] = defaultdict(int)
        for guess in words:
            frequencies[tuple(wordle.guess(guess))] += 1

        for count in frequencies.values():
            probability = count / total_words
            entropy[i] -= probability * log2(probability)

    return entropy

def _word_matches_guess_outcome(word: str, guess: str, outcome: list[LetterStatus]) -> bool:
    wordle = Wordle([word])
    wordle.start(word)
    return wordle.guess(guess) == outcome

def get_best_word(words: list[str]) -> str:
    entropy = _get_words_entropy(words)
    max_index = 0
    for i, value in enumerate(entropy):
        if value > entropy[max_index]:
            max_index = i
    return words[max_index]

def filter_words(words: list[str], guess: str, outcome: list[LetterStatus]) -> list[str]:
    return [
        word
        for word in words
        if _word_matches_guess_outcome(word, guess, outcome)
    ]
