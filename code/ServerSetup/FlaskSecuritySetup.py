from flask_security import Security, SQLAlchemyUserDatastore

from code.ServerSetup.DBSetup import User, Role, DBSetup
from code.ServerSetup.FlaskAppSetup import AppSetup


class FlaskSecuritySetup(object):
    security = None

    @staticmethod
    def get_security():
        if FlaskSecuritySetup.security is not None:
            return FlaskSecuritySetup.security

        db = DBSetup.get_db()
        # Setup Flask-Security
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        app = AppSetup.get_app()
        FlaskSecuritySetup.security = Security(app, user_datastore)
        return FlaskSecuritySetup.security
