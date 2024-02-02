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
    name = input("\nTo start the game please type in your player name: ")
    print(
        f"\n Agent {name}! The evil dictator Kim Jong Un has decided to launch the nukes. All of humanity's hopes rest on your shoulders to hack into the system and stop the launch. You will see a series of possible words that are the password. Use our hint system software to determine if you are close to guessing the password. The hint system will tell you the letters that the word choice and the password have in common as well as positioning. You are our last hope.... \n Okay agent {name}, here are list of the possible passwords. \n Type in the word from the available list of words that you believe is the password."
    )

    return name


# this function will gather in the game words from the sevenletterwords.txt file and be returned in this function.
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


# From the word list we need game words that have a certain number of letters in common with the password.
# in this case we sum up the dictionaries values and put them into a list.
# after that the password is appended to the list.


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
    # Test: print("This is the game words dictionary. \n" + str(game_word_set))
    # Test: print("This is the password for the game. \n" + str(password))
    return game_word_set


# the game words need to have a certain amount of characters in common with the password.
# in this function x will hold the number of words that will be generated with each functionc call.
# so if this funciton is called once than three words will generate.
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


# in each game row we need a memory address that starts with a hex number.
# this function will generate the hex number. an example is shown below.
# Ox217_ _ _ _ _ _ _ _ _ _ _
def hex_number():
    number = random.randint(1000, 1500)
    hex_number = hex(number)
    return hex_number


# this function will insert the game word at a random place and always after the hex memory number is made first.
# the garbage characters will fill in the rest of the empty spaces.


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


# python gotchas with mutable data types workaround
# python needs to be told to iterate past the first game word and to include the other 15 words.
# this function generates a list of the game words in strings with the memory address and hex address and garbage characters.
# an issue I ran into was that using pop modifies the list and results in items being skipped over
# so the keyword and is utilized and word is placed as the variable.


def game_word_selection(game_word_set):
    gamewords = []
    while len(gamewords) < 16 and game_word_set:
        word = game_word_set.pop()
        garbageword = garbage_character_filler(word)
        gamewords.append(garbageword)
    return gamewords


# def game_word_selection(game_word_set):
#     gamewords = []
#     while len(gamewords) < 16:
#         for word in game_word_set:
#             game_word_set.pop()
#             garbageword = garbage_character_filler(word)
#             gamewords.append(garbageword)
#         return gamewords

# format gamewords functions job is to create two columns for the gamewords and
# rows with two game words and there string designs.


def format_gamewords(game_rows):
    game_string = "".join(game_rows)
    formatted_rows = []

    for i, row in enumerate(game_rows, start=1):
        formatted_rows.append(row.lstrip())
        if i % 2 == 0 and i != len(game_rows):
            formatted_rows.append("\n")  # Add a new line after every two iterations
        else:
            formatted_rows.append("     ")  # Add 5 spaces in between each iteration
    game_string = "".join(formatted_rows)

    return game_string


def make_guess():
    guess = input("WELCOME SUPREME LEADER PLEASE TYPE THE PASSWORD: ").upper()
    return guess


def evaluate_guess(password, name, word_list):
    attempts_left = 3
    states_lost = []
    game_word_set = get_game_word_set(word_list, password)
    guess = make_guess()

    while attempts_left != 0:
        if guess == password:
            print("\n ACCESS GRANTED! YOU DID IT! YOU SAVED THE WORLD!")
            print(
                "\n YOU WIN! GREAT JOB AGENT {name} I WILL SPEAK TO THE POTUS ABOUT YOUR MEDAL OF HONOR AND PROMOTION!"
            )
            break
            # game_word_set has the symbols which means guessing this is impossible. unless i tell them to input the symbols.
        elif guess in game_word_set and guess != password:
            print("\n Oh no! We got it wrong!")
            state_lost = get_states_lost()
            print(f"\n We lost the state of {state_lost} in a nuclear explosion!")
            states_lost.append(state_lost)
            print(f"\n So far we have lost the following territories: {states_lost}")
            attempts_left -= 1

            if attempts_left > 0:
                print(f"\n We have {attempts_left} attempts left!")
                make_guess()

            elif attempts_left == 0:
                print(
                    "\n WE ARE OUT OF TIME! MISSION FAILED! CALL IN OUR AIRSTRIKE UNITS AND ATTACK! LETS REGROUP AT THE BUNKER!"
                )
                print(
                    "GAME OVER! Better luck next time! At least we can play Fallout3 while things calm down!"
                )

        else:
            print(
                f"\n Agent {name}, what are you doing! Thats not one of the words listed! Pick one of the game words listed on screen!"
            )
        # print("Test:This is the current guess", guess)
        # print("Test: for game_word_set", game_word_set)
        # print("Test: This is the password", password)


# determine a state, determine a point value, add the states to a dictionary and sum up the totals at the end of the game.


# have all of the states in one dictionary and have each state have a point value.
# have small states be worth 50, intermediate 100, and large states 500 points.
# or just have states lost and no point values.
# random.choice
def get_states_lost():
    usa_states = [
        "Alaska",
        "Alabama",
        "Arkansas",
        "American Samoa",
        "Arizona",
        "California",
        "Colorado",
        "Connecticut",
        "District ",
        "of Columbia",
        "Delaware",
        "Florida",
        "Georgia",
        "Guam",
        "Hawaii",
        "Iowa",
        "Idaho",
        "Illinois",
        "Indiana",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Massachusetts",
        "Maryland",
        "Maine",
        "Michigan",
        "Minnesota",
        "Missouri",
        "Mississippi",
        "Montana",
        "North Carolina",
        "North Dakota",
        "Nebraska",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "Nevada",
        "New York",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Puerto Rico",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Virginia",
        "Virgin Islands",
        "Vermont",
        "Washington",
        "Wisconsin",
        "West Virginia",
        "Wyoming",
    ]
    lost_state = random.choice(usa_states)
    return lost_state


def hint_system():
    print(
        "\nLets utilize our software to determine what letters and spacing your guess has in common with the password!"
    )
    # need a pausing mechanism

    # DRIVER CODE ---------------------
    # these lines of code are here to prevent not defined issues.


def main():
    name = introduce()
    word_list = get_word_list()
    password = get_password(word_list)
    game_word_set = get_game_word_set(word_list, password)
    # we need to determine which game word python will use one at a time without duplicates.
    game_rows = game_word_selection(game_word_set)
    print("\n")
    game_rows = format_gamewords(game_rows)
    print("Okay we managed to get into his system! \n")
    print(game_rows)
    print("\n")

    evaluate_guess(password, name, word_list)


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
# random will change things in place. there is no need for variables.
