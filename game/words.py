from typing import Optional

def _get_words(filepath: str, size: Optional[int] = None) -> list[str]:
    with open(filepath, "r") as file:
        words = file.read().split("\n")
        if size is not None:
            words = [word for word in words if len(word) == size]
        return words

WORDS = _get_words("game/data/words.txt")
