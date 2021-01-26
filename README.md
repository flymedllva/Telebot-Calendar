# Inline calendar for Telebot

<p align="left">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

Simple calendar for [Telebot](https://github.com/eternnoir/pyTelegramBotAPI).

## Installation
[PYPI](https://pypi.org/project/telebot-calendar/)
```shell script
pip install telebot-calendar
```

## Description
The file **telebot_calendar.py** used to create, modify, and retrieve user data from an [inline keyboard](https://core.telegram.org/bots/2-0-intro) calendar created by the user.

## Usage
To use the telebot_calendar you need to have [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) installed first. Working example.py
```python
@bot.message_handler(commands=["start"])
def check_other_messages(message):
    """
    Catches a message with the command "start" and sends the calendar

    :param message:
    :return:
    """

    now = datetime.datetime.now()  # Get the current date
    bot.send_message(
        message.chat.id,
        "Selected date",
        reply_markup=telebot_calendar.create_calendar(
            name=calendar_1.prefix, # Specify the NAME of your calendar
            year=now.year,
            month=now.month,
            language=0, # language: 0 for English, 1 for Russian
        ),
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith(calendar_1.prefix))
def callback_inline(call: CallbackQuery):
    """
    Обработка inline callback запросов
    :param call:
    :return:
    """

    # At this point, we are sure that this calendar is ours. So we cut the line by the separator of our calendar
    name, action, year, month, day = call.data.split(calendar_1.sep)
    # Processing the calendar. Get either the date or None if the buttons are of a different type
    date = telebot_calendar.calendar_query_handler(
        bot=bot, call=call, name=name, action=action, year=year, month=month, day=day
    )
    # There are additional steps. Let's say if the date DAY is selected, you can execute your code. I sent a message.
    if action == "DAY":
        bot.send_message(
            chat_id=call.from_user.id,
            text=f"You have chosen {date.strftime('%d.%m.%Y')}",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{calendar_1}: Day: {date.strftime('%d.%m.%Y')}")
    elif action == "CANCEL":
        bot.send_message(
            chat_id=call.from_user.id,
            text="Cancellation",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{calendar_1}: Cancellation")
```

## Demo
![](https://github.com/FlymeDllVa/telebot-calendar/blob/master/demo.gif)