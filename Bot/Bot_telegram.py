import config
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram import MessageHandler
from telegram import Filters


TG_TOKEN = config.TOKEN


# def messege_handler(bot: Bot, update: Update):
#     user


def main():
    bot = Bot(token=TG_TOKEN)
    update = Updater(bot=bot)