import telebot
import os
import const

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token)

time_table = 'Расписание'
location = 'Местоположение'
participants = 'Участники'
organisers = 'Организаторы'

main_menu_markup = telebot.types.ReplyKeyboardMarkup(True)
main_menu_markup.row(time_table, location)
main_menu_markup.row(participants, organisers)

@bot.message_handler(commands=['start'])
def start_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, 'Welcome', reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == time_table)
def time_table_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, const.time_table_text_1, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == location)
def location_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, location, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == participants)
def participants_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, participants, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == organisers)
def organisers_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, organisers, reply_markup=main_menu_markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
