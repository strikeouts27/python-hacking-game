import sys
import random

# garbage characters system
garbage_chars = ["~!@#$%^&*()_+-={}[]|;:,.<>?/"]


def main():
    introduce()
    word_list = get_word_list()


# introduce game
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
def get_game_words(
    word_list,
    zero_letters=0,
    one_letters=1,
    two_letters=2,
    three_letters=3,
    four_letters=4,
    count=3,
):
    password = get_password(word_list)
    # print(f'password is {password}')
    overlapping_words = []
    # overlap_n is part of the filter variable that tells python to only grab game words with 2 matching letters to the password.
    overlap_n = zero_letters, one_letters, two_letters, three_letters, four_letters
    for word in word_list:
        if word in game_words:
            continue

        # this finds the matching characters
        overlap = set(password.upper()) & set(word.upper())
        print("This is the password: " + password)
        print("This is the word: " + word)
        print("this is overlap: " + str(overlap))
        if len(overlap) >= overlap_n and word.upper() != password.upper():
            print(f"Adding word to list {word}")
            overlapping_words.append(word)
            count += 1
            # print(f"This is before the count incremention: {count}")
        if count > 3 and len(overlapping_words) > 14:
            break
    print(f"count of overlapping words {len(overlapping_words)}")
    print("this is the " + str(count))

    # return random.choice(overlapping_words)


# function calls
word_list = get_word_list()
count = 3
game_words = get_game_words(word_list, count)
password = get_password(word_list)
get_game_words(word_list, 0, 1, 2, 3, 4)
    # return random.choice(overlapping_words)


def display_board():
    pass


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
