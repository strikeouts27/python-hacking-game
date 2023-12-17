import random

GARBAGE_CHARS = "~!@#$%^&*()_+-={}[]|;:,.<>?/"
word = "PYTHON"


def garbageify(word, width):
    # fill the row with garbage characters
    row = [random.choice(GARBAGE_CHARS) for _ in range(width)]
    # with 10 character spaces as the max we write scalable code to determine the word length.
    # width - len of the word
    width_max = width - len(word)
    insertion_index = random.randint(0, width_max)
    placement = insertion_index + len(word)
    game_string = row[insertion_index:placement]
    # slicing
    row[insertion_index:placement] = word
    print("This is row ", row)
    print("This is word", word)

    game_string = str(row).join(word)
    print(game_string)
    return game_string


x = garbageify("PYTHON", 10)
print(x)
