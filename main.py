import csv

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
    txt_to_csv()
    
def txt_to_csv():
    with open('list_of_words.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(" ") for line in stripped if line) 
        with open('list_of_words.csv', 'w') as out_file:
            writer = csv.writer(out_file) 
            writer.writerow(lines)



def select_word():
    ...
    # Function to select a word from a long list of words (create as separate text file?)
    # Randomly select a word
    # Store as a variable in current session





if __name__ == '__main__':
    main()