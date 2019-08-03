import time

from flask_socketio import emit
from flask import session

from src.ServerSetup.SocketIOSetup import SocketIOSetup


class SocketIORoutes(object):
    routes_are_setup = False

    @staticmethod
    def setup_socketio_routes():
        if SocketIORoutes.routes_are_setup is not True:
            socketio = SocketIOSetup.get_socketio()

            # Define all the socketio routes
            # TODO: Other namespaces?? Think chatroom
            @socketio.on('connect', namespace='/test')
            def connect():
                print('someone connected!')
                emit('my_response', {'data': 'Connected from server!'})

            @socketio.on('my_event', namespace='/test')
            # @login_required
            def test_message(msg):
                print('got message')
                print(session)
                print(msg)
                emit('my_response', {'data': msg['data']})

            # Test to see if several simultaneous events will block eachother
            @socketio.on('stress_test_event', namespace='/test')
            def stress_test(msg):
                print('got, sleeping')
                print(msg)
                time.sleep(5)
                print('done sleeping')
                emit('stress_test_response', {'data': msg['data']})
                emit('stress_test_response', {'data': msg['data']}, broadcast=True)

            SocketIORoutes.routes_are_setup = True
