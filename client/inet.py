import select
import socket
import struct

class CommHandler():

    #Setup for the listener server socket and client socket. Also starts the
    #server, but does not start accepting. Currently listener is locked at port
    #5555
    def __init__(self, localport, hostname, hostport):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listener.bind('localhost', localport)
        self.listener.listen(5)

        self.remoteloc = (hostname, hostport)
        self.client = socket.socket()

    #Sends message to the given socket as the given username.
    def sendMessage(self, args):
        username = args[0]
        message = args[1]

        self.client.connect(self.remoteloc)

        length = len(message)

        self.client.send(struct.pack("64s", username.encode()))
        self.client.send(struct.pack("I", length))
        self.client.send(struct.pack('%ds' % length, message.encode()))

        self.client.close()
        self.client = socket.socket()

    #Check to see if there is a message available for the listener to recv
    def checkForMessage(self):
        readable = select.select([self.listener],[],[],0)[0]
        return len(readable) != 0

    #Receive a Message on a given Socket. This is strictly the
    #message in the scope of this program, consisting of 64B name, 4B datalength,
    #data (up to) 2^32
    def recvMessage(self):
        recvsocket = self.listener.accept()[0]
        username = struct.unpack('64s', recvsocket.recv(64))[0].replace(b'\0',b'').decode()
        size = struct.unpack('I', recvsocket.recv(4))[0]
        data = struct.unpack('%ds' % size, recvsocket.recv(size))[0].decode()
        recvsocket.close()

        return (username, data)
