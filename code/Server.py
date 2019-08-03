# Script to run the flask/socketio app
from code.ServerSetup.FlaskAppSetup import AppSetup
from code.ServerSetup.SocketIOSetup import SocketIOSetup
from code.Routing.FlaskRoutes import SetupFlaskRoutes
from code.ServerSetup.DBSetup import DBSetup
from code.ServerSetup.FlaskSecuritySetup import FlaskSecuritySetup

if __name__ == '__main__':
    app = AppSetup.get_app()
    socketio = SocketIOSetup.get_socketio()
    # Ensure DB Is set up
    DBSetup.get_db()
    # Ensure flask security is set up
    FlaskSecuritySetup.get_security()
    # Ensure flask routes are set up
    SetupFlaskRoutes.setup_flask_routes()

    # run the app
    socketio.run(app)