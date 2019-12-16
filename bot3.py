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
import telegram.update




def getLocation(bot, update, user_data):
    updater = Updater(TELEGRAM_API_KEY)
    msg = update.message
    user_data['msg'] = msg
    user_data['id'] = update.update_id
    print(update.message.reply_text('lat: {}, lng: {}'.format(msg.location.latitude, msg.location.longitude)))


def showCoordinates(bot, update, user_data):
    # I need to update location here but I don't know
    newLoc = user_data['msg']
    update.message.reply_text('lat: {}, lng: {}'.format(
        newLoc.location.latitude, newLoc.location.longitude))

dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.location, getLocation, pass_user_data=True))
dp.add_handler(CommandHandler('track', showCoordinates, pass_user_data=True))


# ------------ END of Commands Creation Block --------------


if __name__ == '__main__':
    updater.start_polling()
    # updater.idle()
