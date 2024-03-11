import random
from random import randint

class SnakesAndLadders:
    def __init__(self): #constructor method to initialize the class attributes.
        self.board_size = 10 #sets the size of the game board.

#create a library thatrepresents the mapping of ladder positions in a Snakes and Ladders game.
#The keys represent the positions on the game board where the bottom of a ladder is located.
# The values represent the positions where the top of the ladder leads to when a player lands on the bottom of that ladder.
# The numbers before the colon are keys while the numbers after the colon represents values e.g., 1 is key, 38 is value.
        self.ladders = {2: 15, 7: 29, 12: 42, 17: 33, 22: 48, 35: 50, 44: 67, 60: 80}

#create a library that represents the mapping of snake positions in a Snakes and Ladders game.
#The key corresponds to the position on the game board where the head of the snake is located.
# The value corresponds to the position where the tail of the snake leads to when a player lands on the head of that snake.
# The numbers before the colon are keys while the numbers after the colon represents values e.g., 32 is key and 10 is value. 
        self.snakes = {14: 5, 28: 10, 38: 20, 45: 22, 55: 17, 72: 35, 81: 45, 92: 70}

    def roll_dice(self): #this is a contructor method that simulates the rolling of a dice
        return random.randint(1, 6) #returns a random number between 1 and 6.

    def get_position(self, current_position, dice_roll): #this is a constructor method that calculates the position after the roll dice.
        new_position = current_position + dice_roll #calculates new position based on current position and dice roll.

        if new_position in self.ladders: #checks if the new position is on a ladder
            print("You climbed a ladder!")
            new_position = self.ladders[new_position] #updates the new  position to the top of the ladder

        elif new_position in self.snakes: # checks if new position is on a snake.
            print("You landed on a snake!")
            new_position = self.snakes[new_position] #updates the new  position to the tail of the snake

        return new_position #return final position
    
    def play_game(self): #  constructor method to start and play game.
        player_positions = [0, 0] #show the initial players' position
        players = ['Player 1', 'Player 2'] # define player names.

#use a while loop that will be used to control the game
        while max(player_positions) < self.board_size * self.board_size: #checks whether the maximum player position is less than the final position on the board.
            for i in range(2):  #iterate over the two players
                input(f"{players[i]}, press Enter to roll the dice.") #prompt player to roll the dice
                dice_roll = self.roll_dice() # roll dice
                player_positions[i] = self.get_position(player_positions[i], dice_roll) #update the position of the current player.
                print(f"{players[i]} moved to position {player_positions[i]} after rolling a {dice_roll}.") #print player movement

                if player_positions[i] >= self.board_size * self.board_size: #check if a player has won
                    print(f"{players[i]} wins!") # prints the winning player
                    break

# Create an instance of the SnakesAndLadders class and start the game
game = SnakesAndLadders()
game.play_game()
