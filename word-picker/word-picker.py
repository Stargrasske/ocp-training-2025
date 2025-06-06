from random import choice
from flask import Flask

app = Flask(__name__)

choices = ["first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth"]

@app.route('/')
def pick_word():
    return choice(choices).strip()