import random
from words import wordss
import string


def get_valid_word(words):
    word = random.choice(words) # randomly choose from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()



def hangman():
    word = get_valid_word(wordss)
    word_letters = set(word)  # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        #letter used
        # ' '.join(['a','b','cd'])--> 'a b cd'
        print("you have used these letters: ", ' '.join(used_letters))
        
        # what current word is (ie W - R D)
        word_list= [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))



        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

        elif user_letter in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. please try again")

if __name__=='__main__':
    hangman()
