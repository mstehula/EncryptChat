
import msvcrt

class UI():

    def __init__(self, username):
        self.username = username
        self.data = ''
        self.retdata = ''

    def readInChars(self):
        if not (msvcrt.kbhit()):
            return False

        while msvcrt.kbhit():
            key = msvcrt.getch();
            char = ''
            try:
                char = key.decode();
            except UnicodeDecodeError:
                continue;

            if(key == b'\r'):
                if(self.data == ''):
                    return False
                print('\r\n', end="", flush=True)
                self.retdata = self.data
                self.data = ''
                return True

            elif(key == b'\x08'):
                print('\b \b',end="",flush=True)
                self.data = self.data[:-1]
            else:
                self.data += char

            print('\r[%s]:' % self.username,self.data,end="",flush=True)

        return False

    def getMessageToSend(self):
        return (self.username, self.retdata)

    def printMessage(self, args):
        username = args[0]
        message = args[1]
        print('\r[%s]:' % username, message, end="\r\n", flush=True)
        print('\r[%s]:' % self.username, self.data, end="", flush=True)
