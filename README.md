# Twitch-Chat-Bot-V2
A Python framework for a Twitch Chat bot

Using this will require some knowledge of Python since there are no commands to begin with, once the **username**, **channels** and **oauth** has been filled out. The program will just print out the chat of the channels it connects to.


## Installation
You will need Python to use this, I myself use Python 2.7.9. You can download it [here](https://www.python.org/downloads/release/python-279/). Once it's installed you can download the ZIP or copy/paste the contents of `bot.py`. It's quite easy

## Use
##### Sending a message...
```python
def sendmsg(chan,msg):
    ''' Send specified message to the channel '''
    socks[0].send('PRIVMSG '+chan+' :'+msg+'\n')
    print('[BOT] -> '+chan+': '+msg+'\n')
```
```
chan = The channel you want to send the message to, make sure it has a '#' in front of it (String)
msg = The message you want to send to the channel, must be a string
```

##### Sending a whisper...
```python
def sendwhis(user,msg):
    socks[1].send('PRIVMSG #jtv :/w '+user+' '+msg+'\n')
    print('[BOT] -> '+user+': '+msg+'\n')
```
```
user = The username of the person you want to send the message to (String)
msg = The message you want to send to the user, must be a string
```
Whispers will need some extra paramters to be populated, these are currently commented out under the connection to `irc.twitch.tv`
```python
socks[1].connect(('GROUP_CHAT_IP',GROUP_CHAT_PORT))
socks[1].send('PASS OAUTH_TOKEN\n') #Same OAuth for your Username
socks[1].send('NICK USER\n') #Same Username
socks[1].send('JOIN GROUP_CHAT_CHANNEL\n')
socks[1].send('CAP REQ :twitch.tv/commands\n')
```
You will need to be apart of a Group Chat and need to find the IP and Port of the server you're connected to, a useful guide for this can be found [here](http://blog.bashtech.net/twitch-group-chat-irc/)
**The last line allows us to send whispers to other people**

#### Doing stuff with chat...
```python
# ANYTHING TO DO WITH CHAT FROM CHANNELS
''' GET THE INFO FROM THE SERVER '''
check = re.findall('@(.*).tmi.twitch.tv PRIVMSG (.*) :(.*)',msg)
if(len(check) > 0):
  msg_edit = msg.split(':',2)
  if(len(msg_edit) > 2):
    user = msg_edit[1].split('!',1)[0] # User
    message = msg_edit[2] # Message
    channel = msg_edit[1].split(' ',2)[2][:-1] # Channel
    
    msg_split = str.split(message)
```
**User**, **Message** and **Channel** are defined for every message recieved. Creating commands are done here right below the above code block, example:
```python
''' Respond to command '''
if(msg_split[0] == '!Hi'):
  sendmsg(channel,'Hi '+user+', how are you doing today?')
```

#### Doing stuff with whispers...
```python
# ANYTHING TO DO WITH WHISPERS RECIEVED FROM USERS
check = re.findall('@(.*).tmi.twitch.tv WHISPER (.*) :(.*)',msg)
if(len(check) > 0):
  msg_edit = msg.split(':',2)
  if(len(msg) > 2):
    user = msg_edit[1].split('!',1)[0] # User
    message = msg_edit[2] # Message
    channel = msg_edit[1].split(' ',2)[2][:-1] # Channel

    whis_split = str.split(message)
```
Once again, **User**, **Message** and **Channel** are defined for every whisper recieved, much like when you recieve a chat message.
The only difference in creating commands between whispers and normal chat messages is how the command is sent. Whispers use...
```python
sendwhis(user,'This is an example message')
```
