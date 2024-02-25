import random

# Step 1: Define a list of words for the game
words = ["greenback", "python", "hangman", "programming", "computer"]

# Step 2: Select a random word from the list and convert it to lowercase
secret_word = random.choice(words).lower()

# Step 3: Initialize variables for tracking game progress and guesses
display_word = "_" * len(secret_word)    #
failure_counts = 6
guessed_letters = []


#display_word = "_" * len(secret_word) 
#Purpose: This line initializes the `display_word` variable, which represents the current state of the word being guessed by the player.

#len(secret_word)` calculates the length of the `secret_word` string.
#len(secret_word)` creates a string consisting of underscores (`_`) that is the same length as the `secret_word`.
#This line sets up the initial display of the word as underscores, where each underscore represents a letter that needs to be guessed.

#failure_counts = 6`:
#Purpose: This variable is used to track the number of incorrect guesses the player can make before losing the game. 
#failure_counts` is initialized to `6`, indicating that the player has 6 chances (incorrect guesses) before losing the game.
#Each time the player makes an incorrect guess, this count will be decremented until it reaches 0.

#guessed_letters = []:
#Purpose: This list is used to keep track of the letters that the player has already guessed.
#guessed_letters` is initialized as an empty list.
#As the player makes guesses, the guessed letters will be added to this list to prevent duplicate guesses and allow the player to track their previous guesses.



# Step 4: Start the main game loop
while failure_counts > 0:
    guess = input("Enter a letter: ").lower()
    # Step 6: Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue #skips the current iteration and moves to the next.

    # Step 7: Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Step 8: Check if the guessed letter is in the secret word
    if guess in secret_word:
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
#he loop uses for i in range(len(secret_word)) to iterate through each index of the secret_word.
#The variable i represents the index of each character in the secret_word
#In the provided for loop within the Hangman game program, the `[i]` is used as an index to access individual characters in strings. Let's break down the relevant part of the code and explain the purpose of `[i]`:
#for i in range(len(secret_word)):`: This loop iterates through each index `i` in the range of indices from 0 to the length of the `secret_word` string.
#secret_word[i]`: This expression accesses the character at index `i` in the `secret_word` string. By using `secret_word[i]`, we can examine each character of the secret word one by one during each iteration of the loop.
#display_word[i]`: Similarly, this expression accesses the character at index `i` in the `display_word` string. It allows us to update the `display_word` based on correct guesses made by the player.

#In summary, `[i]` is used to access individual characters at specific positions within strings (`secret_word` and `display_word`) during each iteration of the loop. This allows the program to compare guessed letters with the characters in the secret word and update the display accordingly based on correct guesses.

    # Step 9: Display the current progress of the word
    print(display_word)

    # Step 10: Check if the player has won
    if "_" not in display_word:
        print(f"Congratulations, you won! The secret word was '{secret_word}'.")
        break

# Step 11: Handle the end of the game - player wins or loses
if failure_counts == 0:
    print(f"Sorry, you lost. The secret word was '{secret_word}'.")



    
