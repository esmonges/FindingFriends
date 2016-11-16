from gamerouter import GameRouter

class FindingFriendsRouter(GameRouter):
    """docstring for FindingFriendsRouter"""
    def __init__(self):
        super(FindingFriendsRouter, self).__init__()

    def handleAction(self, action, actionArgs):
        print(action)
        print(actionArgs)
        return 1