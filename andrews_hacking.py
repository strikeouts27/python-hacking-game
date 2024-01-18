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


# I want the function to generate a hex number.
# game row
# Ox217_ _ _ _ _ _ _ _ _ _ _
def hex_number():
    number = random.randint(1000, 1500)
    hex_number = hex(number)
    return hex_number


def game_word_selection(game_word_set, already_selected_words):
    game_words_counter = 0
    # game_word_set contains all of the function calls where python gathers words that have 0,1,2,3,4 letters in common with the password.
    # we evaluate if the game word has been selected already. if not, than we return it so that we can call this function
    # with other functions and join the the hex memor address + the game word+ and some garbage characters. 
    for game_word in game_word_set:
        if game_word not in already_selected_words:
            already_selected_words.append(game_word)
            return game_word

        # If the game word is already selected I need python to try again to find a game word that is not already used.
        elif game_word in already_selected_words:
            for game_word in range(500):
                if game_word not in already_selected_words:
                    game_word = random.choice(game_word_set)
                    already_selected_words.append(game_word)
                    return game_word


# I than want the function to generate a random number indicating the starting position of the garbage characters and fill the row after the hex number. In this case lets say 4
# Ox217 _ _ _ _ _ _ _ _ _ _ _
# I than want the game word to be generated and appended to the list.
# I than want the garbage character filler to fill the remainder of the row with garbage characters.
# i need 16 rows not one row generator


def garbage_character_filler(one_game_word):
    character_row_limit = 16
    game_words_being_used = 16
    garbage_row = []
    garbage_row.append(hex_number())
    print(
        "This is the current state of garbage_row with just the hex number", garbage_row
    )
    garbage_placement = random.randint(2, 8)
    for i in range(garbage_placement):
        garbage_char = random.choice(garbage_chars)
        print(garbage_char, end="")
        garbage_row.append(garbage_char)

    # Total Length = (Len of hex string) + (Number of garbage chars) + (Len of keyword)
    length = len(garbage_row[0]) + len(garbage_row[1:-1]) + len(garbage_row[-1])

    for _ in range(character_row_limit - length):
        garbage_char = random.choice(garbage_chars)
        garbage_row.append(garbage_char)

    print(
        "After the random garbage character placement garbage row looks like this",
        garbage_row,
    )
    result = garbage_row
    return result


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


# DRIVER CODE ---------------------
# these lines of code are here to prevent not defined issues.

# OUTLINE
# INTRODUCE THE GAME : COMPLETED
# ESTABLISH THE GAME WORDS AND THE PASSWORD
# GET THE GAME BOARD ROWS GENERATED
# hex memory + random number of garbage characters + game_word + random garbage characters.


# HAVE THE PLAYER MAKE ATTEMPTS TO GUESS THE PASSWORD
# HAVE A HINT SYSTEM AND A TRIES LEFT SYSTEM
# WIN CONDITION
# LOSING CONDITION


def main():
    introduce()
    word_list = get_word_list()
    password = get_password(word_list)
    print("This is the games password " + password)
    game_word_set = get_game_word_set(word_list, password)
    get_game_word(game_word_set)
    garbage_character_filler(game_word_set)


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
# random will change things in place. there is no need for variables.
