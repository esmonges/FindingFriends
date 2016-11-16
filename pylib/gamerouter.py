class GameRouter(object):
    """docstring for GameRouter"""
    def __init__(self):
        super(GameRouter, self).__init__()

    def handleAction(self, action, actionArgs):
        raise NotImplementedError("unimplemented")