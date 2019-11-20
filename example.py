import logging

import telebot
import telebot_calendar
import datetime

from telebot.types import ReplyKeyboardRemove

API_TOKEN = "token"
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# Proxy
# from telebot import apihelper
# ip = "url"
# port = 1080
# apihelper.proxy = {
#     'http': 'socks5h://{}:{}'.format(ip, port),
#     'https': 'socks5h://{}:{}'.format(ip, port)
# }

bot = telebot.TeleBot(API_TOKEN)


# It stores calendar data for each user. Can be to remove in another place
users_calendar_dates = dict()


@bot.message_handler(content_types=["text"])
def check_other_messages(message):
    # Catches a message with the text "start" and sends the calendar
    if message.text == "start":
        now = datetime.datetime.now()
        users_calendar_dates[message.chat.id] = (now.year, now.month)
        bot.send_message(message.chat.id, "Selected date",
                         reply_markup=telebot_calendar.create_calendar(now.year, now.month))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    """
    Обработка inline callback запросов
    :param call:
    :return:
    """

    # Checks the callback inline keyboard
    data = call.data.split(";")
    if len(data) > 1:
        type_selected, date = telebot_calendar.calendar_query_handler(bot, call)
        if type_selected == "DAY":
            users_calendar_dates.pop(call.from_user.id)
            bot.send_message(chat_id=call.from_user.id,
                             text=f"You have chosen {date.strftime('%d.%m.%Y')}",
                             reply_markup=ReplyKeyboardRemove())
            print(f"Day: {date.strftime('%d.%m.%Y')}")
        elif type_selected == "CANCEL":
            bot.send_message(chat_id=call.from_user.id,
                             text="Cancellation",
                             reply_markup=ReplyKeyboardRemove())
            print("Cancellation")


bot.polling(none_stop=True)
