import unittest
from gamerouter import GameRouter

class GameRouter_Test(unittest.TestCase):
    def setUp(self):
        self.gameRouter = GameRouter()

    def test_handleAction(self):
        with self.assertRaises(NotImplementedError):
            self.gameRouter.handleAction('action', {})

if __name__ == '__main__':
    unittest.main()