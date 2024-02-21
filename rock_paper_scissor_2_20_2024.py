#f is a way of formating strings

import random

# Function to get the winner and assign points
def get_the_winner(joseph, computer, joseph_points, computer_points):
    if joseph == 'Paper' and computer == 'Rock':
        print("Joseph wins this round!")
        joseph_points += 1
    elif joseph == "Rock" and computer == "Paper":
        print("Computer wins this round!")
        computer_points += 1
    elif joseph == "Rock" and computer == "Scissors":
        print("Joseph wins this round!")
        joseph_points += 1
    elif joseph == "Scissors" and computer == "Paper":
        print("Computer wins this round!")
        computer_points += 1
    else:
        print("It's a tie! Try again.")

    return joseph_points, computer_points

# Main program
choices = ["Rock", "Paper", "Scissors"]
joseph_points = 0
computer_points = 0
rounds_to_win = 3

while joseph_points < rounds_to_win and computer_points < rounds_to_win:
    joseph = input("\nChoose Rock, Paper, or Scissors: ")
    computer = random.choice(choices)
    
    joseph_points, computer_points = get_the_winner(joseph, computer, joseph_points, computer_points)
    
    print("Joseph Points: ", joseph_points)
    print("Computer Points: ", computer_points)

    if joseph_points >= 2 or computer_points >= 2:
        break

if joseph_points > computer_points:
    print("\nJoseph wins the game!")
elif computer_points > joseph_points:
    print("\nComputer wins the game!")
else:
    print("\nIt's a tie! No clear winner.")
