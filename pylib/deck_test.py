import unittest
from deck import Deck

class Deck_Test(unittest.TestCase):
    def setUp(self):
        return

    def test_construct(self):
        with self.assertRaises(AssertionError):
           Deck(0)
        for x in xrange(1,10):
            Deck(x)

if __name__ == '__main__':
    unittest.main()



