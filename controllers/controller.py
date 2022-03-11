from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/<choice_1>/<choice_2>')
def choices(choice_1, choice_2):
    player_1 = Player("TestPlayer1", choice_1)
    player_2 = Player("TestPlayer2", choice_2)
    this_game = Game(player_1, player_2)
    winner = Game.play_game(this_game)
    return f"Choice 1 is {choice_1}, choice 2 is {choice_2}, winner is {winner}"


# def index():
    # return render_template('index.html', title='Home')