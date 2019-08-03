# WSGI app, via flask. Contains all the flask (static) endpoints
import uuid

from flask import *
from flask_mail import Mail

from src.Instance import Secrets
from src.Config import DatabaseConfiguration, FlaskSecurityConfiguration, MailConfiguration


class AppSetup(object):
    app = None

    @staticmethod
    def get_app():
        # Object cache the app so we don't reinit it
        if AppSetup.app is not None:
            return AppSetup.app

        AppSetup.app = Flask(__name__)
        AppSetup.app.secret_key = str(uuid.uuid4())

        # DB Config; actual connection and schema construction happens in DBSetup.py
        AppSetup.app.config.from_object(DatabaseConfiguration)

        # Secrets!
        AppSetup.app.config.from_object(Secrets)

        # Mail Config
        AppSetup.app.config.from_object(MailConfiguration)
        Mail(AppSetup.app)

        # Flask Security Config
        AppSetup.app.config.from_object(FlaskSecurityConfiguration)

        return AppSetup.app
