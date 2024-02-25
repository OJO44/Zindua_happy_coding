import random

# Define a list of words for the game
words = ["green", "python", "hangman", "program", "computer"]

# Select a random word from the list.
secret_word = random.choice(words).lower()

# Initialize variables for tracking game progress and guesses
display_word = "_" * len(secret_word)    #This line initializes the `display_word` variable, which represents the current state of the word being guessed by the player.
failure_counts = 6
guessed_letters = []

# Introduce a Loop
while failure_counts > 0:
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters: #Checks if the letter has already been guessed
        print("You've already guessed that letter. Try again.")
        continue #skips the current iteration and moves to the next.

    guessed_letters.append(guess)   #Add the guessed letter to the list of guessed letters

    if guess in secret_word: #Checks if the guessed letter is in the secret word
        print(f"Correct! '{guess}' is in the word.")
        new_display_word = ""
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                new_display_word += guess
            else:
                new_display_word += display_word[i]
        display_word = new_display_word
    else:
        failure_counts -= 1
        print(f"Incorrect! '{guess}' is not in the word. {failure_counts} trials remaining.")

    # Displays the current progress of the word
    print(display_word)

    # check the winning status
    if "_" not in display_word:
        print(f"Congratulations, you won! The secret word was '{secret_word}'.")
        break

# loss
if failure_counts == 0:
    print(f"Sorry, you lost. The secret word was '{secret_word}'.")



    
