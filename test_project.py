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

