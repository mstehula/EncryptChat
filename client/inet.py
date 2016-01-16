import socket
import struct

class CommunicationHandler():
    def sendMessage(socket, username, message):
        length = len(message)

        remote.send(struct.pack("64s", username.encode()))
        remote.send(struct.pack("I", length))
        remote.send(struct.pack('%ds' % length, message.encode()))

    #Receive a Message on a given Socket. This is strictly the
    #message in the scope of this program, consisting of 64B name, 4B datalength,
    #data (up to) 2^32
    def recvMessage(socket):
        username = struct.unpack('64s', socket.recv(64))[0].replace(b'\0',b'')
        size = struct.unpack('I', socket.recv(4))[0]
        data = struct.unpack('%ds' % size, socket.recv(size))[0]

        return (username, data)
