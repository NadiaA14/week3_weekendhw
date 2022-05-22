from app import app
from flask import render_template, request
from models.game import *

@app.route("/")
def index():
    return render_template("index.html", title="Rock, Paper, Scissors")

@app.route("/twoplayers", method=['POST'])
def play_game():
    choice_a = request.form["choice_a"]
    choice_b = request.form["choice_b"]
    player_1 = Game("Player 1", choice_a)
    player_2 = Game("Player 2", choice_b)

    return render_template("twoplayers.html", player_1=player_1, player_2=player_2)
