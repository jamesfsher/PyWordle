import pytest
from project import play_round, update_progress, is_game_won, select_word, get_user_guess, print_game_state, end_game, user_play_again


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


def mock_get_user_guess(all_words):
    return "apple"

def mock_select_word():
    return "apple", ["apple", "ample", "apply"]
