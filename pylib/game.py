from player import Player

class Game(object):
    """Class representing the game. Primarily a collection of players"""

    # Game - constructor
    #
    # A game has a dictionary of players, which map their peer address to the
    # player object. TODO: Is this the best mapping? maybe need to do cookies and
    # proper session handling
    #
    # args:
    #   players - dictionary, defaults to empty dictionary
    def __init__(self, players={}):
        super(Game, self).__init__()
        self.players = players

    def __repr__(self):
        return "Game(%r)" % (self.players)

    def __str__(self):
        return "%r" % (self.players)

    # addPlayer
    #
    # Maps a peerAddress to a new player.
    #
    # args:
    #   peerAddress: address of where the player is connecting from
    def addPlayer(self, peerAddress):
        # TODO: Make name more intelligent than just the address
        self.players[peerAddress] = Player(peerAddress)