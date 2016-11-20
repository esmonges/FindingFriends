class Card(object):
    """Class representing an individual card"""
    NUMBERS = (
    	'ONE',
    	'TWO',
    	'THREE',
    	'FOUR',
    	'FIVE',
    	'SIX',
    	'SEVEN',
    	'EIGHT',
    	'NINE',
    	'TEN',
    	'JACK',
    	'QUEEN',
    	'KING',
    	'ACE',
    )
    JOKERNUMBER = ('JOKER',)
    JOKERSUITS = (
    	'BIG',
    	'SMALL',
    )
    SUITS = (
    	'CLUB',
    	'SPADE',
    	'HEART',
    	'DIAMOND',
    )

    def __init__(self, suit, number):
        super(Card, self).__init__()

        # Card should have a number and a suit
        # If it is not a joker, it should be
        # one of the standard suits. If it is a joker,
        # it should be BIG or SMALL instead of one
        # of the standard suits
        assert (number in self.NUMBERS + self.JOKERNUMBER)
        if (number == 'JOKER'):
        	assert suit in self.JOKERSUITS
        else :
        	assert suit in self.SUITS

        self.suit = suit
        self.number = number

    @classmethod
    # Getter for NUMBERS constant
    def getNumbers(cls):
        return Card.NUMBERS

    @classmethod
    # Getter for JOKERSUITS constant
    def getJokerSuits(cls):
        return Card.JOKERSUITS

    @classmethod
    # Getter for SUITS constant
    def getSuits(cls):
        return Card.SUITS

    @classmethod
    def getJokerNumber(cls):
        return Card.JOKERNUMBER

