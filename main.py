import telebot
from tinydb import TinyDB, Query
import os

token = os.environ.get('TOKEN')

time_table = 'Расписание'
location = 'Местоположение'
participants = 'Участники'
organisers = 'Организаторы'

main_menu_markup = telebot.types.ReplyKeyboardMarkup(True)
main_menu_markup.row(time_table, location)
main_menu_markup.row(participants, organisers)

@bot.message_handler(func=lambda m: m.text == time_table)
def time_table_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, time_table)

@bot.message_handler(func=lambda m: m.text == location)
def location_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, location)

@bot.message_handler(func=lambda m: m.text == participants)
def participants_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, participants)

@bot.message_handler(func=lambda m: m.text == organisers)
def organisers_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, organisers)

if __name__ == '__main__':
    bot.polling(none_stop=True)
