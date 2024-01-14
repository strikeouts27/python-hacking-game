# IMPORTS
import sys
import random

@@ -25,6 +24,7 @@ def introduce():
        f"Agent {name}! The evil dictator Kim Jong Un has decided to launch the nukes. All of humanity's hopes rest on your shoulders to hack into the system and stop the launch. You will see a series of possible words that are the password. Use our hint system software to determine if you are close to guessing the password. The hint system will tell you the letters that the word choice and the password have in common as well as positioning. You are our last hope.... \n Okay agent {name}, here are list of the possible passwords. \n Type in the word from the available list of words that you believe is the password."
    )


# this function will gather in the game words from the sevenletterwords.txt file
def get_word_list():
    with open("sevenletterwords.txt", "r") as file:
@@ -33,17 +33,19 @@ def get_word_list():
        # test print(full_list_of_words)
    return word_list


# This function generates a password for the player to guess.
def get_password(word_list):
    password = random.choice(word_list)
    # print("test: This is a test for the password: ", password)
    return password


# This function gets one game word from the game word list to place in the game board row.
# I want this function to randomly select one word from the game_word_set.
def get_game_word(game_word_set):
    one_game_word = random.choice(game_word_set)
    return one_game_word
    return str(one_game_word)


def hex_number():
@@ -55,22 +57,24 @@ def hex_number():
# this function will fill the game row with garbage characters.
def garbage_character_filler(one_game_word):
    garbage_row = []
    garbage_row.append(hex_number())
    garbage_placement = random.randint(2, 8)

    # we will fill the game row with a random amount of garbage characters
    for i in range(garbage_placement):
        print(random.choice(garbage_chars), end="")
        garbage_row.append(random.choice(garbage_chars))

    garbage_row.append(one_game_word)

    for ending_characters in range(9 - len(garbage_row)):
        random.choice(garbage_chars),
        garbage_row.append(ending_characters)
    return str(garbage_row)
        garbage_row.append(random.choice(garbage_chars)),


# the game words need to have a certain amount of characters in common with the password.
    result = "".join(garbage_row)
    return result


# the game words need to have a certain amount of characters in common with the password.
def get_n_overlap(password, n):
    overlapping_words = []
    x = 0
@@ -112,7 +116,7 @@ def get_n_overlap(password, n):
# all of the game words are shuffled and random.shuffle will shuffle the values in place.
# alright the game words are finally established!
random.shuffle(game_word_set)
print("This is a test for game_word_set after the shuffling occurs." + str(game_word_set))
# print("This is a test for game_word_set after the shuffling occurs." + str(game_word_set))
# now I need to get the hex() number, garbage character function run, and than have the game word be put into place.
# garbage character filler requires one game word

@@ -128,11 +132,16 @@ def main():
    introduce()
    # we call these functions to grab the game words list and the password.
    get_word_list()
    get_password(word_list) 
    get_password(word_list)
    one_game_word = get_game_word(game_word_set)
    print("This is the one_game_word", one_game_word)
    garbage_character_filler(one_game_word)


    row_test = garbage_character_filler(one_game_word)
    result = garbage_character_filler(one_game_word)
    print("\n This is the result", result)


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
