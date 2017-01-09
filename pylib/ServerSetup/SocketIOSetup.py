# Module for all the socketio endpoints
from flask_socketio import SocketIO

from pylib.ServerSetup.FlaskAppSetup import AppSetup


class SocketIOSetup(object):
    socketio = None

    @staticmethod
    def get_socketio():
        if SocketIOSetup.socketio is not None:
            return SocketIOSetup.socketio
        app = AppSetup.get_app()
        SocketIOSetup.socketio = SocketIO(app)

        return SocketIOSetup.socketio
