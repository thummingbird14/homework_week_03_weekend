import random

class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self):
        if self.player_1.choice == self.player_2.choice:
            return "Draw"
        if self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return self.player_1.name
        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_1.name
        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return self.player_1.name
        else:
            return self.player_2.name

    def make_random_choice():
        moves = ["rock", "paper", "scissors"]
        choice = random.choice(moves)
        return choice

