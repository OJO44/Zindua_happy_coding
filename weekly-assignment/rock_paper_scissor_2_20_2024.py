import random

# Function to get the winner
def get_the_winner(joseph, computer):
    if joseph == 'Paper' and computer == 'Rock':
        print("Joseph wins!")
        return 'Joseph'
    elif joseph == "Rock" and computer == "Paper":
        print("Computer wins!")
        return "Computer"
    elif joseph == "Rock" and computer == "Scissors":
        print("Joseph wins!")
        return "Joseph"
    elif joseph == "Scissors" and computer == "Paper":
        print("Computer wins!")
        return "Computer"
    else:
        print("It's a tie! Try again.")

# Main program
choices = ["Rock", "Paper", "Scissors"]
while True:
    joseph = input("\nChoose Rock, Paper, or Scissors: ")
    computer = random.choice(choices)
    
    result = get_the_winner(joseph, computer)
    print("Winner: ", result)
