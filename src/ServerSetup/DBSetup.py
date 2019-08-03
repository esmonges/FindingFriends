from flask_sqlalchemy import SQLAlchemy, Model
from flask_security import UserMixin, RoleMixin

from src.ServerSetup.FlaskAppSetup import AppSetup


class DBSetup(object):

    db = None

    @staticmethod
    def get_db():
        if DBSetup.db is not None:
            return DBSetup.db

        # Exception here: need to make things static
        app = AppSetup.get_app()
        DBSetup.db = SQLAlchemy(app)

        # Ensure tables are created before the app serves anything
        @app.before_first_request
        def create_tables():
            DBSetup.db.create_all()
            DBSetup.db.session.commit()

        return DBSetup.db

    @staticmethod
    def get_db_model():
        return DBSetup.get_db().Model


# BEGIN: Flask_Security User/Role schema
class Role(DBSetup.get_db_model(), RoleMixin):
    db = DBSetup.get_db()
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(DBSetup.get_db_model(), UserMixin):
    db = DBSetup.get_db()
    roles_users = db.Table('roles_users',
           db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
           db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
# END: Flask_Security User/Role schema
