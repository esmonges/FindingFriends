# WSGI app, via flask
import uuid

from flask import *
from functools import wraps

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_id = check_login(request.form['username'], request.form['password'])
        if user_id == None:
            error = "Invalid Login"
        else:
            session['logged_in'] = True
            return redirect(url_for('socket_test'))
    return render_template('login.html', error=error)

def check_login(username, password):
    if username == 'admin' and password == 'admin':
        return 1
    else:
        return None

@app.route('/socket_test')
def socket_test():
    return render_template('autobahnflasksockettest.html')