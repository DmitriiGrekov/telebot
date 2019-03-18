import telebot

bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
@bot.message_handler(content_types=["text"])
def handler_welkome(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id,"And i hi you")

bot.polling()





