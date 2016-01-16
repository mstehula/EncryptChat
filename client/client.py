#!usr/bin/python

from inet import CommHandler
from ui import UI

import os
import sys


print('Welcome to the first iteration of secure chats')

username = str(input('Please enter a username to use: '))
ch = CommHandler()
ui = UI(username)

print('Setup complete. Anything you type will be directly transmitted to the remote client')
print("\r[%s]: " % username,end="")

while True:
    if(ch.checkForMessage()):
        ui.printMessage(ch.recvMessage())

    if(ui.readInChars()):
        ch.sendMessage(ui.getMessageToSend())
