
import msvcrt

class UI():

    def __init__(self, username):
        self.username = username
        self.data = ''

    def readInChars(self):
        if not (msvcrt.kbhit()):
            return (False, self.username, self.data)

        while msvcrt.kbhit():
            key = msvcrt.getch();
            char = ''
            try:
                char = key.decode();
            except UnicodeDecodeError:
                continue;

            if(key == b'\r'):
                if(self.data == ''):
                    return(False, self.username, '')
                print('\r\n', end="", flush=True)
                ret = self.data
                self.data = ''
                return(True, self.username, ret)

            elif(key == b'\x08'):
                print('\b \b',end="",flush=True)
                self.data = self.data[:-1]
            else:
                self.data += char

            print('\r[%s]:' % self.username,self.data,end="",flush=True)

        return (False, self.username, '')

    def printMessage(self, username, message):
        print('\r[%s]:' % username, message, end="\r\n", flush=True)
        print('\r[%s]:' % self.username, self.data, end="", flush=True)
