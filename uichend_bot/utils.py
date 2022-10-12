import os
import time
from datetime import datetime, timedelta

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


def get_pickle_db():
    return PICKLEDB_PATH


def get_timedelta():
    return timedelta(days=INTERVAL_BETWEEN_MEETINGS)


def get_default_time():
    return datetime.strptime(DEFAULT_TIME_MEETING, "%H:%M")


def get_default_place():
    return DEFAULT_PLACE_MEETING
