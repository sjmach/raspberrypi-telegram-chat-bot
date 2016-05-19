import sys
import time
import telepot
import urllib2
import json

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command
    if command == '/status':
        bot.sendMessage(chat_id, 'Checking the build status for ya!')
        response =json.load(urllib2.urlopen('http://URL:8080/job/BUILDNAME/api/json?pretty=true'))
        buildnumber = response["builds"][0]["number"]
        statusurl = "http://URL:8080/job/BUILDNAME/%s/api/json?pretty=true" % buildnumber
        statusresponse = json.load(urllib2.urlopen(statusurl))
        status = statusresponse['building']
        if status is True:
            bot.sendMessage(chat_id, "The Build is in progress")
        else:
            bot.sendMessage(chat_id, statusresponse["result"])
    elif command == '/test':
        bot.sendMessage(chat_id, 'Telling Jenkins to run a Test')
        urllib2.urlopen('http://URL:8080/job/BUILDNAME/build')
        bot.sendMessage(chat_id, "The Build is in progress and check back later")

# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
