class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self):
        if self.player_1.choice == self.player_2.choice:
            return None
        if self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return "Player 1"
        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return "Player 1"
        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return "Player 1"
            # return self.player_1
        else:
            return "Player 2"
            # return self.player_2

