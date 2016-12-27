# WSGI app, via flask
import uuid

from flask import Flask
from flask import render_template
from flask_login import LoginManager
from flask_login import login_user

import FindingFriendsUserFactory

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())
# Make our app loginable
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return FindingFriendsUserFactory.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Some sort of form validation. Apparently WTForms is good
    # user = User()
    # login_user(user)


@app.route('/')
def page_home():
    return render_template('autobahnflasksockettest.html')