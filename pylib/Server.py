# Script to run the flask/socketio app
from SocketIOSetup import socketio
from FlaskAppSetup import app

if __name__ == '__main__':
    socketio.run(app)