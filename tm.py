import telebot
bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")
@bot.message_handler(commands=["start"])
def firest(message):
    key=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    key.row("Да","Нет")
    bot.send_message(message.chat.id,"Руслан гей",reply_markup=key)
@bot.message_handler(content_types=["text"])
def send_message(message):
    if message.text == "Да":
        bot.send_message(message.chat.id,'Красава,Уважаю!')
        photo = open('yes.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Руслан гей")
    elif message.text == 'Нет':
        bot.send_message(message.chat.id,'Рустик,ты что-ли!')
        photo = open('no.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Руслан гей")
    
        


if __name__=="__main__":
    bot.polling()
