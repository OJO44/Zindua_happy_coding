import random
from random import randint

class SnakeAndLadder:
#represents the mapping of snake positions in a Snakes and Ladders game.
#The key corresponds to the position on the game board where the head of the snake is located.
# The value corresponds to the position where the tail of the snake leads to when a player lands on the head of that snake.
    Snake = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}

#represents the mapping of ladder positions in a Snakes and Ladders game.

# In this dictionary:

# The keys represent the positions on the game board where the bottom of a ladder is located.
# The values represent the positions where the top of the ladder leads to when a player lands on the bottom of that ladder
    Ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}

LAST_TILE = 100

def __init__ (self, n_players, verbose = False):
        self.n_players = n_players
        self.verbose = verbose
        self.players = [0] * n_players
        self.turn = 0
        self.winner = None # used determine when the gave is over.

def die_roll(self):
        return randint(1,6)
    
    #define how to move a single player and position of a player

def move_player (self, player_i):
    prev_pos = self.players[player_i]
    new_pos = prev_pos + self.die_roll()

    if new_pos >= LAST_TILE: #winneer, game over!
        self.winner = player_i
        new_pos = self.LAST_TILE
    
    elif new_pos in self.Snake:
          new_pos = self.Snake[new_pos]
    
    elif new_pos in self.Ladder:
          new_pos = self.Ladder[new_pos]

    self.players[player_i] = new_pos

game = SnakeAndLadder(n_players = 2)
game.players
game.move_player(0)
game.players

def move_players (self):
      for player_i in range(self.n_players):
            self.move_player(player_i)
            if self.winner is not None:
                  break

def play_game(self):
      while self.winner is None:
            self.turn +=1
            self.move_players()
            is self.verbose:
            self.print_turn()

      return self.winner

def print_turn(self):
      self.turn
      



        


