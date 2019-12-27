from flask import Blueprint, render_template, Flask
from . import db

app = Flask(__name__)

app.config['SECRET_KEY'] = '\xcd\xa23\xf8LN:d\x8f&\xb3\x1d\t\x13$\x00\x9d\x96^:\x11!\xe7\xa5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def login():
    return render_template('profile.html')
