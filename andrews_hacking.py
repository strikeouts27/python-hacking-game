# IMPORTS
import sys
import random

"""
https://inventwithpython.com/bigbookpython/project33.html
basically game_words is where I am telling python to grab the 15 words used fo the hacking mini game.

Players select from this list of words hoping to guess the password.

I need 3 words that have 0 letters in common with the password
and another 3 words that have 1,2,3,4 letters in common with the password respectivley and the password all stored in a way that python can know about it.
after that I need to make a game board that will display the characters and the words on the screen.
"""
# -----------------------------------------------------------------#

# CONSTANTS
# garbage characters system
garbage_chars = "~!@#$%^&*()_+-={}[]|;:,.<>?/"


def introduce():
    name = input("To start the game please type in your player name: ")
    print(
        f"Agent {name}! The evil dictator Kim Jong Un has decided to launch the nukes. All of humanity's hopes rest on your shoulders to hack into the system and stop the launch. You will see a series of possible words that are the password. Use our hint system software to determine if you are close to guessing the password. The hint system will tell you the letters that the word choice and the password have in common as well as positioning. You are our last hope.... \n Okay agent {name}, here are list of the possible passwords. \n Type in the word from the available list of words that you believe is the password."
    )


def final_game_word(game_word_set):
    one_game_word = random.choice(game_word_set)
    return one_game_word


def game_row_generator(final_game_words):
    row = []
    starting_garbage_number = random.randint(2, 8)

    for i in range(starting_garbage_number):
        print(random.choice(garbage_chars), end="")
        starting_garbage_characters = row.append(random.choice(garbage_chars))

    for ending_characters in range(9 - range(row)):
        random.choice(garbage_chars),
        row.append(ending_characters)

    x = (
        starting_garbage_characters
        + str(final_game_word(game_word_set))
        + str(ending_characters)
    )
    (
        str(starting_characters)
        + str(final_game_word(game_word_set))
        + str(ending_characters)
    )
    return x


def generate_game_row(final_game_words):
    game_word_row = (
        str(hex_number())
        + str(final_game_word(final_game_words))
        + str(game_row_generator(final_game_words))
    )
    return game_word_row


def get_word_list():
    with open("sevenletterwords.txt", "r") as file:
        word_list = [line.strip().upper() for line in file.readlines()]
        random.shuffle(word_list)
        # test print(full_list_of_words)
    return word_list


# This function generates a password for the player to guess.
def get_password(word_list):
    password = random.choice(word_list)
    print("test: This is a test for the password: ", password)
    return password


def get_n_overlap(password, n):
    overlapping_words = []
    x = 0
    for word in word_list:
        if x < 3:
            overlap = set(password) & set(word)
            if len(overlap) == n and word != password:
                overlapping_words.append(word)
                x += 1
                if x == 3:
                    break
    return overlapping_words


def hex_number():
    number = random.randint(1000, 9999)
    hex_number = hex(number)
    return hex_number


# DRIVER CODE ---------------------
# these lines of code are here to prevent not defined issues.


# password = get_password(word_list)
# word_list = get_word_list()
word_list = get_word_list()
password = get_password(word_list)
# word_list = get_word_list()

game_words_dictionary = {}
game_words = []
# we can target keys in a dictionary with variables!
# I want to use this technique once I get all three of them in there.

game_words_dictionary[0] = get_n_overlap(password, 0)
game_words_dictionary[1] = get_n_overlap(password, 1)
game_words_dictionary[2] = get_n_overlap(password, 2)
game_words_dictionary[3] = get_n_overlap(password, 3)
game_words_dictionary[4] = get_n_overlap(password, 4)

# hex()+ garbage characters + random placement of game word + garbage characters
# the iter function runs out after sum is used.
game_word_set = sum(game_words_dictionary.values(), [])
game_word_set.append(password)
# all of the game words shuffled and shuffling by itself will not hold values.
random.shuffle(game_word_set)
print("This is the game_word_set", game_word_set)

one_game_word = final_game_word(game_word_set)


x = generate_game_row(game_word_set)
print(x)

x = final_game_word()
print(x)


def main():
    rows = 16
    columns = 2
    tries = random.randint(3, 5)
    # introduce()
    # word_list = get_word_list()
    # password = get_password(word_list)


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
# random will change things in place. there is no need for variables.
