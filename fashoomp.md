strikeouts27
OP
 — Today at 8:31 PM
I have managed to fix the issue only to run into another issue.

I am trying to have python search the full game_word_list variable to find words that do not have any matching characters. 

I plan on having it search my word_list up to 500 times via random.choice. I think that would be a sufficent number of tries to find three words in the list. 

Once python has found three words which does not have any common letters I want to append those words to my game_word_list which is currently empty.

I was thinking a for loop could work as well, but I am not sure.

My question is this: 

I am trying to write a function that has python check the full game word list 500 times looking for a word with 0 matching characters to the password. 

so far I have written

def zero_matching_letters_words(password, full_game_word_list):
    zero_matching_letters_words = []
    while len(zero_matching_letters_words) < 3:
        for i in range(500):
            random_word = random.choice(full_game_word_list)
            if random_word 


do I need to create other small functions and break this down?

my code as it is: https://paste.pythondiscord.com/H2KA

automate the boring stuff with python solution code: https://inventwithpython.com/bigbookpython/project33.html
Python
 pinned 
a message
 to this channel. See all 
pinned messages
.
 — Today at 8:31 PM
Python
BOT
 — Today at 8:31 PM
@strikeouts27

Python help channel opened
Remember to:
• Ask your Python question, not if you can ask or if there's an expert who can help.
• Show a code sample as text (rather than a screenshot) and the error message, if you've got one.
• Explain what you expect to happen and what actually happens.

:warning: Do not pip install anything that isn't related to your question, especially if asked to over DMs.
Closes after a period of inactivity, or when you send !close.
Fashoomp — Today at 8:40 PM
What do you expect to happen if it runs 500 times and doesn't find a match?
Why not just iterate through the words instead of randomly selecting one over and over?
@strikeouts27
Also just looking at the structure of your code...you should be defining ALL your functions before calling and assigning from them
def get_full_game_word_list():
    with open('sevenletterwords.txt', 'r') as file:
        full_list_of_words = [line.strip().upper() for line in file]
        return full_list_of_words

full_game_word_list = get_full_game_word_list()


def get_password(full_game_words_list):
    password = random.choice(full_game_words_list)
    return password


password = get_password(full_game_word_list)
instead of this
def get_full_game_word_list():
    with open('sevenletterwords.txt', 'r') as file:
        full_list_of_words = [line.strip().upper() for line in file]
        return full_list_of_words


def get_password(full_game_words_list):
    password = random.choice(full_game_words_list)
    return password


full_game_word_list = get_full_game_word_list()
password = get_password(full_game_word_list)
Do this
strikeouts27
OP
 — Today at 8:45 PM
so have all of my function definitions togather, and than call and assign things
If I remember your past advice, you suggested that I write many small functions that do one thing and test along the way.
Fashoomp — Today at 8:45 PM
yes, exactly
strikeouts27
OP
 — Today at 8:46 PM
I will make some edits. be back in 5 minutes
Fashoomp — Today at 8:47 PM
Yes, this is good
strikeouts27
OP
 — Today at 8:57 PM
Updated code: https://paste.pythondiscord.com/54NQ
Fashoomp — Today at 8:59 PM
So what exactly is the point of the zero matching letters?
strikeouts27
OP
 — Today at 9:00 PM
In this game, 15 words are generated. one of them is the password. the other 14 are incorrect answers. when you select a word, if your answer is incorrect, a hint system is triggered. it will say 0 of 7 letters matching. or 3 of 7 letters matching. and so on.
I need a certain number of 0 letter matching character words, 1,2, and 3 letter matching words,
I would probably want it scalable
My problem is in the get_zero_matching_letters_words function. I am comparing the whole word instead of the individual letter
I think I need a more precise if statement that iterates over each letter in the random word
thinking....
def 
get_zero_matching_letters_words(password, full_game_word_list):
    zero_matching_letters_words = []
    while len(zero_matching_letters_words) < 3:
        for word in full_game_word_list:
            random_word = random.choice(full_game_word_list)
            for letter in random_word:
                if letter not in password:
                    zero_matching_letters_words.append(random_word)
            else:
                print("Error! Loop failed!")
    return zero_matching_letters_words
 
I have refined it a little so that it is checking the letters but now I need to refine it further to say 0 matching letters
I am thinking == 0 attempting
strikeouts27
OP
 — Today at 9:08 PM
perhaps something like this?

def get_zero_matching_letters_words(password, full_game_word_list):
    zero_matching_letters_words = []
    while len(zero_matching_letters_words) < 3:
        for word in full_game_word_list:
            random_word = random.choice(full_game_word_list)
            for letter in random_word:
                if letter in password:
                    matches += 1
                    if matches == 0:
                        zero_matching_letters_words.append(random_word)
            else:
                print("Error! Loop failed!")
    return zero_matching_letters_words
Fashoomp — Today at 9:13 PM
it doesn't quite make sense then to have a separate function for zero matching letters, one matching letters, two matching letters, etc
you can create one get_n_matching_letters and use that for all of them
just provide how many matches you need
if you want to see how many letters each word has in common, you can use a set
Image
in this example, my password is "python"
this shows each word, how many letters overlap, and which letters overlap
this is just a few lines of code...
you can store the results that match what you're looking for and then randomly return one
password = 'python'
overlapping_words = []
overlap_n = 2 # or more
for word in word_list:
    overlap = set(password) & set(word)
    if len(overlap) >= overlap_n and word != password:
        overlapping_words.append(word)

print(random.choice(overlapping_words))
 
it's not a function, but here's the logic
this randomly selects a word with 2 or more shared letters with the password
also sorry but I gtg!
Good luck, hopefully this makes sense
@strikeouts27
strikeouts27
OP
 — Today at 9:19 PM
thank you for your help as always Fashoomp