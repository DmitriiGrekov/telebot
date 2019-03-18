import telebot
from flask import Flask,request
import os
bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")
server = Flask(__name__)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id,"Test")

bot.send_message(264212583,"test")

bot.polling(none_stop=True)


if __name__ == "__main__":
    server.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
