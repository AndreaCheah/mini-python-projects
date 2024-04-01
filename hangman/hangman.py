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
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)  # letters in the English alphabet
    used_letters = set()    # what the user has guessed
    lives = 6
    print("answer is", word)

    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input('Guess a letter: ').upper()
        if user_input in (alphabet - used_letters):
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print("Wrong guess. Try again! :)")

        elif user_input in used_letters:
            lives -= 1
            print('No man, you already guessed that letter. xD')

        else:
            print('Invalid character. Try again! :)')
    if lives == 0:
        print("You died, sorry. The word was", word, ". :(")
    else:
        print("You survived! The word was", word, "! :D")

hangman()