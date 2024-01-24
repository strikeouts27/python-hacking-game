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


# this function will gather in the game words from the sevenletterwords.txt file
def get_word_list():
    with open("sevenletterwords.txt", "r") as file:
        word_list = [line.strip().upper() for line in file.readlines()]
        random.shuffle(word_list)
        # test print(full_list_of_words)
    return word_list


# This function generates a password for the player to guess.
def get_password(word_list):
    password = random.choice(word_list)
    # print("test: This is a test for the password: ", password)
    return password


def get_game_word_set(word_list, password):
    game_words_dictionary = {}
    game_words = []
    # we can target keys in a dictionary with variables!
    # I want to use this technique once I get all three of them in there.
    # place the words that have 0 letters in common into the dictionary at the 0 index.
    game_words_dictionary[0] = get_n_overlap(word_list, 0, password)
    # now do the same things for the other words
    game_words_dictionary[1] = get_n_overlap(word_list, 1, password)
    game_words_dictionary[2] = get_n_overlap(word_list, 2, password)
    game_words_dictionary[3] = get_n_overlap(word_list, 3, password)
    game_words_dictionary[4] = get_n_overlap(word_list, 4, password)
    # now we combine these values in the dictionary togather into a single list.
    game_word_set = sum(game_words_dictionary.values(), [])
    game_word_set.append(password)
    random.shuffle(game_word_set)
    print("This is the game words dictionary. " + str(game_word_set))
    print("This is the password for the game. " + str(password))
    return game_word_set


# the game words need to have a certain amount of characters in common with the password.
def get_n_overlap(word_list, n, password):
    overlapping_words = []
    x = 0
    for word in word_list:
        if x < 3:
            # if the number of matching letters is the same as n than append that word to the list.
            overlap = set(password) & set(word)
            if len(overlap) == n and word != password:
                overlapping_words.append(word)
                x += 1
                if x == 3:
                    break
    return overlapping_words


# I want the function to generate a hex number.
# game row
# Ox217_ _ _ _ _ _ _ _ _ _ _
def hex_number():
    number = random.randint(1000, 1500)
    hex_number = hex(number)
    return hex_number


# python gotchas with mutable data types workaround
# for some reason python is not iterating past the first word.


# do I need to return just one game word? or one game word that iterates over the dictionary. <-


def game_word_selection(game_word_set):
    gamewords = []
    while len(gamewords) < 16:
        for word in game_word_set:
            game_word_set.pop()
            garbageword = garbage_character_filler(word)
            gamewords.append(garbageword)
        return gamewords


def garbage_character_filler(game_word):
    character_row_limit = 16
    garbage_row = []
    garbage_row.append(hex_number())
    characters_left = character_row_limit - len(garbage_row[0]) - len(game_word)
    insertion = random.randint(1, characters_left)
    garbage_chars = "~!@#$%^&*()_+-={}[]|;:,.<>?/"
    garbage_row.extend(random.choices(garbage_chars, k=5))
    garbage_row.insert(insertion, game_word)
    game_row = "".join(garbage_row)
    return game_row


# DRIVER CODE ---------------------
# these lines of code are here to prevent not defined issues.


def main():
    introduce()
    word_list = get_word_list()
    password = get_password(word_list)

    # on this line of code we establish the game words to be used for the game session.
    game_word_set = get_game_word_set(word_list, password)

    # we need to determine which game word python will use one at a time without duplicates.
    game_rows = game_word_selection(game_word_set)
    print(game_rows)



# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
# random will change things in place. there is no need for variables.
