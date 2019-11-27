from src.Game.Modules.CardConstants import Suit, Rank


class Card(object):
    TRUMP_SUIT = None
    TRUMP_RANK = None

    def __init__(self, suit: Suit, number: Rank):
        """
        Constructs a card, represented by a suit, a number,
        whether or not it is a trump number, and whether or not
        it is a trump suit.

        Note that istrumpsuit will normally
        not be specified, as we do not know the trump suit
        until long after the cards have been generated. It is mostly
        for debugging purposes

        :param suit: Suit of the card. Must be in SUITS or JOKERSUITS
        :param number: Number of the card. Must be in NUMBERS
        """
        super(Card, self).__init__()
        self.suit = suit
        self.number = number

    def __repr__(self):
        """ Python representation for the card """
        return "%s(%r, %r, %r, %r)" % (
        'Card', self.get_suit(), self.get_rank(), self.isTrumpNumber(), self.isTrumpSuit())

    def __lt__(self, other):
        return self.getTotalWeight() < other.getTotalWeight()

    def __le__(self, other):
        return self.getTotalWeight() <= other.getTotalWeight()

    def __eq__(self, other):
        return self.suit == other.suit and self.getTotalWeight() == other.getTotalWeight()

    def getTotalWeight(self):
        """
        Gets the total weight for the Card based on its suit and number.
        This is only used for displaying the order of cards
        :return: The numeric weight for the card, based on its number and suit
        """
        return self.getNumberWeight() + self.getSuitWeight()

    def getNumberWeight(self):
        """
        Gets the weight of the number for this card, based on if the card is a trump number or not.
        :return: weight of the card's number
        """
        return Rank.TRUMP.value if self.isTrumpNumber() else self.number.value

    def getSuitWeight(self):
        """
        Gets the weight of the suit for this card, based on whether
        the card is trump suit
        :return: weight of the card's suit
        """
        return Suit.TRUMP.value if self.isTrumpSuit() else self.suit.value

    def get_suit(self) -> Suit:
        """
        Accessor for self.suit
        :return: self.suit
        """
        return self.suit

    def get_rank(self) -> Rank:
        """
        Accessor for self.number
        :return: self.number
        """
        return self.number

    def isTrumpNumber(self):
        """
        Accessor for self.istrumpnumber
        :return: self.istrumpnumber
        """
        return self.number == Card.TRUMP_RANK

    def isTrumpSuit(self):
        """
        Accessor for self.istrumpsuit. Note that this
        is only if the card is specified as in the trump
        suit, not if it is in the trump suit. Jokers are the
        exemption to this flag. See isInTrumpSuit
        :return: self.istrumpsuit
        """
        return self.suit == Card.TRUMP_SUIT

    def isInTrumpSuit(self):
        """
        Tells whether the card is in the trump suit. This includes
        cards that are explicitly in the trump suit (istrumpsuit == True)
        and cards that are implicitly in the trump suit (JOKERs). Assumes that
        trump numbers are always set to be in the trump suit correctly

        :return: True if the card is in the trump suit, False otherwise
        """
        return self.isTrumpSuit() or self.get_rank() == Rank.JOKER

    def setTrumpSuit(self, istrumpsuit):
        """
        Sets the card to be in or out of the trump suit.
        :param istrumpsuit: true or false
        :return: sets istrumpsuit for this card
        """
        if not istrumpsuit:
            assert not self.isTrumpNumber(), 'trump numbers must be trump suit'
        Card.set_trump_suit(self.get_suit()) if istrumpsuit else Card.set_trump_suit(None)

    @classmethod
    def set_trump_suit(cls, suit: Suit):
        cls.TRUMP_SUIT = suit

    @classmethod
    def set_trump_rank(cls, rank: Rank):
        cls.TRUMP_RANK = rank
