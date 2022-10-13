from datetime import datetime, timedelta
from pytz import timezone
from uichend_bot.config.settings import *


def get_token():
    with open(TOKEN_PATH) as file:
        token = file.read()
    return token


def get_chatid():
    with open(CHATID_PATH) as file:
        chat_id = int(file.read())
    return chat_id


def get_pickle_db():
    return PICKLEDB_PATH


def convert_datetime_timezone(dt, from_tz=None, to_tz=None):
    if from_tz is None:
        from_tz = LOCAL_TIMEZONE
    if to_tz is None:
        to_tz = SERVER_TIMEZONE
    old_dt = timezone(from_tz).localize(dt)
    new_dt = old_dt.astimezone(timezone(to_tz))
    new_dt = new_dt.replace(tzinfo=None)
    return new_dt


def get_timedelta_poll_meeting():
    return timedelta(days=TIMEDELTA_POLL_MEETING)


def get_default_time_poll():
    return datetime.strptime(DEFAULT_TIME_POLL, "%H:%M").time()


def get_timedelta_between_meetings():
    return timedelta(days=TIMEDELTA_BETWEEN_MEETINGS)


def get_default_time_meeting():
    return datetime.strptime(DEFAULT_TIME_MEETING, "%H:%M").time()


def get_default_place_meeting():
    return DEFAULT_PLACE_MEETING
