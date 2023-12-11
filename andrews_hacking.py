# IMPORTS
import sys
import random

# -----------------------------------------------------------------#

# CONSTANTS
# garbage characters system
garbage_chars = ["~!@#$%^&*()_+-={}[]|;:,.<>?/"]

# Load the WORDS list from a text file that has 7-letter words.
with open("sevenletterwords.txt") as file:
    word_list = file.readlines()
for i in range(len(word_list)):
    # Convert each word to uppercase and remove the trailing newline:
    word_list[i] = word_list[i].strip().upper()

# -------------------------------------------------------------------#
# FUNCTIONS


def introduce():
    name = input("To start the game please type in your player name: ")
    print(
        f"Agent {name}! The evil dictator Kim Jong Un has decided to launch the nukes. All of humanity's hopes rest on your shoulders to hack into the system and stop the launch. You will see a series of possible words that are the password. Use our hint system software to determine if you are closs to guessing the password. You are our last hope.... \n Okay agent {name}, here are list of the possible passwords. \n Type in the word from the available list of words that you believe is the password."
    )


# from the text file pull out all of the game words.
def get_word_list():
    with open("sevenletterwords.txt", "r") as file:
        word_list = [line.strip().upper() for line in file.readlines()]
        random.shuffle(word_list)
        # test print(full_list_of_words)
    return word_list


# This function generates a password for the player to guess.
def get_password(word_list):
    password = random.choice(word_list)
    # print("test: This is a test for the correct word: " + correct_word)
    return password


# my goal is to use this function to get 3 0 letter matching words and 3 1 letter matching words and 3 2 letter matching words and so on.
# a set of game words that I will actually be using. vs the word_list which is all of the words in the text file.
# count is the number of words that python will collect for each matching letter words.
def get_n_overlap(password, n):
    overlapping_words = []
    for word in word_list:
        overlap = set(password) & set(word)
        if len(overlap) == n and word != password:
            overlapping_words.append(word)
    return overlapping_words

game_words = {}
password = "reverse"

# implemented a for loop to target the dictionary so that 
for i in range(5):
    game_words[i] = get_n_overlap(password, i)

game_words[0] = get_n_overlap(password, 0)
game_words[1] = get_n_overlap(password, 1)
game_words[2] = get_n_overlap(password, 2)
game_words[3] = get_n_overlap(password, 3)
game_words[4] = get_n_overlap(password, 4)


# DRIVER CODE ---------------------


def main():
    introduce()


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
