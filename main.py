import telebot
import os
from const import *
from tinydb import TinyDB, Query
import datetime
import time
import json

db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, GREETING, reply_markup=main_menu_markup)
    User = Query()
    t = datetime.datetime.now()
    """
    Add new user to tinyDB
    """
    if not db.get(User.cid == cid):
        db.insert(
            {
                'cid': cid,
                'date': '{} {}:{}'.format(t.day, t.hour, t.minute),
                'username': m.from_user.username or 'without username',
                'first_name': m.from_user.first_name
            }
        ) 

"""
Handlers for user messages
"""

@bot.message_handler(func=lambda m: m.text == REGISTER)
def register_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, REGISTER)
    bot.send_message(cid, REGISTER_LINK, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == TIME_TABLE)
def time_table_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, TIME_TABLE_TEXT_1, parse_mode='HTML')
    bot.send_message(cid, TIME_TABLE_TEXT_2, reply_markup=main_menu_markup, parse_mode='HTML')

@bot.message_handler(func=lambda m: m.text == ABOUT)
def about_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, ABOUT, reply_markup=main_menu_markup)
    bot.send_location(cid, LOC_LAT, LOC_LONG)

@bot.message_handler(func=lambda m: m.text == PARTICIPANTS)
def participants_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, PARTICIPANTS, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == ORGANISERS)
def organisers_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, ORGANISERS)
    bot.send_message(cid, CONTACTS, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == 'get_logs')
def logs_handler(m):
    """
    Request users info from db
    """
    cid = str(m.chat.id)
    users = db.all()
    message = ''
    for i in users:
        m = i['cid'] + '\n' + i['first_name'] + '\n' + i['username'] + '\n' + i['date'] + '\n' + '-----------------' + '\n'
        message += m
    bot.send_message(cid, message)


@bot.message_handler()
def else_handler(m):
    bot.send_message(m.chat.id, 'Пожалуйста, используйте клавиатуру', reply_markup=main_menu_markup)


bot.polling(none_stop=True)
