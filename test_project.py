import pytest
from project import end_game, select_word, get_user_guess, update_progress

def test_update_progress():
    guess = "apple"
    current_word = "ample"
    progressed_word = ['', '', '', '', '']
    letters_remaining = list('abcdefghijklmnopqrstuvwxyz')
    correct_letter_wrong_place = []

    update_progress(guess, current_word, progressed_word, letters_remaining, correct_letter_wrong_place)

    assert progressed_word == ['a', '', 'p', 'l', 'e']
    assert "a" not in letters_remaining
    assert "p" in correct_letter_wrong_place
    assert "p" not in letters_remaining
    assert "l" not in letters_remaining
    assert "e" not in letters_remaining
