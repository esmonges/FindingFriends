import SocketServer
import re
from base64 import b64encode
from hashlib import sha1

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # print self
        self.data = self.request.recv(1024).strip()
        # self.parseHeaders()
        # handshake = self.generateHandshake(self.data)
        # self.request.sendall(handshake)
        # self.request is the TCP socket connected to the client
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        #TODO: Figure out where to send the handshake, then gen it and send it there

    def parseHeaders(self):
        dataary = self.data.split('\r\n')
        self.headers = {}
        for data in dataary:
            parameter = data.split(':', 1)
            if len(parameter) > 1:
                key, value = parameter
                self.headers[key] = value


    def generateHandshake(self, data):
        handshake = '\
HTTP/1.1 101 Web Socket Protocol Handshake\r\n\
Upgrade: WebSocket\r\n\
Connection: Upgrade\r\n\
\r\n\
'
        # print data
        # From https://developer.mozilla.org/en-US/docs/WebSockets/Writing_WebSocket_servers
        secret = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        return data

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()