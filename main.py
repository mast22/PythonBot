import telebot
import os
import const

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token)

time_table = 'Расписание'
about = 'О мероприятии'
participants = 'Участники'
organisers = 'Организаторы'

main_menu_markup = telebot.types.ReplyKeyboardMarkup(True)
main_menu_markup.row(time_table, about)
main_menu_markup.row(participants, organisers)

@bot.message_handler(commands=['start'])
def start_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, 'Welcome', reply_markup=main_menu_markup)

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
    bot.send_message(cid, participants, reply_markup=main_menu_markup)

@bot.message_handler(func=lambda m: m.text == organisers)
def organisers_handler(m):
    cid = str(m.chat.id)
    bot.send_message(cid, 'Руководитель')
    bot.send_contact(cid, '+79093081080', 'Ксения', 'Башлай')
    bot.send_message(cid, 'Заместитель руководителя')
    bot.send_contact(cid, '+79534067497', 'Хафизова', 'Зарина')
    bot.send_message(cid, 'Разработчик бота')
    bot.send_contact(cid, '+79991568802', 'Николай')

if __name__ == '__main__':
    bot.polling(none_stop=True)
