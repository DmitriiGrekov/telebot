import telebot
import requests
bot = telebot.TeleBot("797549243:AAE-nR3eITIaO-OberdmXRi2Poywlpj3_0w")
lang1=""
lang2=''


@bot.message_handler(commands=["start"])
def firest(message):
    key=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    key.row("Переводчик")
    send=bot.send_message(message.chat.id,"Выберите функцию",reply_markup=key)
    bot.register_next_step_handler(send,translated_menu_1)
def translated_menu_1(message):
    if message.text == "Переводчик":
        key=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
        key.row("Рус","Англ","Франц")
        send=bot.send_message(message.chat.id,"Выберите с какой язык переводить",reply_markup=key)
        bot.register_next_step_handler(send,translated_menu_2)
def translated_menu_2(message):
    global lang1
    if message.text == 'Рус':
        lang1='ru'
        key=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
        key.row("Рус","Англ","Франц")
        
        send=bot.send_message(message.chat.id,"Выберите на какой язык переводить",reply_markup=key)
        bot.register_next_step_handler(send,translated_menu_3)
    
    
    elif message.text == 'Англ':
        lang1='en'
        key=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
        key.row("Рус","Англ","Франц")
        
        send=bot.send_message(message.chat.id,"Выберите на какой язык переводить",reply_markup=key)
        bot.register_next_step_handler(send,translated_menu_3)
    
    elif message.text == 'Франц':
        lang1='fr'
        key=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
        key.row("Рус","Англ","Франц")
        
        send=bot.send_message(message.chat.id,"Выберите на какой язык переводить",reply_markup=key)
        bot.register_next_step_handler(send,translated_menu_3)
    
def translated_menu_3(message):
    global lang2
    bot.send_message(message.chat.id,lang1)
    if message.text == 'Рус':
        lang2='ru'
        
        send=bot.send_message(message.chat.id,"Введите фразу")
        bot.register_next_step_handler(send,translated)
    
    
    elif message.text == 'Англ':
        lang2='en'
        
        send=bot.send_message(message.chat.id,"Введите фразу")
        bot.register_next_step_handler(send,translated)
    
    elif message.text == 'Франц':
        lang2='fr'
        send=bot.send_message(message.chat.id,"Введите фразу")
        bot.register_next_step_handler(send,translated)

def translated(message):
    global lang1
    global lang2
    bot.send_message(message.chat.id,lang1)
    
    
    
        
        
        
    

        

        


if __name__=="__main__":
    bot.polling()
