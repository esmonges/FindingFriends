import unittest
from src.Game.Modules.Player import Player
from src.Game.Modules.Card import Card


class Player_Test(unittest.TestCase):
    def test_insertCard(self):
        p = Player('Teddy', [])
        a = Card(suit='DIAMOND', number='FIVE')
        p.addCardToHand(a)
        self.assertTrue(p.getHand() == [a])
        # Yeah, this is a little error-prone, since it's the
        # same object. But this is just for testing purposes.
        # Probably best to avoid this in real src
        p.addCardToHand(a)
        self.assertTrue(p.getHand() == [a, a])

        b = Card(suit='CLUB', number='TWO')
        p.addCardToHand(b)
        c = Card(suit='CLUB', number='THREE')
        p.addCardToHand(c)
        self.assertTrue(p.getHand() == [b, c, a, a])

        d = Card(suit='HEART', number='SIX', istrumpnumber=True, istrumpsuit=True)
        p.addCardToHand(d)
        e = Card(suit='HEART', number='FIVE', istrumpsuit=True)
        p.addCardToHand(e)
        self.assertTrue(p.getHand() == [b, c, a, a, e, d])
        # Mix it up to keep us on our toes
        self.assertFalse(p.getHand() == [a, a, b, c, d, e])

        # Switched the order to stess test things. Totally
        # not because I screwed up earlier...
        f = Card(number='JOKER', suit='SMALL')
        p.addCardToHand(f)
        g = Card(number='JOKER', suit='BIG')
        p.addCardToHand(g)
        self.assertTrue(p.getHand() == [b, c, a, a, e, d, f, g])


if __name__ == '__main__':
    unittest.main()
