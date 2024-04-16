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
    print(select_word())


def select_word():
    ...
    # Randomly select a word from csv file containing 5 letter words
    with open('list_of_words.csv', 'r') as file:
        reader = csv.reader(file)
        return random.choice(list(reader))
    





if __name__ == '__main__':
    main()