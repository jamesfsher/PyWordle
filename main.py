import csv
import pandas as pd
import random

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
    current_word = select_word().lower()
    print(current_word)
    current_wordle = list(current_word)
    try_counter = 0
    progressed_word = ['', '', '', '', '']
    correct_letter_wrong_place = [] 
    AVAILABLE_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters_remaining = AVAILABLE_LETTERS
    while try_counter <= 5:
        guess(try_counter) = input("Guess a word: ").lower()
        for letter in guess:
            if letter in current_wordle:
                if guess.index(letter) == current_wordle.index(letter):
                    progressed_word[guess.index(letter)] = letter.upper()
                else:
                   correct_letter_wrong_place.append(letter)                           
            else:
                try:
                    letters_remaining.remove(letter.upper())
                except ValueError:
                    continue
        print("Current progress: ", progressed_word)
        print("Correct letters wrong place: ", correct_letter_wrong_place)
        print("Letters remaining: ", letters_remaining)





def select_word():
    ...
    # Randomly select a word from csv file containing 5 letter words
    words = ['Above', 'About', 'Abuse']
    # with open('list_of_words.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     return random.choice(list(reader))
    return random.choice(words)


def check_guess():
    ...






if __name__ == '__main__':
    main()