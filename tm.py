import telebot
bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")
@bot.message_handler(commands=["start"])
def firest(message):
    key=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    key.row("Да","Нет")
    bot.send_message(message.chat.id,"Руслан гей",reply_markup=key)


if __name__=="__main__":
    bot.polling()
