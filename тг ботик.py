import telebot
from telebot import types
#Создал бота для проверки https://t.me/Fackamakaka_bot
bot = telebot.TeleBot('7786664713:AAGTsLgHKhf7eaeBV8Ymd2caY3PWxQlhoXc')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет ученик Гимназии!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Показать презентации')
        btn2 = types.KeyboardButton('Помощь!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) 


    elif message.text == 'Показать презентации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn3 = types.KeyboardButton ('7 Класс')
        btn4 = types.KeyboardButton ('8 Класс')
        btn5 = types.KeyboardButton ('9 Класс')
        btn6 = types.KeyboardButton ('10 Класс')
        btn7 = types.KeyboardButton ('11 Класс')
        btn8 = types.KeyboardButton ('Назад')
        markup.add(btn3,btn4,btn5,btn6,btn7,btn8)
        bot.send_message(message.from_user.id, 'В каком вы классе?', reply_markup=markup) 
        
    elif message.text == 'Помощь':
        bot.send_message(message.from_user.id, 'Вы всегда можете обратиться в нашу тех.поддержку, которая всегда будет рада вам помочь! https://t.me/fuckinglazydream или @fuckinglazydream', reply_markup=markup)


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть