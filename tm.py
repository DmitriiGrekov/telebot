import telebot

bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.send_message(message.chat.id,'Ринат вор? --> Да/Нет')
	
@bot.message_handler(content_types=['text'])
def mes_handler(message):
        if message.text=="Да":
                bot.send_message(message.chat.id,'Красава,уважаю')
        elif message.text=='Нет':
                bot.send_message(message.chat.id,'Ты случайно не ринат')
                photo = open('rinat.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)
                
        else:
                bot.send_message(message.chat.id,"Попробуй ответить снова.")

bot.polling()





