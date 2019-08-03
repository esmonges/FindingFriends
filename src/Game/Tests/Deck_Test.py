import unittest
from src.Game.Modules.Deck import Deck

class Deck_Test(unittest.TestCase):
    def setUp(self):
        return

    def test_construct(self):
        with self.assertRaises(AssertionError):
           Deck(0)

    def test_it_generates_cardsets(self):
        for x in range(1, 10):
            d = Deck(x)
            d.generateDeck()
            self.assertEqual(d.getSize(), 54 * x)

    def test_draw(self):
        for x in range(1, 10):
            d = Deck(x)
            d.generateDeck()
            d.shuffleDeck()
            for y in range(1, 10):
                d.draw()
                self.assertEqual(d.getSize(), (54 * x) - y)

if __name__ == '__main__':
    unittest.main()



