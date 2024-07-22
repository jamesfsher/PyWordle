import pytest
from unittest.mock import patch, mock_open
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

@patch('project.end_game')
@patch('project.select_word', return_value=("apple", ["apple", "ample", "apply"]))
@patch('project.get_user_guess', return_value="apple")
@patch('project.is_game_won')
@patch('project.update_progress')
def test_play_round(mock_update_progress, mock_is_game_won, mock_get_user_guess, mock_select_word, mock_end_game):
    from project import play_round, print_game_state, user_play_again

    play_round(
        mock_select_word,
        mock_get_user_guess,
        mock_update_progress,
        print_game_state,
        mock_is_game_won,
        mock_end_game,
        user_play_again
    )

    assert mock_update_progress.called
    assert mock_is_game_won.called
    assert mock_get_user_guess.called
    assert mock_select_word.called
    assert mock_end_game.called

@patch('builtins.open', new_callable=mock_open, read_data="apple\nample\napply\n")
@patch('csv.reader', return_value=[["apple"], ["ample"], ["apply"]])
def test_select_word(mock_csv_reader, mock_open):
    word, all_words = select_word()
    assert word in ["apple", "ample", "apply"]
    assert all_words == ["apple", "ample", "apply"]
