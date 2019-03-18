import telebot

bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Руслан гей? -> Да/Нет")
@bot.message_handler(content_types=['text'])
def mes_handler(message):
        if message.text=="Да":
                bot.send_message(message.chat.id,'Красава,уважаю')
        elif message.text=='Нет':
                bot.send_message(message.chat.id,'Рустик,ты что-ли')
        else:
                bot.send_message(message.chat.id,'Ты настолько тупой что даже не можешь правильно написать.Это точно Руслан' )
        

@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    now = datetime.datetime.now() #Текущая дата
    chat_id = message.chat.id
    date = (now.year,now.month)
    current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
    markup = create_calendar(now.year,now.month)
    bot.send_message(message.chat.id, "Пожалйста, выберите дату", reply_markup=markup)

bot.polling()





