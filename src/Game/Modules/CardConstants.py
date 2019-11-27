from enum import Enum, unique

@unique
class Suit(Enum):
    CLUB = 0x10
    SPADE = 0x20
    HEART = 0x30
    DIAMOND = 0x40
    TRUMP = 0x50
    SMALL = 0xe0
    BIG = 0xf0



@unique
class Rank(Enum):
    TWO = 0x01
    THREE = 0x02
    FOUR = 0x03
    FIVE = 0x04
    SIX = 0x05
    SEVEN = 0x06
    EIGHT = 0x07
    NINE = 0x08
    TEN = 0x09
    JACK = 0x0a
    QUEEN = 0x0b
    KING = 0x0c
    ACE = 0x0d
    TRUMP = 0x0e
    JOKER = 0x0f


# Suits
CLUB = 'CLUB'
SPADE = 'SPADE'
HEART = 'HEART'
DIAMOND = 'DIAMOND'
BIG = 'BIG'
SMALL = 'SMALL'
CARDSUITS = [CLUB, SPADE, HEART, DIAMOND]
JOKERSUITS = [SMALL, BIG]

# Numbers
TWO = 'TWO'
THREE = 'THREE'
FOUR = 'FOUR'
FIVE = 'FIVE'
SIX = 'SIX'
SEVEN = 'SEVEN'
EIGHT = 'EIGHT'
NINE = 'NINE'
TEN = 'TEN'
JACK = 'JACK'
QUEEN = 'QUEEN'
KING = 'KING'
ACE = 'ACE'
JOKER = 'JOKER'
NONJOKERNUMBERS = [TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]
NUMBERS = NONJOKERNUMBERS + [JOKER]

"""Class representing an individual card"""
# Numbers and their relative weights
NUMBERWEIGHTS = {
    TWO: 0x01,
    THREE: 0x02,
    FOUR: 0x03,
    FIVE: 0x04,
    SIX: 0x05,
    SEVEN: 0x06,
    EIGHT: 0x07,
    NINE: 0x08,
    TEN: 0x09,
    JACK: 0x0a,
    QUEEN: 0x0b,
    KING: 0x0c,
    ACE: 0x0d,
}
JOKERNUMBERWEIGHT = {
    JOKER: 0x0f,
}
# Special suits for jokers, and their relative display weights
JOKERSUITWEIGHTS = {
    BIG: 0xf0,
    SMALL: 0xe0,
}
# Card suits and their relative display weights
SUITWEIGHTS = {
    CLUB: 0x10,
    SPADE: 0x20,
    HEART: 0x30,
    DIAMOND: 0x40,
}
# Special weights for trump number and trump suit
TRUMPNUMBERWEIGHT = 0x0e
TRUMPSUITWEIGHT = 0x50