import unittest
from deck import Deck

class Deck_Test(unittest.TestCase):
    def setUp(self):
        return

    def test_construct(self):
        with self.assertRaises(AssertionError):
           Deck(0)
        for x in xrange(1, 10):
            d = Deck(x)
            self.assertEqual(d.getSize(), 54 * x)

    def test_draw(self):
        for x in xrange(1, 10):
            d = Deck(x)
            for y in xrange(1, 10):
                d.draw()
                self.assertEqual(d.getSize(), (54 * x) - y)

if __name__ == '__main__':
    unittest.main()



