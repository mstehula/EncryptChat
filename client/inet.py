import select
import socket
import struct

class CommunicationHandler():

    client, listener = None

    #Setup for the listener server socket and client socket. Also starts the
    #server, but does not start accepting
    def __init__:
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        host = listener.gethostname()
        port = 5555
        listener.bind((host, port))
        listener.listen(5)

        client = socket.socket()

    #Sends message to the given socket as the given username.
    def sendMessage(username, message):
        length = len(message)

        remote.send(struct.pack("64s", username.encode()))
        remote.send(struct.pack("I", length))
        remote.send(struct.pack('%ds' % length, message.encode()))

    #Check to see if there is a message available for the listener to recv
    def checkForMessage():
        readable = select.select([listener],[],[],0)
        return len(readable) != 0

    #Receive a Message on a given Socket. This is strictly the
    #message in the scope of this program, consisting of 64B name, 4B datalength,
    #data (up to) 2^32
    def recvMessage():
        recvsocket = listener.accept()[0]
        username = struct.unpack('64s', recvsocket.recv(64))[0].replace(b'\0',b'')
        size = struct.unpack('I', recvsocket.recv(4))[0]
        data = struct.unpack('%ds' % size, recvsocket.recv(size))[0]
        recvsocket.close()

        return (username, data)
