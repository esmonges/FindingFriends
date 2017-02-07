x Route some basic requests from the front end. Just do some basic echoing, ensure that autobahn is getting the request.
x Figure out how to identify a user, and manage their session (or if this is even the correct paradigm with sockets).
	NEXT GOAL: Make sure I can use Flask session managment stuff with sockets
		x SHIT! I cant! Functions in my socket server module dont have access to the request context that flask provides.
		x So I can either use a flask socket package, or use a more autobahn friendly webapp package. Twisted Klien
		appears to be a thing, but Ill need to convert over to WAMP. That said, the paradigm seems similar to flask,
		although I should check if it has similar session abstraction, since thats real real nice.
		    x Twisted is more scalable (aka actually threaded/nonblocking) so I should stress test my server.
		        x Write up a thing with flask sockets, and then hit it with 6 simultaneous requests, and sleep during each.
		        see if it blocks the whole time or can do them in parallel
		            x Gross, they all block.
		            x Might want to use twisted, need to think about this more. Maybe just do a similar test and see what
		            happens.
		            x Maybe its fine? Only thing that could have race conditions is flipping for trump suit, but even then
		            it'll (probably) be fast enough that things can be done serially
        Hokay, so:
            x Next steps: write a flask thing with flask_socketio, and make sure session data can be used in the socket
            handlers and the app handlers
                it can! wooo
		x Basic login page
		x Redirect to my socket page
		x Need to start throwing stuff in session
	x Next: figure out which login framework to use. Build out users to easily identify players and collect persistent
	stats. Try to use an object for the login manager so it can be somewhat testable
	x How much more does flask-login get me?
	x     actually less, flask security sits on top of flask login
	x Basic DB
	x 	https://www.youtube.com/watch?v=BkdVq9ag7aw
	x 	Factor out config nicely (see the from_object)
	x Using flask-login
		Figure out all the flask-login methods. Build a session manager that just stores users in memory. No DB yet. Understand	what all the different states mean and how to modify them (active, authd, anon, etc).
		Figure out what the ids look like and how they make it into `login_manager.user_loader`
		Figure out if i can use all the authd mixins on socket operations
	x Using flask-security
		Need to setup a DB, since it cares a lot about your ORM (user role permission). Maybe overkill for me? Flask-login might be good enough? Still will eventually need a DB.
x Eventually refactor modules to more consistent naming scheme.
    x and refactor config
        x db should be separate
        x security should be separate
        x app should be separate
        x sockets should be separate
        x main should be separate
Maybe get a game started, just build a deck in the game state manager. Get the dealing routine working
    probably start with a lobby, get 2 users to register into a game and then kick off the game
        Gotta factor out some of the socket connection code into real js stuff
        maybe need static content serving?
        also make layout.html
            what is defining the template dir?
Eventually refactor models into a package
Get a single user to be able to draw cards from the deck.

