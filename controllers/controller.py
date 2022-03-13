from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/<choice_1>/<choice_2>')
def choices(choice_1, choice_2):
    player_1 = Player("Fred", choice_1)
    player_2 = Player("Bill", choice_2)
    this_game = Game(player_1, player_2)
    winner = Game.play_game(this_game)
    return render_template("index.html", name_1=player_1.name, name_2=player_2.name, choice_1=choice_1, choice_2=choice_2, winner=winner)
