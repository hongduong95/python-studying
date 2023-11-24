import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() 
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You have", lives, " lives and used: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current: ", ' '.join(word_list))
        user_letters = input("Guess: ").upper()
        if used_letters in alphabet - used_letters:
            used_letters.add()
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives = lives - 1
                print("not in it")

        elif user_letters in used_letters:
            print("same, again")
        else:
            print("invalid")
        
    if lives == 0:
        print("u dead: ", word)
    else:
        print(" nice guess: ", word )

hangman()