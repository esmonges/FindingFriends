class Card(object):
    """Class representing an individual card"""
    NUMBERS = {
    	'TWO': 0x02,
    	'THREE': 0x03,
    	'FOUR': 0x04,
    	'FIVE': 0x05,
    	'SIX': 0x06,
    	'SEVEN': 0x07,
    	'EIGHT': 0x08,
    	'NINE': 0x09,
    	'TEN': 0x0a,
    	'JACK': 0x0b,
    	'QUEEN': 0x0c,
    	'KING': 0x0d,
    	'ACE': 0x0e,
        'JOKER': 0x0f,
    }
    JOKERSUITS = {
    	'BIG': 0xf0,
    	'SMALL': 0xe0,
    }
    SUITS = {
    	'CLUB': 0x10,
    	'SPADE': 0x20,
    	'HEART': 0x30,
    	'DIAMOND': 0x40,
    }


    def __init__(self, suit, number):
        super(Card, self).__init__()

        # Card should have a number and a suit
        # If it is not a joker, it should be
        # one of the standard suits. If it is a joker,
        # it should be BIG or SMALL instead of one
        # of the standard suits
        assert (number in Card.getNumbers())
        if (number == 'JOKER'):
        	assert suit in Card.getJokerSuits()
        else :
        	assert suit in Card.getSuits()
        self.suit = suit
        self.number = number

    def __repr__(self):
        return "%s(%r, %r)" % ('Card', self.getSuit(), self.getNumber())

    def __cmp__(self, other):
        return self.getTotalWeight() - other.getTotalWeight()

    # Doesn't necessarily specify which cards are better. Just
    # used to specify how we sort them when they are displayed
    def getTotalWeight(self):
        return Card.getNumberWeight(self.getNumber()) + Card.getSuitWeight(self.getSuit())

    def getSuit(self):
        return self.suit

    def getNumber(self):
        return self.number

    @classmethod
    # Getter for NUMBERS constant
    def getNumbers(cls):
        return Card.NUMBERS.keys()

    @classmethod
    # Getter for JOKERSUITS constant
    def getJokerSuits(cls):
        return Card.JOKERSUITS.keys()

    @classmethod
    # Getter for SUITS constant
    def getSuits(cls):
        return Card.SUITS.keys()

    @classmethod
    def getNumberWeight(cls, number):
        return Card.NUMBERS[number]

    @classmethod
    def getSuitWeight(cls, suit):
        return dict(Card.SUITS.items() + Card.JOKERSUITS.items())[suit]

