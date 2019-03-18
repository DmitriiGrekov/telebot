import telebot

bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")



@bot.message_handler(content_types=["text"])
def handler_welkome(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id,"And i hi you")

markup = telebot.types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')
bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
bot.polling()





