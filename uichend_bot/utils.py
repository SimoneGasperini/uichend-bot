import os
import time

from uichend_bot.config.settings import *


def get_token():
    with open(TOKEN_PATH) as file:
        token = file.read()
    return token


def get_chatid():
    with open(CHATID_PATH) as file:
        chat_id = int(file.read())
    return chat_id


def set_timezone():
    os.environ["TZ"] = TIMEZONE
    if hasattr(time, "tzset"):
        time.tzset()
