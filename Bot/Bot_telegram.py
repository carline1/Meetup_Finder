import telebot
from telebot import apihelper
import config
# import pymysql

bot = telebot.TeleBot(config.TOKEN)

# apihelper.proxy = {
#     'https': 'socks5://188.226.141.127:1080'
# }
apihelper.proxy = {
    'https': 'socks5://geek:socks@t.geekclass.ru:7777'
}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, друг!')


@bot.message_handler(commands=['ха'])
def start_message(message):
    bot.send_message(message.chat.id, 'хаха')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'ээээ':
        bot.send_message(message.chat.id, 'ну да я')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'пока')


if __name__ == '__main__':
    bot.polling(none_stop=True)
