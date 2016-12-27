import sys

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

from autobahn.twisted.websocket import WebSocketServerFactory
from autobahn.twisted.resource import WebSocketResource, WSGIRootResource

from FindingFriendsSocketServerProtocol import FindingFriendsSocketServerProtocol

# Build up our flask app so we can shove it in the server config.
import FlaskConfiguration

# Spin up the server
if __name__ == '__main__':

    log.startLogging(sys.stdout)

    wsFactory = WebSocketServerFactory(u"ws://127.0.0.1:8080")
    wsFactory.protocol = FindingFriendsSocketServerProtocol
    wsResource = WebSocketResource(wsFactory)

    # WSGI resource for flask
    wsgiResource = WSGIResource(reactor, reactor.getThreadPool(), FlaskConfiguration.app)

    rootResource = WSGIRootResource(wsgiResource, {b'ws': wsResource})

    site = Site(rootResource)
    reactor.listenTCP(8080, site)
    reactor.run()
