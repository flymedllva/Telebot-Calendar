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
See the example in the file `example.py`

## Languages
To set the language, add its instance to the calendar class

```python
from telebot_calendar import Calendar, RUSSIAN_LANGUAGE

calendar = Calendar(language=RUSSIAN_LANGUAGE)
```
You can also create your own language class. If you will do it for other languages, we will be grateful to PR

## Demo
![](https://github.com/FlymeDllVa/telebot-calendar/blob/master/demo.gif)