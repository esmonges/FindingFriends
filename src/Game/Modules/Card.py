from src.Game.Modules import CardConstants

JOKER = 'notajoker'

class Card(object):
    JOKER = 'Joker'

    # Card - Constructor
    #
    # Constructs a card, represented by a suit, a number,
    # whether or not it is a trump number, and whether or not
    # it is a trump suit. Note that istrumpsuit will normally
    # not be specified, as we do not know the trump suit
    # until long after the cards have been generated. It is mostly
    # for debugging purposes
    #
    # Args:
    #   suit: Suit of the card. Must be in SUITS or JOKERSUITS
    #   number: Number of the card. Must be in NUMBERS
    #   istrumpnumber: Optional. Is this card a trump number. Defaults
    #       to false
    #   istrumpsuit: Optional. Is the card in the trump suit. Note that this
    #       is not normally known at the time the cards are constructed, and
    #       should only be used for debugging purposes. Jokers have this
    #       set to false as they have their own special suits, but will behave
    #       as trumps (see isInTrumpSuit). Must be set to true for trump numbers
    #       Defaults to False
    #
    # returns:
    #   a Card object
    def __init__(self, suit, number, istrumpnumber=False, istrumpsuit=False):
        super(Card, self).__init__()

        # Card should have a number and a suit
        # If it is not a joker, it should be
        # one of the standard suits. If it is a joker,
        # it should be BIG or SMALL instead of one
        # of the standard suits
        assert number in CardConstants.NUMBERS, 'invalid number'
        if (number == CardConstants.JOKER):
            assert suit in CardConstants.JOKERSUITS, 'suit must be in joker suits for jokers'
        else:
            assert suit in CardConstants.CARDSUITS, 'invalid suit'

        # Trump numbers are always trump suits
        if (istrumpnumber):
            assert istrumpsuit, 'trump numbers must be in the trump suit explicitly'
        self.suit = suit
        self.number = number
        self.istrumpnumber = istrumpnumber
        self.istrumpsuit = istrumpsuit

    # __repr__
    # Python representation for the card
    def __repr__(self):
        return "%s(%r, %r, %r, %r)" % (
        'Card', self.getSuit(), self.getNumber(), self.isTrumpNumber(), self.isTrumpSuit())

    # __cmp__
    # Comparator for the card based on weight. Note that this
    # is only for display logic use, and will not dictate
    # the relative strength of cards in the game
    # def __cmp__(self, other):
    #     # TODO: Kill this off and use __lt__ and __eq__
    #     return self.getTotalWeight() - other.getTotalWeight()

    # TODO: some way to make type annotation `CARD` instead of `object`?
    def __lt__(self, other: object):
        return self.getTotalWeight() - other.getTotalWeight() < 0

    def __le__(self, other: object):
        return self.getTotalWeight() - other.getTotalWeight() <= 0

    def __eq__(self, other: object):
        return self.suit == other.suit and self.getTotalWeight() == other.getTotalWeight()

    # GetTotalWeight
    #
    # Gets the total weight for the Card based on its suit and number.
    # This is only used for displaying the order of cards
    #
    # args:
    #   none
    #
    # returns:
    #   The numeric weight for the card, based on its number and suit
    def getTotalWeight(self):
        return self.getNumberWeight() + self.getSuitWeight()

    # getNumberWeight
    #
    # Gets the weight of the number for this card, based on
    # if the card is a trump number or not.
    #
    # args:
    #   none
    # returns:
    #   weight of the card's number
    def getNumberWeight(self):
        if (self.isTrumpNumber()):
            return CardConstants.TRUMPNUMBERWEIGHT
        else:
            return Card.getConstantNumberWeight(self.getNumber())

    # getSuitWeight
    #
    # Gets the weight of the suit for this card, based on whether
    # the card is trump suit
    #
    # args:
    #   none
    # returns:
    #   weight of the card's suit
    def getSuitWeight(self):
        if (self.isTrumpSuit()):
            return CardConstants.TRUMPSUITWEIGHT
        else:
            return Card.getConstantSuitWeight(self.getSuit())

    # getSuit
    #
    # Accessor for self.suit
    #
    # args:
    #   none
    #
    # returns:
    #   self.suit
    def getSuit(self):
        return self.suit

    # getNumber
    #
    # Accessor for self.number
    #
    # args:
    #   none
    #
    # returns:
    #   self.number
    def getNumber(self):
        return self.number

    # isTrumpNumber
    #
    # Accessor for self.istrumpnumber
    #
    # args:
    #   none
    #
    # returns:
    #   self.istrumpnumber
    def isTrumpNumber(self):
        return self.istrumpnumber

    # isTrumpSuit
    #
    # Accessor for self.istrumpsuit. Note that this
    # is only if the card is specified as in the trump
    # suit, not if it is in the trump suit. Jokers are the
    # exemption to this flag. See isInTrumpSuit
    #
    # args:
    #   none
    #
    # returns:
    #   self.istrumpsuit
    def isTrumpSuit(self):
        return self.istrumpsuit

    # isInTrumpSuit
    #
    # Tells whether the card is in the trump suit. This includes
    # cards that are explicitly in the trump suit (istrumpsuit == True)
    # and cards that are implicitly in the trump suit (JOKERs). Assumes that
    # trump numbers are always set to be in the trump suit correctly
    #
    # args:
    #   none
    #
    # returns:
    #   True if the card is in the trump suit, False otherwise
    def isInTrumpSuit(self):
        return (self.isTrumpSuit() or self.getNumber() == CardConstants.JOKER)

    # setTrumpSuit
    #
    # Sets the card to be in or out of the trump suit.
    #
    # args:
    #   istrumpsuit: true or false
    #
    # returns:
    #   nothing
    #
    # effects:
    #   sets istrumpsuit for this card
    def setTrumpSuit(self, istrumpsuit):
        if (not istrumpsuit):
            assert not self.isTrumpNumber(), 'trump numbers must be trump suit'
        self.istrumpsuit = istrumpsuit
        return

    # getConstantNumberWeight
    #
    # Accessor for the relative weight of a number
    #
    # args:
    #   number: key into NUMBERS
    #
    # returns:
    #   weight of the given number
    @classmethod
    def getConstantNumberWeight(cls, number):
        if (number == CardConstants.JOKER):
            return CardConstants.JOKERNUMBERWEIGHT[number]
        return CardConstants.NUMBERWEIGHTS[number]

    # getConstantSuitWeight
    #
    # Accessor for the weight of a given suit
    #
    # args:
    #   suit: key into SUITS or JOKERSUITS
    #
    # returns:
    #   weight of the given suit
    @classmethod
    def getConstantSuitWeight(cls, suit):
        if (suit in CardConstants.JOKERSUITS):
            return CardConstants.JOKERSUITWEIGHTS[suit]
        return CardConstants.SUITWEIGHTS[suit]
