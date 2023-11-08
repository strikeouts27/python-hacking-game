import random

rows = 8
columns = 3
tries = random.randint(3, 5)

words = ["TESTS", "THREE", "TWO", "LENGTH", "ONE", "GODEL", "TURING", "LOVELACE", "BACH", "KASTRUP", "LEVIN", "FALLOUT"]
word_set = set()
password_set = set()
junk = "!@#$%[^&*)_+<>~:;~|}?v"

#lambda = x: 

def render_words(): # Defines the rows & column structure and memory
    for loop in range(rows):
        mem = random.randint(1000, 9999)
        
        for column in range(columns):
            print(f"   |0x{mem}  ", end="") # Prints fake memory address.
            junk_string()
        print() # Ends row.
    return random.choice(list(word_set))

    
def junk_string():
    for n in range(16):
        char = random.randint(0, 21)
        word_chance = random.randint(0, 21)
        word_choice = random.choice(words)
        
        if word_chance == char and len(word_choice) + n < 16:
            print(f"\033[1;37m{word_choice}\033[0m", end="")
            word_set.add(word_choice)

            for u in range(16 - (len(word_choice) + n)):
                #print(len(junk) - len(word_choice) + char)
                char_end = random.randint(0, 21)
                print(f"\033[1;37m{junk[char_end]}\033[0m", end = "")
            return
        print(f"\033[1;37m{junk[char]}\033[0m", end = "")


def hacking(password):
    #print("PASSWORD: ", password)
    for lives in range(tries, 0, -1):
        guess = input(f"\nEnter Password ({lives} tries remaining):").upper()
        if guess == password: return print("[Access Granted]")

        for letter in range(len(guess)):
            for character in range(len(password)):
                if guess[letter] == password[character]: 
                    password_set.add(guess[letter])
                    #print(password_set)
        print("Hint: ", len(password_set))


if __name__ == "__main__":
    password = render_words()
    #print(word_set)
    hacking(password)
