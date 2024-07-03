from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize players list
players = []

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def total_score(self):
        return sum(self.scores)

@app.route('/')
def index():
    return render_template('index.html', players=players)

@app.route('/add_player', methods=['POST'])
def add_player():
    name = request.form.get('name')
    if name:
        players.append(Player(name))
    return redirect(url_for('index'))

@app.route('/add_score', methods=['POST'])
def add_score():
    name = request.form.get('name')
    score = request.form.get('score')
    if name and score:
        for player in players:
            if player.name == name:
                player.add_score(int(score))
                break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
