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
    # print("test: This is a test for the correct word: " + password)
    return password


def get_n_overlap(password, n):
    if n == 0:
        return []

    overlapping_words = []
    for word in word_list:
        overlap = set(password) & set(word)
        if len(overlap) == n and word != password:
            overlapping_words.append(word)

    recursive_call = get_n_overlap(password, n - 1)
    overlapping_words.extend(recursive_call)
    return overlapping_words


# Modified get_matching_words function
# current_n is the filter for what words are passed in.
# n is how many words are to be gathered I believe?
# something is wrong with this function. I need to call to call it 5 times and reuse code.


def get_matching_words(password, word_list, n, current_n=0, result=None):
    if result is None:
        result = {i: [] for i in range(n + 1)}

    if current_n > n:
        return result

    matching_words = [
        word
        for word in word_list
        if len(set(password) & set(word)) == current_n and word != password
    ]
    result[current_n] += matching_words
    return result


# Modified overlapping dictionary to store the result in a variable
overlapping = {}


# Form an outline of what you need.
# What parameters does my function need? -> It needs the password and it needs the game words list. It also needs to know the number of letters to search for.
# What is the goal of my function?
# I need to have the function evaluate the iterated word in the gamewords list and compare it to the password to see how many matching letters there are.
# After the function has gotten how many matching letters there are, it needs to put it in a container that holds words with the same amount of matching letters.
# From those containers I would want to randomly select three words. Another option would be to shuffle the containers of words and pick the first three.
# What is the base case of this function? It would be n being at 0 right? 0 matching letters? It cannot be less.

# DRIVER CODE ---------------------
password = get_password(word_list)
print("Test for password from the driver code: " + password)
overlapping = {}

for i in range(len(password)):
    overlapping[i] = get_n_overlap(password, i)

zero_matching_words = get_matching_words(
    password, word_list, 3, current_n=0, result=None
)
print("This is zero matching_words ", zero_matching_words[0])

one_matching_words = get_matching_words(
    password, word_list, 3, current_n=1, result=None
)
print("This is one words set", one_matching_words[1])

two_matching_words = get_matching_words(
    password, word_list, 3, current_n=2, result=None
)
print("This is two words set", two_matching_words[2])

three_matching_words = get_matching_words(
    password, word_list, 3, current_n=3, result=None
)
print("This is three words set", three_matching_words[3])

four_matching_words = get_matching_words(
    password, word_list, 3, current_n=4, result=None
)
print("This is four words set", four_matching_words[4])


def main():
    # introduce()
    get_word_list()
    # password defined on line 149
    password = get_password(word_list)
    get_matching_words(password, word_list, 3, current_n=0, result=None)


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
