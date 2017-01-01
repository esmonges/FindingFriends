# Script to run the flask/socketio app
from FlaskConfiguration import app
from SocketIOConfiguration import socketio

if __name__ == '__main__':
    socketio.run(app)