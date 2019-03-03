from Card import Card
from Randomizer import Randomizer
import random

class Deck(object):
    """Object representing a deck that can contain any multiple of 54 cards"""
    deck = False  # type: List[Card]
    cardsets = 0
    randomizer = False

    # Deck - Constructor
    #
    # Constructs a deck with a given number of cardsets. For each cardset, an
    # individual 54 card deck will be constructed and pushed to the playing deck
    #
    # args:
    #   cardsets: Number of sets of 54 cards to use
    #
    # returns:
    #   Deck object
    def __init__(self, cardsets, randomizer=False):
        super(Deck, self).__init__()
        if not randomizer:
            randomizer = Randomizer()
        assert (cardsets >= 1)
        self.cardsets = cardsets
        self.randomizer = randomizer

    # __repr__
    # Python representation for this deck
    def __repr__(self):
        return "%s(%r)" % ('Deck', self.cardsets)

    # __str__
    # string representation of the deck
    def __str__(self):
        return str(self.deck)

    # generateDeck
    #
    # Generates a deck based on the number of cardsets
    #
    # args:
    #   none
    #
    # returns:
    #   nothing
    #
    # effects:
    #   Creates a deck of self.cardsets * 54 cards containing self.cardsets
    #   copies of each individual card
    def generateDeck(self):
        self.deck = []
        # Generate full deck
        for i in range(self.getCardsets()):
            self.deck += [
                Card(suit, number)
                for
                    suit
                in
                    Card.getSuits()
                for
                    number
                in
                    Card.getNonJokerNumbers()
            ]
            self.deck += [
                Card(suit, number)
                for
                    suit
                in
                    Card.getJokerSuits()
                for
                    number
                in
                    Card.getJokerNumber()
            ]
        return

    # shuffleDeck
    #
    # Randomizes the deck
    #
    # args:
    #   none
    #
    # returns:
    #   nothing
    #
    # effects:
    #   randomizes self.deck
    def shuffleDeck(self):
        self.deck = self.randomizer.shuffle(self.deck)
        return

    # getCardsets
    #
    # Accessor for self.cardsets
    #
    # args:
    #   none
    #
    # returns:
    #   self.cardsets
    def getCardsets(self):
        return self.cardsets

    # getDeck
    #
    # Accessor for self.deck
    #
    # args:
    #   none
    #
    # returns:
    #   self.deck
    def getDeck(self):
        return self.deck

    # getSize
    #
    # Gets the size of the deck
    #
    # args:
    #   none
    #
    # return:
    #   size of the deck
    def getSize(self):
        return len(self.deck)

    def isEmpty(self):
        # type: () -> bool
        return self.getSize() == 0

    # draw
    #
    # Draws a card off of the deck
    #
    # args:
    #   none
    #
    # returns:
    #   top card of the deck
    #
    # effects:
    #   removes top card from the deck
    def draw(self):
        return self.deck.pop()


