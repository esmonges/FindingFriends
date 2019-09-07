from src.Game.Modules.Round import Round
from src.Game.Modules.Randomizer import Randomizer
from src.Game.Modules.Player import Player
from src.Game.Modules import Card

class Game(object):
    """Class representing the game. Primarily a collection of players"""

    players = []  # type: List[Player]
    firstDrawPlayer = "" #TODO is there a null?
    firstDrawPlayerIndex = 0 #should always be the case
    currentRound = False   # type: Round
    previousRounds = False
    randomizer = False  # type: Randomizer


    # Game - constructor
    #
    # A game has a dictionary of players, which map their peer address to the
    # player object. TODO: Is this the best mapping? maybe need to do cookies and
    # proper session handling
    #
    # args:
    #   players - dictionary, defaults to empty dictionary
    def __init__(self, players=False, randomizer=False):
        super(Game, self).__init__()
        if not players:
            players = [] # Do this to get around players=[] resulting in "[]" being a ref that persists call to call (WTF)
        if not randomizer:
            randomizer = Randomizer()

        self.players = players
        self.randomizer = randomizer

    def __repr__(self):
        return "Game(%r)" % (self.players)

    def __str__(self):
        return "%r" % (self.players)

    # addPlayer
    #
    # Adds a player to the game
    #
    # args:
    #   player: Player object to add to the game
    def registerPlayer(self, player):
        self.players.append(player)

    def startRound(self):
        self.currentRound = Round(self.players, self.randomizer)
