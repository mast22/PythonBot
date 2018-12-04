import telebot
import os
import const

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token)

time_table = 'Расписание'
about = 'О мероприятии'
participants = 'Участники'
organisers = 'Организаторы'
register = 'Регистрация'

main_menu_markup = telebot.types.ReplyKeyboardMarkup(True)
main_menu_markup.row(register)
main_menu_markup.row(time_table, about)
main_menu_markup.row(participants, organisers)

@bot.message_handler(commands=['start'])
def start_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, const.greeting, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == register)
def register_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, const.register)
    bot.send_message(cid, const.register_link, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == time_table)
def time_table_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, const.time_table_text_1, parse_mode='HTML')
    bot.send_message(cid, const.time_table_text_2, reply_markup=main_menu_markup, parse_mode='HTML')

@bot.message_handler(func=lambda m: m.text == about)
def about_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, const.about, reply_markup=main_menu_markup)
    bot.send_location(cid, const.loc_lat, const.loc_long)

@bot.message_handler(func=lambda m: m.text == participants)
def participants_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, const.participants, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == organisers)
def organisers_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, const.organisers)
    bot.send_message(cid, const.contacts, reply_markup=main_menu_markup)

@bot.message_handler()
def else_handler(m):
    bot.send_message(m.chat.id, 'Пожалуйста, используйте клавиатуру', reply_markup=main_menu_markup)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        time.sleep(5)