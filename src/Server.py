# Script to run the flask/socketio app
from src.ServerSetup.FlaskAppSetup import AppSetup
from src.ServerSetup.SocketIOSetup import SocketIOSetup
from src.Routing.FlaskRoutes import SetupFlaskRoutes
from src.ServerSetup.DBSetup import DBSetup
from src.ServerSetup.FlaskSecuritySetup import FlaskSecuritySetup

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