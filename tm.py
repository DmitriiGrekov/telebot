import telebot
bot=telebot.Telebot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")
@bot.message_handler(commands=["start"])
def firest(message):
    key=telebot.types.ReplyKeyboardMarkup(True,False)
    key.row("Да","Нет")
    bot.send_message(message.chat.id,"Руслан гей",reply_markup=key)


if __name__=="__main__":
    bot.polling(none_stop=True,interval=0,timeout=20)
