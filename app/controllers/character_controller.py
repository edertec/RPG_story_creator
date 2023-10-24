from flask import Flask, render_template, request
from models import Character

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_story', methods=['POST'])
def create_story():
    character = Character(
        age=request.form['age'],
        skin=request.form['skin'],
        height=request.form['height'],
        eyes=request.form['eyes'],
        weight=request.form['weight'],
        other_features=request.form['other_features']
    )
    # Lógica para criar a história
    return render_template('story.html', character=character)
