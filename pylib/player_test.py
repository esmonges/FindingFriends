import unittest
from player import Player
from card import Card

class Player_Test(unittest.TestCase):

    def test_insertCard(self):
        p = Player('Teddy', [])
        a = Card(suit='DIAMOND', number='FIVE')
        p.insertCard(a)
        self.assertTrue(p.getHand() == [a])
        # Yeah, this is a little error-prone, since it's the
        # same object. But this is just for testing purposes.
        # Probably best to avoid this in real code
        p.insertCard(a)
        self.assertTrue(p.getHand() == [a,a])

        b = Card(suit='CLUB', number='TWO')
        p.insertCard(b)
        c = Card(suit='CLUB', number='THREE')
        p.insertCard(c)
        self.assertTrue(p.getHand() == [b,c,a,a])

        d = Card(suit='HEART', number='SIX', istrumpnumber=True, istrumpsuit=True)
        p.insertCard(d)
        e = Card(suit='HEART', number='FIVE', istrumpsuit=True)
        p.insertCard(e)
        self.assertTrue(p.getHand() == [b,c,a,a,e,d])
        # Mix it up to keep us on our toes
        self.assertFalse(p.getHand() == [a,a,b,c,d,e])

        # Switched the order to stess test things. Totally
        # not because I screwed up earlier...
        f = Card(number='JOKER', suit='SMALL')
        p.insertCard(f)
        g = Card(number='JOKER', suit='BIG')
        p.insertCard(g)
        self.assertTrue(p.getHand() == [b,c,a,a,e,d,f,g])


if __name__ == '__main__':
    unittest.main()
