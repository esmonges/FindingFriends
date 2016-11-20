import sys

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File
from ffrouter import FindingFriendsRouter

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol, \
    listenWS


class EchoServerProtocol(WebSocketServerProtocol):

    def __init__(self, *args):
        super(EchoServerProtocol, self).__init__(*args)
        # TODO: Some way to parameterize the router? Not really needed right now.
        self.router = FindingFriendsRouter()

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))
        self.router.handleAction('Connection', {
                'peer': request.peer
            })

    def onOpen(self):
        print("Ws conn open.")
        self.router.handleAction('Open', {})

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Bin get: {} bytes".format(len(payload)))
            self.router.handleAction('BinaryMessage', {
                    'payload': payload
                })
        else:
            print("Text get: {}".format(payload.decode('utf8')))
            self.router.handleAction('Message', {
                    'payload': payload
                })

        # Echo!
        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason, *args):
        print("Ws conn closed: {}".format(reason))
        self.router.handleAction('Closed', {
                'reason': reason
            })

if __name__ == '__main__':

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = EchoServerProtocol
    listenWS(factory)

    webdir = File(".")
    print(webdir)
    web = Site(webdir)
    print(webdir)
    reactor.listenTCP(8080, web)

    reactor.run()
