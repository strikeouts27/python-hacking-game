import sys
import random

name = "Python"

# garbage characters system
garbage_chars = ["~!@#$%^&*()_+-={}[]|;:,.<>?/"]


def main():
    introduce()
    word_list = get_word_list()
    password = get_password(word_list)
    get_matching_letter_words(password, word_list, num_matches, count)
    game_word_list = combine_word_lists()


# introduce game
def introduce():
    print(
        f"Agent {name}! The evil dictator Kim Jong Un has decided to launch the nukes. All of humanites hopes rest on your shoulders to hack into the system and stop the launch. You will see a series of possible words that are the password. Use our hint system software to determine if you are closs to guessing the password. You are our last hope.... \n Okay agent {name}, here are list of the possible passwords. \n Type in the word from the available list of words that you believe is the password."
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


# num_matches is the number of matching letters.
def get_matching_letter_words(password, word_list, num_matches, count):
    matching_words = []
    while len(matching_words) < count:
        word = random.choice(word_list)
        if sum(l1 == l2 for l1, l2 in zip(password, word)) == num_matches:
            matching_words.append(word)
    return matching_words


def combine_word_lists(password, word_list):
    zero_word_list = get_matching_letter_words(password, word_list, 0, 3)
    one_word_list = get_matching_letter_words(password, word_list, 1, 3)
    three_word_list = get_matching_letter_words(password, word_list, 3, 3)
    five_word_list = get_matching_letter_words(password, word_list, 3, 5)
    game_list = merge(zero_word_list, one_word_list, three_word_list, five_word_list)
    return game_list


def merge(*lists: [list]) -> list:
    return [item for sublist in lists for item in sublist]


def randomWords(full_game_words_list):
    random_word_list = []
    if random_word_list < 2:
        randomWord = random.choice(full_game_words_list)
        random_word_list.append(randomWord)
        return randomWord

    else:
        print("Error!")
        return


def generate_memory_address():
    memory_address = f"x0" + str(random.randint(1000, 9999))
    return memory_address


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
