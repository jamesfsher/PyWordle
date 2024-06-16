import csv
import pandas as pd
import random
import os
import string

def main():
    ...
    # Call select word to randomly select word
    # Create # of trys counter
    # Create loop that displays current progress towards word (initalize as empty)
    # prompt user for guess
    # Error check guess to make sure its a valid entry
    # compare entry against currently stored word
    # if a letter is correct, and in the correct location, display it capitalized
    # if a letter is correct but in the wrong location, make it lower case
    # if word is correct, diplay so
    # if word is not correct still, reprompt with updated progress and try counter++
    # possibly display all the possible letters also, eliminating the incorrectly guessed ones?
    current_word, all_words = select_word()
    current_word.lower()
    print(current_word)
    term_size = os.get_terminal_size()
    current_wordle = list(current_word)
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
        for letter in guess:
            if letter in current_wordle:
                if guess.index(letter) == current_wordle.index(letter):
                    progressed_word[guess.index(letter)] = letter.upper()
                    try:
                        letters_remaining[letters_remaining.index(letter)] = letter.upper()
                    except ValueError:
                        continue
                else:
                    if letter not in progressed_word: 
                        correct_letter_wrong_place.append(letter)                           
            else:
                try:
                    letters_remaining.remove(letter)
                except ValueError:
                    continue
        print("Current progress: ", progressed_word)
        print("Correct letters wrong place: ", correct_letter_wrong_place)
        print("Letters remaining: ", letters_remaining)
        try_counter += 1

def play_round():
    ...
    # Function to play and track a round of 5 


def select_word():
    ...
    # Randomly select a word from csv file containing 5 letter words
    words = []
    with open('list_of_words.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Reads first item in each row since CSV was set up incorrectly and is 1 word per row
            words.append(row[0])
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