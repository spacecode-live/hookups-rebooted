from flask import Flask, render_template, abort
from flask_socketio import SocketIO
from sys import argv

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')
