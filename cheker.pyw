import os
import sys
import telebot
from telebot import types
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

chat_id=config["telegram"]["chat_id"] #chat_id=ВАШ ЧАТ АЙДИ
token=config["telegram"]["token"] #token=ТОКЕН ВАШЕГО БОТА
bot = telebot.TeleBot(token);

while True:
    try:
        os.rename('main.pyw', 'checked.pyw')
        os.rename('checked.pyw', 'main.pyw')
    except OSError:
        print('+')
    else:
        print("Detected")
        bot.send_message(chat_id, "> " + config["local"]["prefix"] + " " + config["local"]["name"] + ":выключено")
        break
