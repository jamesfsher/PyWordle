# PyWordle

#### Video Demo: https://youtu.be/7Bt3I1xpNQM

#### Description:
Overview:

This is my final project for cs50P. It is a copy of NYT's Wordle (https://www.nytimes.com/games/wordle/index.html) that runs in your terminal, built using Python. The game is played just like Wordle, where you have 5 tries to guess a randomly selected 5 letter word. The game will update you on your progress, listing which letters were correct in the correct placement, and correct in the wrong placement. It will also display all available letters to you, removing incorrect letters as you go.

Logic Breakdown:
The code is broken down into several functions. The primary being a function to play a round, 

which can be called continuously to keep playing. I realize this may cause an issue with stack overflow, but that is a problem TODO. Play_round accepts several functions as parameters in order to perform unit testing (described below)

Each time a round is called, the first operation the code performs is to select a random word. I have compiled a list of 430 five letter words. In truth, this is not very many. I pulled this information from this source: https://byjus.com/english/5-letter-words/. 430 words is a very small selection as compared to Wordle, but it is sufficient for a proof-of-concept game. The words are stored in a csv, which is read to a variable each round. This is done to perform user input validation to check if a guessed word is in the list of available words. I believe this can be improved, as it seems redundant to read the file into a csv each time. A random word is chosen from this list.

The user is then prompted to guess a 5 letter word. Each time the user guesses a word, the guess is validated via get_user_guess. The parameters guessed are: length (must be 5 letters), alphanumeric, and in list of available words (as described above). 

If the user guess is valid, it is then appended to a list of guesses (to display when the game ends), and then passed to update_progress. This function will compare each letter of the user's guess to the randomly selected word. For each correct letter, progressed_word is updated in order to display the user's current progress to the correct word. The letter is then capitalized in the variable, "letters_remaining", which keeps a running record of letters the user hasn't guessed. If the letter is not correct, but in the current word, then correct_letter_wrong_place is appended with this letter to show the user that the letter is in the wordle word, but not in the placement they have. Finally, if the letter isn't in the wordle word at all, letters_remaining is updated to remove this letter.

After the user’s progress towards the correct word is analyzed, the game state is then printed via a separate function, print_game_state. This prints the current progress (progressed_word), the correct letters but in the wrong place (correct_letters_wrong_place_), and the letters remaining (letters_remaining).

The game then checks if the user won by comparing the guess to the current wordle word. If so, the function “end_game” with the parameter “winner” is called. If not, the user is prompted to continue guessing, and the guess is checked the same way each time. Once the number of tries has reached 5 and the user has still not guessed the word correctly, end_game is called but with “loser” as the parameter.

end_game states if the user has won or lost, states the current wordle word, and lists all user guesses. It then calls user_play_again(), which allows the user to play again with “Y” or end the game with “N”. If the user wants to keep playing, play_round() is called, all variables are reset, and a new wordle word is selected.



    
