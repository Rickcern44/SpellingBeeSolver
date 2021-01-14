# Imports
import string
import re
from pathlib import Path
import os.path as path

# Initilize the text file and make it into a list to be used later
# Uncomment the larger dictionary file to get a larger result set. Only one can be used a a time

txt_file = open('Words/10000_word_list.txt')
# txt_file = open('Words/EnglishWords.txt')



words_list = []

for word in txt_file:
    if len(word) > 3 and len(word) < 8:
        words_list.append(str(word.strip().lower()))

# Global Variables

alphabet = list(string.ascii_lowercase)

# With this set there should be 166 posibilities


# Functions


def SolveBee(center_letter, other_letters):

    alphabet = list(string.ascii_lowercase)
    s = set(other_letters)
    bad_letters = [x for x in alphabet if x not in s]

    acceptable_words = []

    for word in words_list:
        if center_letter in word:
            if len(word) > 3:
                if any(letter in bad_letters for letter in word) == False:
                    acceptable_words.append(word)

    return acceptable_words


def PrintToFile(center_letter, rem_letters, final_list):
    # Check if the file exists if it does not create it. If it does tell the user.
    gen_file = Path(f'Solutions/{rem_letters} -- {len(final_list)}.txt')
    if path.exists(gen_file):
        return 'A file with that name has already been created try another solution!'
    else:
        f = open(f'Solutions/{rem_letters} -- {len(final_list)}.txt', 'wt')

        # Write the center letter and the rem letters
        f.write(f'The Center letter is: {center_letter}\n')
        f.write(f'\nThe remaining letters are: {rem_letters}\n')
        f.write(f'\nThe total number of possibilities is: {len(final_list)}\n')
        for word in final_list:
            f.write(f'{word}\n')
        f.close()

        return 'The file was created and is in the solutions folder.'


# Main Function
def main():


    # Place the letter combination here. Later this weill be switched to user input.
    center_letter = 'a'
    rem_letters = ['d', 'l', 'g', 'e', 'i', 'h', 'a']

    # Create the final list with the Solver Function
    final_list = SolveBee(center_letter, rem_letters)

    # Create the file and give the user a message based on the file creation status.
    message = PrintToFile(center_letter, rem_letters, final_list)

    print(message)

    # print(f'Total number of acceptable words: {len(final_list)}')
    # print(final_list)


if __name__ == "__main__":
    main()
