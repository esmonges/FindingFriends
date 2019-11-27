import unittest
import copy
from src.Game.Modules.Player import Player
from src.Game.Modules.Card import Card
from src.Game.Modules import CardConstants


class Player_Test(unittest.TestCase):
    def test_insertCard(self):
        p = Player('Teddy', [])
        a = Card(suit=CardConstants.DIAMOND, number=CardConstants.FIVE)
        b = Card(suit=CardConstants.CLUB, number=CardConstants.TWO)
        c = Card(suit=CardConstants.CLUB, number=CardConstants.THREE)
        d = Card(suit=CardConstants.HEART, number=CardConstants.SIX, istrumpnumber=True, istrumpsuit=True)
        e = Card(suit=CardConstants.HEART, number=CardConstants.FIVE, istrumpsuit=True)
        f = Card(number=CardConstants.JOKER, suit=CardConstants.SMALL)
        g = Card(number=CardConstants.JOKER, suit=CardConstants.BIG)

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
