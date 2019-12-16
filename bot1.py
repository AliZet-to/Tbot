# import telebot
import config
import random
from telegram.ext import *
import requests
import re
import sys
import json
import pprint
import time
from telegram import Update, Location
# import telegram.update

URL = "https://api.telegram.org/bot822728951:AAHz7aNQ1C1R6_2j5Pjh4SX9UKqwfu3QpKQ/setWebhook?url=https://https://alizetto.pythonanywhere.com/:8443/822728951:AAHz7aNQ1C1R6_2j5Pjh4SX9UKqwfu3QpKQ/"




# updater = Updater(token=config.TOKEN, use_context=True)
# dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def stop(update, context):
    print('Good-bye')
    sys.exit()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def location(update, context):
    message = None
    # print("Start Point: " + message['location'])
    if update.edited_message:
        message = update.edited_message
    else:
        message = update.message
        # print(update.message['location'] + "ELSE")
    # current_pos = (message.location.latitude, message.location.longitude)
    # print(current_pos + "CURRENT POS")
    print(message['location'] + "GEN")

# def location(update, context):
#     print(update.message.location)


# def showMyLoc(update, context):
#     # context.bot.send_message(chat_id=update.effective_chat.id, text="My Location is ")
#     # pprint.pprint(json.dumps(update.message))
#     # print(update.message)
#     print(update.message['location'])
#     # URL = 'https://api.telegram.org/bot' + config.TOKEN + '/'
#     # print(update.message['location'])
#     # url = URL + 'editMessageLiveLocation'
#     # while True:
#     #     r = requests.post(url)
#     #     print(r.json())
#     #     time.sleep(2)



updater = Updater(token=config.TOKEN, use_context=True)
dispatcher = updater.dispatcher


# ----------- BOT Commands Creation ----------------
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)


echo_handler = MessageHandler(Filters.text, echo) ### Returns ANY input by user TEXT
dispatcher.add_handler(echo_handler)


# location_handler = MessageHandler(Filters.location, showMyLoc) ### Returns ANY input by user TEXT
# dispatcher.add_handler(location_handler)


# location_handler = MessageHandler(Filters.location, location, edited_updates=None)
location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)

# ------------ END of Commands Creation Block --------------


if __name__ == '__main__':
    URL.run()
    # updater.start_polling()