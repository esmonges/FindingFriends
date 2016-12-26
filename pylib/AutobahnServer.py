import sys
import uuid

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File
from twisted.web.wsgi import WSGIResource

from flask import Flask, render_template

from ffrouter import FindingFriendsRouter

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol, \
    listenWS
from autobahn.twisted.resource import WebSocketResource, WSGIRootResource


class FindingFriendsServerProtocol(WebSocketServerProtocol):

    def __init__(self, *args):
        super(FindingFriendsServerProtocol, self).__init__(*args)
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

# WSGI app, via flask
app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

@app.route('/')
def page_home():
    return render_template('testautobahn.html')

if __name__ == '__main__':

    log.startLogging(sys.stdout)

    wsFactory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    wsFactory.protocol = FindingFriendsServerProtocol
    wsResource = WebSocketResource(wsFactory)

    # WSGI resource for flask
    wsgiResource = WSGIResource(reactor, reactor.getThreadPool(), app)

    rootResource = WSGIRootResource(wsgiResource, {b'ws': wsResource})

    site = Site(rootResource)
    reactor.listenTCP(8080, site)
    reactor.run()
