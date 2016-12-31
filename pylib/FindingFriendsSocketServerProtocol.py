from autobahn.twisted import WebSocketServerProtocol
from FlaskConfiguration import login_required
from flask import *

class FindingFriendsSocketServerProtocol(WebSocketServerProtocol):

    def __init__(self, *args):
        super(FindingFriendsSocketServerProtocol, self).__init__(*args)
        # TODO: Some way to parameterize the router? Not really needed right now.
        #self.router = FindingFriendsRouter()

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))
        # self.router.handleAction('Connection', {
        #         'peer': request.peer
        #     })

    def onOpen(self):
        print("Ws conn open.")
        # self.router.handleAction('Open', {})

    @login_required
    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Bin get: {} bytes".format(len(payload)))
            # self.router.handleAction('BinaryMessage', {
            #         'payload': payload
            #     })
        else:
            print("Text get: {}".format(payload.decode('utf8')))
            # self.router.handleAction('Message', {
            #         'payload': payload
            #     })

        # Echo!
        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason, *args):
        print("Ws conn closed: {}".format(reason))
        # self.router.handleAction('Closed', {
        #         'reason': reason
        #     })