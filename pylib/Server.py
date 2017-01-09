# Script to run the flask/socketio app
from pylib.ServerSetup.FlaskAppSetup import AppSetup
from pylib.ServerSetup.SocketIOSetup import SocketIOSetup
from pylib.Routing.FlaskRoutes import SetupFlaskRoutes
from pylib.ServerSetup.DBSetup import DBSetup
from pylib.ServerSetup.FlaskSecuritySetup import FlaskSecuritySetup

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