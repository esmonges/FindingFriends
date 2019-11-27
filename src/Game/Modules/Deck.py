from src.Game.Modules.Card import Card
from src.Game.Modules.CardConstants import Suit, Rank, CARDSUITS,JOKERSUITS, NONJOKERNUMBERS
from src.Game.Modules.Randomizer import Randomizer


class Deck(object):
    def __init__(self, cardsets:int, randomizer=Randomizer()):
        """
        Object representing a deck that can contain any multiple of 54 cards
        For each cardset, an individual 54 card deck will be constructed and pushed to the playing deck

        :param cardsets: Number of sets of 54 cards to use
        :param randomizer: Object that shuffles the deck
        """
        super(Deck, self).__init__()
        assert (cardsets >= 1)
        self.cardsets = cardsets
        self.randomizer = randomizer
        self.deck = list()

    def __repr__(self):
        """Python representation for this deck"""
        return "%s(%r)" % ('Deck', self.cardsets)

    def __str__(self):
        """ string representation of the deck """
        return str(self.deck)

    def generateDeck(self):
        """
        Generates a deck based on the number of cardsets
        Creates a deck of self.cardsets * 54 cards containing self.cardsets copies of each individual card
        :return:
        """
        self.deck = Deck.generate_single_deck() * self.getCardsets()

    @staticmethod
    def generate_single_deck():
        """
        Generates a full list of Cards with jokers included
        :return: a list of cards
        """
        non_joker_card = [Card(suit, number) for suit in CARDSUITS for number in NONJOKERNUMBERS]
        joker_card = [Card(suit, number) for suit in JOKERSUITS for number in [Rank.JOKER]]
        return non_joker_card + joker_card

    def shuffleDeck(self):
        """Randomizes the deck"""
        self.deck = self.randomizer.shuffle(self.deck)

    def getCardsets(self):
        """ Number of decks to generate"""
        return self.cardsets

    def getDeck(self):
        """Accessor for self.deck"""
        return self.deck

    def getSize(self):
        """Gets the size of the deck"""
        return len(self.deck)

    def isEmpty(self) -> bool:
        """A check if the deck is empty"""
        return self.getSize() == 0

    def draw(self):
        """removes top card from the deck"""
        return self.deck.pop()


