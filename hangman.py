import random
import string
from words import words

def get_valid_word():
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word()
    # print(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
    # used letters:
        print("you have guessed these letters: " , " ".join(used_letters))
    # guessed letters:
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("you have", lives , " lives left and the Current word is: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("you already have guessed this letter, try again!")
        else: 
            print("Invalid character, try again")

    if lives == 0:
        print("Sorry you died, the word was:", word)
    else:
        print("You guesed the words", word, "!!")
hangman()