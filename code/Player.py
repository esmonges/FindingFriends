import bisect
from Card import Card

class Player(object):
    """class representing a Player in the game"""
    # Player - constructor
    #
    # A player has a name and a hand of cards. Constructs the player object
    # based on their name and a list of cards (defaults to empty list)
    #
    # args:
    #   name: string that is the name of the player
    #   hand: Optional; list of Card objects. Defaults to []
    #
    # returns:
    #   Player object
    def __init__(self, name, hand=[]):
        super(Player, self).__init__()
        self.name = name
        hand.sort()
        self.hand = hand

    # __repr__
    # Python representation for this Player
    def __repr__(self):
        return "Player(%r, %r)" % (self.name, self.hand)

    # __str__
    # String representing the player
    def __str__(self):
        return "%r %r" % (self.name, str(self.hand))

    # insertCard
    #
    # Method to stick a card into a player's hand
    #
    # args:
    #   card: Card object to put into the hand
    #
    # returns:
    #   nothing
    #
    # effects:
    #   inserts card into self.hand in a sorted manner
    def insertCard(self, card):
        assert type(card) is Card, 'card must be a Card'
        bisect.insort(self.hand, card);
        return

    # getHand
    #
    # accessor for hand
    #
    # args:
    #   none
    #
    # returns:
    #   self.hand
    def getHand(self):
        return self.hand

