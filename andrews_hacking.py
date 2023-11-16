import sys
import random

name = "Python"

# garbage characters system
garbage_chars = ["~!@#$%^&*()_+-={}[]|;:,.<>?/"]
num_of_matches = 3
count = 0


def main():
    introduce()
    word_list = get_word_list()
    password = get_password(word_list)
    game_words = get_game_words(word_list)


# introduce game
def introduce():
    print(
        f"Agent {name}! The evil dictator Kim Jong Un has decided to launch the nukes. All of humanity's hopes rest on your shoulders to hack into the system and stop the launch. You will see a series of possible words that are the password. Use our hint system software to determine if you are closs to guessing the password. You are our last hope.... \n Okay agent {name}, here are list of the possible passwords. \n Type in the word from the available list of words that you believe is the password."
    )


# from the text file pull out all of the game words.
def get_word_list():
    with open("sevenletterwords.txt", "r") as file:
        word_list = [line.strip().upper() for line in file.readlines()]
        # test print(full_list_of_words)
    return word_list


# This function generates a password for the player to guess.
def get_password(word_list):
    password = random.choice(word_list)
    # print("test: This is a test for the correct word: " + correct_word)
    return password

# find 3 0 matching letter words, 3 1 matching letter words, 3 2 matching letter words,
def get_game_words(word_list, count):
    password = "python"
    overlapping_words = []

    # while count < 3:
    overlap_n = 2  # or more
    for word in word_list:
        # breakpoint()
        overlap = set(password) & set(word)
        if len(overlap) >= overlap_n and word != password:
            overlapping_words.append(word)
        # count += 1
    return random.choice(overlapping_words)


# def get_word_gen():
#     with open("sevenletterwords.txt", "r") as f:
#         w = (x.strip().upper() for x in f.readlines())
#     return w  # this is a generator


# word = "WIDGETS"
# test = []
# for w in get_word_gen():
#     x = set(word)
#     x.intersection_update(set(w))
#     test.append((w, x))

# points = filter(lambda x: len(x[1]) == 1, test)
# result = [w[0] for w in points if w[0].count(w[1].pop()) == 2]
# print(result)


def display_board():
    pass


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
