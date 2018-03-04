from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('connect')
def connect():
    print('Client connected!')

@socketio.on('message')
def message(message):
    print(message)
    emit('message', {'state': 'message', 'message': message}, broadcast=True)
