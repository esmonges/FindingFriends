import unittest
from src.Game.Modules.Card import Card
from src.Game.Modules import CardConstants
from src.Game.Modules.CardConstants import Suit, Rank

class Card_Test(unittest.TestCase):
    def setUp(self):
        self.numbers = CardConstants.NUMBERS
        self.suits = CardConstants.CARDSUITS
        self.jokersuits = CardConstants.JOKERSUITS
        Card.clear_trumps()

    def test_eq(self):
        for suit1 in self.suits:
            for suit2 in self.suits:
                suitsequal = (suit1 == suit2)
                for number1 in self.numbers:
                    for number2 in self.numbers:
                        if (
                            (number1 == Rank.JOKER and suit1 not in self.jokersuits)
                            or (number2 == Rank.JOKER and suit2 not in self.jokersuits)
                        ):
                            continue
                        numbersequal = (number1 == number2)
                        cardsequal = (numbersequal and suitsequal)
                        card1 = Card(suit=suit1, number=number1)
                        card2 = Card(suit=suit2, number=number2)
                        self.assertEqual(cardsequal, card1 == card2)

    def test_normal_ranking(self):
        """This unit test. Test if the normal card rankings work"""
        a = Card(suit=Suit.DIAMOND, number=Rank.ACE)
        b = Card(suit=Suit.DIAMOND, number=Rank.TEN)
        self.assertFalse(a < b)
        self.assertFalse(a <= b)
        self.assertTrue(a > b)
        self.assertTrue(a >= b)
        b = Card(suit=Suit.DIAMOND, number=Rank.ACE)
        self.assertFalse(a > b)
        self.assertTrue(a >= b)
        self.assertFalse(a < b)
        self.assertTrue(a <= b)
        b = Card(suit=Suit.BIG, number=Rank.JOKER)
        self.assertFalse(a > b)
        self.assertFalse(a >= b)
        self.assertTrue(a < b)
        self.assertTrue(a <= b)

    def test_trump_rankings(self):
        """This unit test, test if the Trump cards escalate value"""
        Card.set_trump_rank(Rank.TWO)
        Card.set_trump_suit(Suit.SPADE)
        a = Card(suit=Suit.DIAMOND, number=Rank.ACE)
        b = Card(suit=Suit.SPADE, number=Rank.TWO)
        self.assertFalse(a > b)
        self.assertFalse(a >= b)
        self.assertTrue(a < b)
        self.assertTrue(a <= b)

        Card.set_trump_suit(Suit.CLUB)
        b = Card(suit=Suit.CLUB, number=Rank.THREE)
        self.assertFalse(a > b)
        self.assertFalse(a >= b)
        self.assertTrue(a < b)
        self.assertTrue(a <= b)

        a = Card(suit=Suit.CLUB, number=Rank.FOUR)
        self.assertTrue(a > b)
        self.assertTrue(a >= b)
        self.assertFalse(a < b)
        self.assertFalse(a <= b)

        Card.set_trump_rank(Rank.FIVE)
        Card.set_trump_suit(Suit.CLUB)
        a = Card(suit=Suit.CLUB, number=Rank.FIVE)
        self.assertTrue(a > b)
        self.assertTrue(a >= b)
        self.assertFalse(a < b)
        self.assertFalse(a <= b)

    def test_istrumpnumber(self):
        Card.set_trump_suit(Suit.DIAMOND)
        Card.set_trump_rank(Rank.FIVE)
        a = Card(suit=Suit.DIAMOND, number=Rank.FIVE)
        self.assertTrue(a.isTrumpNumber())

        Card.set_trump_suit(None)
        Card.set_trump_rank(None)
        a = Card(suit=Suit.DIAMOND, number=Rank.FIVE)
        self.assertFalse(a.isTrumpNumber())

    def test_istrumpsuit(self):
        a = Card(suit=Suit.DIAMOND, number=Rank.FIVE)
        self.assertFalse(a.isTrumpSuit())
        a.setTrumpSuit(istrumpsuit=True)
        self.assertTrue(a.isTrumpSuit())

        Card.set_trump_suit(Suit.DIAMOND)
        a = Card(suit=Suit.DIAMOND, number=Rank.SIX)
        self.assertTrue(a.isTrumpSuit())
        a.setTrumpSuit(istrumpsuit=False)
        self.assertFalse(a.isTrumpSuit())

        Card.set_trump_suit(Suit.DIAMOND)
        Card.set_trump_rank(Rank.TEN)
        a = Card(suit=Suit.DIAMOND, number=Rank.TEN)
        self.assertTrue(a.isTrumpSuit())
        with self.assertRaises(AssertionError):
            a.setTrumpSuit(False)