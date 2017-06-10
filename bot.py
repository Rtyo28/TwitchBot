# BotRubbix Python
"""""
This is a framework for a Bot configured for Twitch

Using this will require some knowledge of Python since there are no commands
to begin with, once the username, channels and oauth has been filled out. The
program will just print out the chat of the channels it connects to.

You can send a message by using the following function,
sendmsg(chan,msg)
--
chan = The channel you want to send the message to, make sure it has a #
in front of it (String)
msg = The message you want to send to the channel, must be a string
--

sendwhis(user,msg)
--
user = The username of the person you want to send the message to (String)
msg = The message you want to send to the user, must be a string
--
"""


# Import necessary libraries.
import datetime
import socket
import select
import re
from TwitchBot.StoreData import points

''' Change the following settings if you wish to run the program '''
channels = ['rtrobot']
username = 'rtrobot'
oauth = 'oauth:9wu990bid5t4uojye2bkfbud4zpzg7'


# Definitions to use while connected
def ping():
    # Respond to the server 'pinging' (Stays connected)
    socks[0].send('PONG :pingis\n'.encode())
    print('PONG: Client > tmi.twitch.tv')


def sendmsg(chan, msg):
    # Send specified message to the channel
    socks[0].send(('PRIVMSG '+chan+' :'+msg+'\n').encode())
    print('[BOT] -> '+chan+': '+msg+'\n')


def sendwhis(user, msg):
    socks[1].send(('PRIVMSG #jtv :/w '+user+' '+msg+'\n').encode())
    print('[BOT] -> '+user+': '+msg+'\n')


def getmsg(msg):
    # GET IMPORTANT MESSAGE
    if re.findall('@(.*).tmi.twitch.tv PRIVMSG (.*) :(.*)'.encode(), msg):
        msg_edit = msg.split(':'.encode(), 2)
        if len(msg_edit) > 2:
            user = msg_edit[1].split('!'.encode(), 1)[0]                  # User
            message = msg_edit[2]                               # Message
            channel = re.findall('PRIVMSG (.*)'.encode(), msg_edit[1])    # Channel

            privmsg = re.findall('@(.*).tmi.twitch.tv PRIVMSG (.*) :(.*)'.encode(), msg)
            ''' CONVERT TO ARRAY '''
            privmsg = [x for xs in privmsg for x in xs]

            datelog = datetime.datetime.now()

            ''' PRINT TO CONSOLE '''
            if len(privmsg) > 0:
                print('[' + str(datelog.hour) + ':' + str(datelog.minute)+':' +
                      str(datelog.second) + '] ' + user.decode() + ' @ ' + channel[0][:-1].decode() + ': ' + message.decode())
                
    if re.findall('@(.*).tmi.twitch.tv WHISPER (.*) :(.*)'.encode(), msg):
        whisper = re.findall('@(.*).tmi.twitch.tv WHISPER (.*) :(.*)'.encode(), msg)
        whisper = [x for xs in whisper for x in xs]

        ''' PRINT TO CONSOLE '''
        if len(whisper) > 0:
            ''' PRINT WHISPER TO CONSOLE '''
            print('*WHISPER* '+whisper[0]+': '+whisper[2])


# Connect to the server using the provided details
socks = [socket.socket(), socket.socket()]
''' Connect to the server using port 6667 & 443 '''
socks[0].connect(('irc.twitch.tv', 6667))
# socks[1].connect(('GROUP_CHAT_IP',GROUP_CHAT_PORT))

'''Authenticate with the server '''
socks[0].send(('PASS '+oauth+'\n').encode())
# socks[1].send('PASS OAUTH_TOKEN\n')
''' Assign the client with the nick '''
socks[0].send(('NICK '+username+'\n').encode())
# socks[1].send('NICK USER\n')

''' Join the specified channel '''
for val in channels:
    socks[0].send(('JOIN #'+val+'\n').encode())
# socks[1].send('JOIN GROUP_CHAT_CHANNEL\n')

''' Send special requests to the server '''
# Used to recieve and send whispers!
# socks[1].send('CAP REQ :twitch.tv/commands\n')

print('Connected to irc.twitch.tv on port 6667')
print('USER: '+username)
print('OAUTH: oauth:'+'*'*30)
print('\n')

p = points()
p.readData('pointsFile.txt')

temp = 0

while True:
    # Save user data
    p.saveData('pointsFile.txt')

    (sread, swrite, sexc) = select.select(socks, socks, [], 120)
    for sock in sread:
        ''' Receive data from the server '''
        msg = sock.recv(2048)
        if msg == '':
            temp += 1
            if temp > 5:
                print('Connection might have been terminated')
    
        ''' Remove any linebreaks from the message '''
        msg = msg.strip(('\n\r').encode())

        ''' DISPLAY MESSAGE IN SHELL '''
        getmsg(msg)
        # print(msg)

        # ANYTHING TO DO WITH CHAT FROM CHANNELS
        ''' GET THE INFO FROM THE SERVER '''
        check = re.findall('@(.*).tmi.twitch.tv PRIVMSG (.*) :(.*)'.encode(), msg)
        if len(check) > 0:
            msg_edit = msg.split(':'.encode(), 2)
            if len(msg_edit) > 2:
                user = msg_edit[1].split('!'.encode(), 1)[0]             # User
                message = msg_edit[2]                                    # Message
                channel = msg_edit[1].split(' '.encode(), 2)[2][:-1]     # Channel

                msg_split = str.split(message.decode())

                if message.decode() == '!join':
                    sendmsg('#rtrobot', p.addUser(user.decode(), 0))

        # ANYTHING TO DO WITH WHISPERS RECIEVED FROM USERS
        check = re.findall('@(.*).tmi.twitch.tv WHISPER (.*) :(.*)'.encode(), msg)
        if len(check) > 0:
            msg_edit = msg.split(':', 2)
            if len(msg) > 2:
                user = msg_edit[1].split('!', 1)[0]             # User
                message = msg_edit[2]                           # Message
                channel = msg_edit[1].split(' ', 2)[2][:-1]     # Channel

                whis_split = str.split(message)

        ''' Respond to server pings '''
        if msg.find('PING :'.encode()) != -1:
            print('PING: tmi.twitch.tv > Client')
            ping()
