#The hangman game
#Choose some good hangman words for your program and create a list of words for your game.
import random
words = ["abruptly", "absurd", "abyss", "askew",
         "avenue", "awkward", "axiom", "azure",
         "luxury", "lymph", "marquis", "matrix",
         "transcript", "transgress", "transplant", "triphthong"]

#At the start of the game, use the random library to choose a random word from your hangman words and display the word's letters as dashes rather than letters.

# Choose a random word from the list
chosen_word = random.choice(words)
display_word = "_" * len(chosen_word)
#
print("Welcome to Hangman!")
print(display_word)

# You can continue with the game logic from here, such as getting user input, checking if the guessed letter is in the word, updating the display, and keeping track of the number of guesses.

guessed= False
guessed_letters = [] #hold letters the user guessed.
guessed_words = [] #hold words the user guesses
trials = 6     #available number of trials

while not guessed and trials > 0:
    guess = input("please guess a letter or word: ")

    if len(guess) ==1 and guess.isalpha(): #means guess is greater than 1 and is a character of the alphabet.
        print()
        if guess in guessed_letters:
            print("you already guessed", guess)
        elif guess not in words:
            print(guess, "not guessed")
            trials -=1
            guessed_letters.append(guess)
        
        else:
            print("good job", guess, "is the word.")
            guessed_letters.append(guess)
            words_as_lists = list(display_word) #this will assist to reveal all occurences of a guess by first converting the string to a guess.
            indices = [i for i, letter in enumerate(words) if letter== guess]# finding indices where guesses occured in a word.
            
            for index in indices:
                words_as_lists(index) =guess  #replaces each underscore at index with guess.

            display_word = "".join(words_as_lists)
            if"_" not in display_word:
            guessed = True


            
    elif len(guess) == len(words) and guess.isalpha(): # guesing a word would mean the length of the guess is equal to the length of the word and that the guess is an alphabet.
        if guess in guessed_words:
            print("you already guessed word", guess)
        elif guess != words:
            print(guess, "not guessed word")
            trials -=1  #documents the number of tries to 1.
            guessed_words.append(guess)
        
        else:
          guessed = True
          display_word = words
    else:
        print("not a valid guess")
        print(display_word)
        print("\n")
if guessed:
    print("Good guess, you in!")   
else :
    print("not a valid guess, nice try ")



