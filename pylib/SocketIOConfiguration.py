# Module for all the socketio endpoints

from FlaskConfiguration import app
from flask_socketio import SocketIO, emit

# for testing
import time

socketio = SocketIO(app, )


# TODO: Other namespaces?? Think chatroom
@socketio.on('connect', namespace='/test')
def connect():
    print('someone connected!')
    emit('my_response', {'data': 'Connected from server!'})


@socketio.on('my_event', namespace='/test')
def test_message(msg):
    print('got message')
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

