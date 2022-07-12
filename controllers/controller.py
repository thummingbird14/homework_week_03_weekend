from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/<choice_1>/<choice_2>')
def choices(choice_1, choice_2):
    player_1 = Player("Player1", choice_1)
    player_2 = Player("Player2", choice_2)
    this_game = Game(player_1, player_2)
    winner = Game.play_game(this_game)
    return render_template("index.html", name_1=player_1.name, name_2=player_2.name, choice_1=choice_1, choice_2=choice_2, winner=winner)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play', methods=['POST'])
def random_choice():
    name_1 = request.form['username']
    choice_1 = request.form['move']
    name_2 = 'Computer'
    choice_2 = Game.make_random_choice()
    player_1 = Player(name_1, choice_1)
    player_2 = Player(name_2, choice_2)
    that_game = Game(player_1, player_2)
    winner = Game.play_game(that_game)
    return render_template('index.html', name_1=player_1.name, name_2=player_2.name, choice_1=choice_1, choice_2=choice_2, winner=winner)
    