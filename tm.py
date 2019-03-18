import telebot
bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id,"Test")

bot.send_message(264212583,"test")

bot.polling(none_stop=True, interval=0)
