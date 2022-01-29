from flask import render_template
from app import app
from models.players_list import players
from models.game_runs import game

@app.route('/rock/paper')
def index():
    return render_template('index.html')

@app.route('/coolgame')
def index2():
    return render_template('index2.html', players = players, game_runs = game.game(players[0].choice, players[1].choice))

@app.route('/')
def index3():
    return render_template('welcome.html')