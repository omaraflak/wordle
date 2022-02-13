from game.wordle import Wordle, LetterStatus

_INT_TO_STATUS = {
    1: LetterStatus.GOOD_LETTER_GOOD_POSITION,
    2: LetterStatus.GOOD_LETTER_WRONG_POSITION,
    3: LetterStatus.WRONG_LETTER
}

def _make_result_from_int(n: int) -> list[LetterStatus]:
    return [_INT_TO_STATUS[int(i)] for i in str(n)]

def test_guess():
    wordle = Wordle(["abcd", "abef", "bgyu"])
    wordle.start("abef")
    assert wordle.guess("abef") == _make_result_from_int(1111)
    assert wordle.guess("abcd") == _make_result_from_int(1133)
    assert wordle.guess("aabb") == _make_result_from_int(1323)
    assert wordle.guess("dddd") == _make_result_from_int(3333)
    assert wordle.guess("eeee") == _make_result_from_int(3313)

def test_guess_double():
    wordle = Wordle(["abcd", "abef", "bgyu", "aabc"])
    wordle.start("aabc")
    assert wordle.guess("aabc") == _make_result_from_int(1111)
    assert wordle.guess("abcd") == _make_result_from_int(1223)
    assert wordle.guess("abaa") == _make_result_from_int(1223)
    assert wordle.guess("bbbc") == _make_result_from_int(3311)