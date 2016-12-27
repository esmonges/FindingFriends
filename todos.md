Route some basic requests from the front end. Just do some basic echoing, ensure that autobahn is getting the request.
x Figure out how to identify a user, and manage their session (or if this is even the correct paradigm with sockets).
	Using flask-login
		Figure out all the flask-login methods. Build a session manager that just stores users in memory. No DB yet. Understand
		what all the different states mean and how to modify them (active, authd, anon, etc).
		Figure out what the ids look like and how they make it into `login_manager.user_loader`
		Figure out if i can use all the authd mixins on socket operations

Maybe get a game started, just build a deck in the game state manager.
Get a single user to be able to draw cards from the deck.

