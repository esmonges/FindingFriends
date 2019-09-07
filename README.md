FindingFriends
==============

# DEPRECATED

THIS IS DEPRECATED IN FAVOR OF https://github.com/esmongeski/FindingFriends
(I lost access to the account this was living under. Please see the fork for all
future commits)

# LEGACY

Application to play Finding Friends aka Chinese Bridge (https://en.wikipedia.org/wiki/Sheng_Ji)

Mostly a python backend, webapp frontend, likely will be React/Redux down the line.

# Project overview
`src` directory contains all the code.

Most of the meat is in `Game` right now, which includes a TDD approach particularly
using a large integration test to simulate playing the game (`Game_Test.py`)

For the server itself, I've been messing around with websockets and using Flask for
managing the key endpoints. At one point I was using `flask_socketio` for managing
socket communication, as teh app will eventually need to be websocket based to support
simultaneous communication between all the players and the server orchestrating the game.

DB interaction will be via SQLAlchemy (using sqlite).

# Notes/non-obvious things
This is a perpetual WIP and may never work on its own. I'll update as I go.

Credentials for the email account `ffbridgeserver@gmail.com` need to be stored
locally for the app to send account verification emails through flask's framework.
If you want to fork this you'll need to add your own email and credentials, or
ask me for the email password.