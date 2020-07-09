# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letters in secretWord: # will run through all letters in the secret word
        if letters not in lettersGuessed: #wil compare all letters in the secret word w/ the guessed letters
            return False #if even 1 letter in the secret word is not in the guessed letters will return false
    return True #if it doesn't return False, it means that all letters are present and will return True.



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretLetters = '' #string of letters guessed right and underscores.
    
    for letter in secretWord:
        if letter in lettersGuessed: #take all letters from secretWord in order and check if it was guessed alredy
            secretLetters += letter # if the letter was guessed, the position where it should be will be filled with the letter
        else:
            secretLetters += '_ ' #if the letter in the position was not guessed right, the position will be filed with a underscore
    print(secretLetters)
            
    
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letterList = 'abcdefghjklmnopqrstuvwxyz' #list of letters
    notGuessed = '' #string of not guessed letters
    for letter in letterList:
        if letter not in lettersGuessed: #will compare all letters to the guessed letters and include the not guessed in the notGuessed string
            notGuessed += letter
    return notGuessed



def lenWord(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Print the length of the secret word.
    '''
    print('The secret word has {} letters'.format(len(secretWord))) #print the length of the word


    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secretWord))) #print the length of the word
    
    guesses = 0
    lettersGuessed = []
    
    while guesses < 8:
        print('-------------')
        print('You have {} guesses left'.format(8 - guesses))
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        letter = input('Please guess a letter: ').lower()

        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: ", end = '')
            getGuessedWord(secretWord, lettersGuessed)
            
        else:
            lettersGuessed.append(letter) # add the guessed letter to the list of guessed letters
        
            if isWordGuessed(secretWord, lettersGuessed): #check if the user got the word right,
                print('-------------')
                print('Congratulations, you won!')
                break #if the word was guesses the game is over
                
            elif letter in secretWord:
                lettersGuessed.append(letter)
                print('Good guess: ', end = '')
                getGuessedWord(secretWord, lettersGuessed)
      
            else: #if the letter is no the secret word the user loses a guess
                guesses+=1
                print('Oops! That letter is not in my word: ', end = '')
                getGuessedWord(secretWord, lettersGuessed)

             


    if guesses >7:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord)) #if the user did not manage to get theright word in 8 guesses he loses.

secretWord = 'horse'
wordlist = loadWords()
#secretWord = chooseWord(wordlist).lower() # picking a random word from the wordlist given.
hangman(secretWord) # starting the game.




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
