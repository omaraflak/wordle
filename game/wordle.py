import random
from enum import Enum
from typing import Optional
from collections import defaultdict

class LetterStatus(Enum):
    GOOD_LETTER_GOOD_POSITION = 1
    GOOD_LETTER_WRONG_POSITION = 2
    WRONG_LETTER = 3

class Wordle:
    def __init__(self, words: list[str]):
        if not self._check_all_same_length(words):
            raise ValueError("All words must have the same size")
        
        if len(words) == 0:
            raise ValueError("You must provide at least one word")

        self.words = words
        self.word_size = len(words[0])
        self.number_of_guesses = 0
        self.target_mapping: dict[str, list[int]] = defaultdict(list)
        self.target = ""

    def start(self, word: Optional[str] = None):            
        self.number_of_guesses = 0
        self.target = word or random.choice(self.words)
        self.target_mapping.clear()
        for i in range(self.word_size):
            self.target_mapping[self.target[i]].append(i)

    def guess(self, word: str) -> list[LetterStatus]:
        if len(word) != self.word_size:
            raise ValueError("Word provided has wrong size")

        result: list[LetterStatus] = [LetterStatus.WRONG_LETTER] * self.word_size
        used: set[int] = set()
        seen: set[int] = set()
        
        for i, (w, t) in enumerate(zip(word, self.target)):
            if w == t:
                result[i] = LetterStatus.GOOD_LETTER_GOOD_POSITION
                used.add(i)
                seen.add(i)

        for i, letter in enumerate(word):
            if i in seen:
                continue

            if letter not in self.target_mapping:
                result[i] = LetterStatus.WRONG_LETTER
                continue

            used_letter = False
            for index in self.target_mapping[letter]:
                if index not in used:
                    used.add(index)
                    result[i] = LetterStatus.GOOD_LETTER_WRONG_POSITION
                    used_letter = True
                    continue
            
            if not used_letter:
                result[i] = LetterStatus.WRONG_LETTER

        self.number_of_guesses += 1
        return result

    @staticmethod
    def _check_all_same_length(words: list[str]) -> bool:
        return all(len(w) == len(words[0]) for w in words)