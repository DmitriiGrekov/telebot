import telebot

bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Руслан гей? -> Да/Нет")
@bot.message_handler(content_type=['text'])
def mes_handler(message):
        if message.text=="Да":
                bot.send_message(message.chat.id,'Красава,уважаю')
        elif message.text=='Нет':
                bot.send_message(message.chat.id,'Рустик,ты что-ли')
        else:
                bot.send_message(message.chat.id,'Ты настолько тупой что даже не можешь правильно написать.Это точно Руслан' )
        



bot.polling()





