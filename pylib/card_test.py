import unittest
from card import Card

class Card_Test(unittest.TestCase):
    def setUp(self):
        self.numbers = Card.getNumbers() + Card.getJokerNumber()
        self.suits = Card.getSuits()
        self.jokersuits = Card.getJokerSuits()

    def test_allSuits(self):
        for suit in self.suits:
            for number in self.numbers:
                # Special case for jokers
                if (number == 'JOKER'):
                    with self.assertRaises(AssertionError):
                        Card(suit, number)
                else:
                    Card(suit, number)

    def test_jokerSuits(self):
        for suit in self.jokersuits:
            Card(suit, 'JOKER')

    def test_badSuit(self):
        with self.assertRaises(AssertionError):
            Card('LOLNO', 'ONE')

    def test_badNumber(self):
        with self.assertRaises(AssertionError):
            Card('SPADE', 'TREEFIDDY')

if __name__ == '__main__':
    unittest.main()

