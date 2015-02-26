from card import Card
import random

class Deck(object):
    """Object representing a deck that can contain any multiple of 54 cards"""
    def __init__(self, cardsets):
        super(Deck, self).__init__()
        assert (cardsets >= 1)
        self.cardsets = cardsets
        self.generateDeck()
        self.shuffleDeck()

    def __repr__(self):
        return "%s(%r)" % ('Deck', self.cardsets)

    def __str__(self):
        return str(self.deck)

    def generateDeck(self):
        self.deck = []
        # Generate full deck
        for i in range(self.cardsets):
            self.deck += [
                Card(suit, number)
                for
                    suit
                in
                    Card.getSuits()
                for
                    number
                in
                    Card.getNumbers()
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

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def getSize(self):
        return len(self.deck)

    def draw(self):
        return self.deck.pop()


