# WSGI app, via flask. Contains all the flask (static) endpoints
import uuid
from functools import wraps

from flask import *
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy

from pylib.instance import Secrets
from pylib.config import DatabaseConfiguration, FlaskSecurityConfiguration, MailConfiguration

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

# DB config
app.config.from_object(DatabaseConfiguration)
db = SQLAlchemy(app)

# Secrets!
app.config.from_object(Secrets)

# Mail config
app.config.from_object(MailConfiguration)
mail = Mail(app)

# Flask Security Config
app.config.from_object(FlaskSecurityConfiguration)

### BEGIN: Flask-security boilerplate
# Db models for flask-security users
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    db.session.commit()
### END: Flask-Security boilerplate


# TODO: Replace this with a real framework method?
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You no log in.')
            return redirect(url_for('login'))
    return wrap

# Flask socketio test
@app.route('/socketiotest')
# @login_required
def socket_io_test():
    return render_template('SocketIOTest.html')


@app.route('/socketiostresstest')
def socket_io_stress_test():
    return render_template('StressTestSocketIO.html')
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         user_id = check_login(request.form['username'], request.form['password'])
#         if user_id == None:
#             error = "Invalid Login"
#         else:
#             session['logged_in'] = True
#             return redirect(url_for('socket_io_test'))
#     return render_template('logins.html', error=error)


def check_login(username, password):
    if username == 'admin' and password == 'admin':
        return 1
    else:
        return None

# Autobahn socket test
@app.route('/socket_test')
def socket_test():
    return render_template('autobahnflasksockettest.html')