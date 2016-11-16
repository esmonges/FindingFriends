import unittest
from ffrouter import FindingFriendsRouter

class FindingFriendsRouter_Test(unittest.TestCase):
    def setUp(self):
        self.ffrouter = FindingFriendsRouter()

    def test_handleAction(self):
        self.assertTrue(self.ffrouter.handleAction('test', {}))

if __name__ == '__main__':
    unittest.main()