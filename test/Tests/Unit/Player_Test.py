import unittest
import copy
from src.Game.Modules.Player import Player
from src.Game.Modules.Card import Card
from src.Game.Modules import CardConstants
from src.Game.Modules.CardConstants import Suit, Rank


class Player_Test(unittest.TestCase):
    def test_insertCard(self):
        p = Player('Teddy', [])
        Card.set_trump_suit(Suit.HEART)
        Card.set_trump_rank(Rank.SIX)
        a = Card(suit=Suit.DIAMOND, number=Rank.FIVE)
        b = Card(suit=Suit.CLUB, number=Rank.TWO)
        c = Card(suit=Suit.CLUB, number=Rank.THREE)
        d = Card(suit=Suit.HEART, number=Rank.SIX)
        e = Card(suit=Suit.HEART, number=Rank.FIVE)
        f = Card(suit=Suit.SMALL, number=Rank.JOKER)
        g = Card(suit=Suit.BIG, number=Rank.JOKER)

        p.add_card_to_hand(a)
        self.assertTrue(p.get_hand() == [copy.deepcopy(a)])
        # Yeah, this is a little error-prone, since it's the
        # same object. But this is just for testing purposes.
        # Probably best to avoid this in real src
        p.add_card_to_hand(a)
        self.assertTrue(p.get_hand() == [copy.deepcopy(a), copy.deepcopy(a)])

        p.add_card_to_hand(copy.deepcopy(b))
        p.add_card_to_hand(copy.deepcopy(c))
        self.assertTrue(p.get_hand() == [b, c, a, a])

        p.add_card_to_hand(d)
        p.add_card_to_hand(e)
        self.assertTrue(p.get_hand() == [b, c, a, a, e, d])
        # Mix it up to keep us on our toes
        self.assertFalse(p.get_hand() == [a, a, b, c, d, e])

        # Switched the order to stress test things. Totally
        # not because I screwed up earlier...

        p.add_card_to_hand(f)
        p.add_card_to_hand(g)
        self.assertTrue(p.get_hand() == [b, c, a, a, e, d, f, g])


if __name__ == '__main__':
    unittest.main()
