import csv
import pandas as pd
import random
import os
import string

def main():
    print("""
          Welcome to PyWordle!
          Play the game by entering a 5 letter word to try to match one randomly chosen.
          If you get the word right, you win! If you don’t, but any of the letters are in the correct place, you’ll 
          see in “Progressed Word”. If you guess a right letter, but it’s not in 
          the right place, you’ll see it under, “Correct letter wrong place”. 
          With only 5 trys to get it right, think carefully!
          """)
    play_round()


def play_round():
    # Function to play and track a round of 5 
    current_word, all_words = select_word()
    # current_word = "apple"
    current_word.lower()
    # print(current_word)
    term_size = os.get_terminal_size()
    try_counter = 0
    progressed_word = ['', '', '', '', '']
    guesses = []
    correct_letter_wrong_place = [] 
    letters_remaining = list(string.ascii_lowercase)
    while try_counter < 5:
        print('=' * term_size.columns)
        print("Guess #", try_counter + 1)
        guess = user_guess(all_words)
        guesses.append(guess)
        for i in range(len(guess)):
            if guess[i] == current_word[i]:
                progressed_word[i] = guess[i]
                try:
                    letters_remaining[letters_remaining.index(guess[i])] = guess[i].upper()
                except ValueError:
                    continue
            elif guess[i] in current_word:
                correct_letter_wrong_place.clear()
                correct_letter_wrong_place.append(guess[i])
            else:
                try:
                    letters_remaining.remove(guess[i])
                except ValueError:
                    continue

        print("Current progress: ", progressed_word)
        print("Correct letters wrong place: ", correct_letter_wrong_place)
        print("Letters remaining: ", letters_remaining)
        if ''.join(progressed_word) == current_word:
            end_game("winner", guesses, current_word)
        try_counter += 1
    if ''.join(progressed_word) != current_word:
        end_game("loser", guesses, current_word)   



def end_game(result, guesses, current_word):
    # function that takes a "win" or "lose" variable, and ends the game and resets globals to new game mode
    if result == "winner":
        print("You've won! The word was " + current_word)
        print("Your guesses")
        for guess in guesses:
            print(guess)
    elif result == "loser":
        print("You're out of guesses! The word was " + current_word)
        print("Your guesses")
        for guess in guesses:
            print(guess)
    else:
        print("what did you do?")
    while True:
        play_again = input("Do you want to play again (Y or N): ").upper()
        if play_again == "Y" or play_again == "YES":
            play_round()
        elif play_again == "N" or play_again == "NO":
            print("Thanks for playing!")
            exit()
            


def select_word():
    # Randomly select a word from csv file containing 5 letter words
    words = []
    with open('list_of_words.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Reads first item in each row since CSV was set up incorrectly and is 1 word per row
            words.append(row[0].lower())
    return str(random.choice(words)), words

# Function to check validity of user's guess 
def user_guess(all_words):
    guess = input("Guess a word: ").lower()
    while True:
        if len(guess) != 5 or not guess.isalpha():
            guess = input("Invalid input, try again: ")
            continue
        elif guess not in all_words:
            guess = input("Not in list of words, try again: ")
            continue
        else:
            return guess

if __name__ == '__main__':
    main()