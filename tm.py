import telebot
from flask import Flask,request
import os
bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")
server = Flask(__name__)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if meesage.text == "a":
        bot.send_message(message.chat.id,"Б")
    elif message.text == 'б':
        bot.send_message(message.chat.id,'А')
    else:
        bot.send_message(message.chat.id,'Ты не умеешь играть в эту игру')
@bot.message_handler(commands=["start"])
def handler_command(message):
    bot.send_message(message.chat.id,"Welcome to my chat")

bot.send_message(264212583,"test")

bot.polling(none_stop=True)


if __name__ == "__main__":
    server.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
