'''
Name : Pranay Kumar Y
Date : 09-08-2018
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters. 
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = loadWords()

def get_available_letters(letters_guessed):
    ''' letters that are not present are '''
    temp_stng = "abcdefghijklmnopqrstuvwxyz"
    for each_char in letters_guessed:
        temp_stng = temp_stng.replace(each_char, "")
    return temp_stng

def is_word_guessed(secret_word, letters_guessed):
    ''' Checking the characterws if present or not '''
    for each_char in letters_guessed:
        secret_word = secret_word.replace(each_char, "")
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    temp_stng = secret_word
    for each_char in letters_guessed:
        temp_stng = temp_stng.replace(each_char, "")

    for each_char in temp_stng:
        if each_char != "_":
            secret_word = secret_word.replace(each_char, "_")
    return secret_word

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!!")
    lettersguessed = ''
    guessLeft = 8
    print("---------------------------------------------------------------")
    while guessLeft>0:
        print("you have" + str(guessLeft) + "guesses left")
        print("available letters: " + get_available_letters(lettersguessed))
        guess = input("Please guess a letter:")
        if guess in secretWord and guess not in lettersguessed:
            lettersguessed += guess
            print("Good Guess: " + get_guessed_word(secretWord, lettersguessed))

        elif guess in lettersguessed:
            print("Opps! The letter is selected before" + get_guessed_word(secretWord, lettersguessed))

        else:
            lettersguessed += guess 
            print("Opps! The wrong letter is selected" + get_guessed_word(secretWord, lettersguessed))
            guessLeft -= 1

        print("---------------------------------------------------------------")

        if secretWord == get_guessed_word(secretWord, lettersguessed):
            return ("-----Congratulations! You Won-----")
            
        if guessLeft <= 0:
            print("-----Sorry! You Lose the game-----")
            break
        




def main():
    '''
    Main function for the given program
    '''
    secretWord = chooseWord(wordlist).lower()
    print(hangman(secretWord))

    

if __name__ == "__main__":
    main()
