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


    # Code that created csv from .txt list of words
    # new_list = []
    # with open('list_of_words.txt', 'r') as file:
    #     words = file.read().splitlines()

    # with open('output_file.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     for word in words:
    #         writer.writerow([word])

def select_word():
    ...
    # Function to select a word from a long list of words (create as separate text file?)
    # Randomly select a word
    # Store as a variable in current session
    with open('list_of_words.csv', 'r') as file:
        reader = csv.reader(file)
        return random.choice(list(reader))
    





if __name__ == '__main__':
    main()