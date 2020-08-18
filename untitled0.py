# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:11:21 2020

@author: Varun
"""

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    iswordguessed = True
    for i in secret_word:
        if i not in letters_guessed:
            iswordguessed = False
            break
    return iswordguessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    blanks = []
    for i in range(len(secret_word)):
        blanks.append('_ ')
    j = 0
    while j < len(secret_word):
        if secret_word[j] in letters_guessed:
            blanks[j] = secret_word[j] 
        j += 1
    
    return ''.join(blanks)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    allletters = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in allletters:
            del(allletters[allletters.index(i)]) 
            #we used this long format because python gets confused whether i belongs to 
            #letters_guessed or i belongs to allletters
    
    return ''.join(allletters)

def islettercorrect(letter, numguess, strike, letters_guessed):
   
    while True:
        if letter.isalpha() and letter.lower() in get_available_letters(letters_guessed):
            break
        # elif letter == "*" :
        #     break
        else:
            if strike != 0:
                print("Three Strikes and you loose a guess")
                print("Strike ", strike)
            if  strike == 3:
                numguess -= 1
                strike = 0
            print("Guesses Remaining: ", numguess)
            if numguess == 0:
                break
            if not letter.isalpha():
                
                letter = input("Please enter an aplhabet:")
                if letter == "*":
                    strike -= 1
                    print(show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed))
                    print("letters guessed", letters_guessed)
            strike +=1
                
           
                
            print("\n--------------------------")
            
    return (letter, numguess, strike)


def getuniquewords(secret_word):
    count = 0
    listofletters = string.ascii_lowercase
    for i in listofletters:
        if i in secret_word:
            count += 1
  
    return count
        
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    uniquewords = getuniquewords(secret_word)
    numguess = 6
    letters_guessed = []
    strike = 1
    print("Welcome to the game Hangman")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("----------------------------------")
    
    print("Available guesses: ", numguess)
    print("Available letters: ", get_available_letters(letters_guessed))
    print("If you wrongly guess a consonant you get penalty of 1 guess")
    print("If you wrongly guess a vowel you get a penalty of 2 guess")
    
    
    while not(is_word_guessed(secret_word, letters_guessed)) and numguess > 0: 
        
        letter = input("Please input your guessed letter: ")
       
        (letter, numguess, strike) = islettercorrect(letter, numguess, strike, letters_guessed)
        if letter.lower() in secret_word:
           numguess +=1
        elif letter.lower() in 'aeiou' :
            numguess -=1
                
        letters_guessed.append(letter.lower())
        print(get_guessed_word(secret_word, letters_guessed))
       
        
        numguess -=1
        if numguess == -1:
            numguess = 0
        print("\nGuesses Remaining: ", numguess)
        print("Available Letters: ", get_available_letters(letters_guessed))
        print("----------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("You won with a score of ",numguess*uniquewords)
    else:
        print("Game Over! you loose")
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    iword = my_word.replace(" ", "")
    what_to_return = True
    for n in range(len(other_word)):
        if iword[n] != "_" and iword[n] != other_word[n]:
            what_to_return = False
            break
    for a in range(len(other_word)):
        if other_word[a] in letters_guessed and other_word[a] != iword[a]:
            what_to_return = False
    
      
    return what_to_return



def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    possible = []
    new_word = my_word.replace(" ","")
    
    newlist = []
    for i in wordlist:
        if len(i) == len(new_word):
            newlist.append(i)
   
  
    for o in newlist: 
        if match_with_gaps(new_word, o, letters_guessed):
            possible.append(o)
    o = 0
    return possible
        


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    uniquewords = getuniquewords(secret_word)
    numguess = 6
    letters_guessed = []
    strike = 1
    print("Welcome to the game Hangman")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("----------------------------------")
    
    print("Available guesses: ", numguess)
    print("Available letters: ", get_available_letters(letters_guessed))
    print("If you wrongly guess a consonant you get penalty of 1 guess")
    print("If you wrongly guess a vowel you get a penalty of 2 guess")
    print("To get a hint at anytime in game enter an asterik * ")
    
    
    while not(is_word_guessed(secret_word, letters_guessed)) and numguess > 0: 
        
        letter = input("Please input your guessed letter: ")
        if letter == "*":
            numguess +=1
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed))
       
        (letter, numguess, strike) = islettercorrect(letter, numguess, strike, letters_guessed)
        if letter.lower() in secret_word:
           numguess +=1
        elif letter.lower() in 'aeiou' :
            numguess -=1
                
        letters_guessed.append(letter.lower())
        print(get_guessed_word(secret_word, letters_guessed))
       
        
        numguess -=1
        if numguess == -1:
            numguess = 0
        print("\nGuesses Remaining: ", numguess)
        print("Available Letters: ", get_available_letters(letters_guessed))
        print("----------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("You won with a score of ",numguess*uniquewords)
    else:
        print("Game Over! you loose")
        print(secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
