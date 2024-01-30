import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    # saves letters in word as a set/ to keep track what letters have been used for that word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # to track what letters the user has guessed

    lives = 7

    # getting user input
    # guess until all letters are used up/ guess word correctly
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f'You have {lives} lives left, You have used these letters: ', ' '.join(
            used_letters))

        # what current word is (ie. W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # User input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1  # takes a life if worng
                print(f'Letter {user_letter} not in word.')

        elif user_letter in used_letters:
            print('You have already used that character, try again')

        else:
            print('invalid character, try again')

    # get here when len(word_letters) == 0 Or lives == 0
    if lives == 0:
        print('Game Over, you died. The word was:', word)
    else:
        print('Congrats, You have guessed the word:', word)


if __name__ == '__main__':
    hangman()
