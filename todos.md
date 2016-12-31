x Route some basic requests from the front end. Just do some basic echoing, ensure that autobahn is getting the request.
x Figure out how to identify a user, and manage their session (or if this is even the correct paradigm with sockets).
	NEXT GOAL: Make sure I can use Flask session managment stuff with sockets
		SHIT! I cant! Functions in my socket server module dont have access to the request context that flask provides. So I can either use a flask socket package, or use a more autobahn friendly webapp package. Twisted Klien appears to be a thing, but Ill need to convert over to WAMP. That said, the paradigm seems similar to flask, although I should check if it has similar session abstraction, since thats real real nice.
	Nothing!
		Basic login page
		Redirect to my socket page
		Need to start throwing stuff in session
		How much more does flask-login get me?
	Basic DB
		https://www.youtube.com/watch?v=BkdVq9ag7aw
		Factor out config nicely (see the from_object)
	Using flask-login
		Figure out all the flask-login methods. Build a session manager that just stores users in memory. No DB yet. Understand	what all the different states mean and how to modify them (active, authd, anon, etc).
		Figure out what the ids look like and how they make it into `login_manager.user_loader`
		Figure out if i can use all the authd mixins on socket operations
	Using flask-security
		Need to setup a DB, since it cares a lot about your ORM (user role permission). Maybe overkill for me? Flask-login might be good enough? Still will eventually need a DB.

Maybe get a game started, just build a deck in the game state manager.
Get a single user to be able to draw cards from the deck.

