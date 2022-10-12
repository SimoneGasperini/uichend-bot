from datetime import datetime
from telegram.ext.callbackcontext import CallbackContext

from ..meeting import Meeting
from .. import utils

meeting = Meeting(date="14/10/22", time="11:30", place="DIFA")


def poll(context: CallbackContext):
    question = f"UICHEND {meeting}"
    options = ["In presenza", "Da remoto", "Assente"]
    close_date = datetime.combine(meeting.date.date(), meeting.time.time())
    context.bot.send_poll(chat_id=utils.get_chatid(), question=question,
                          options=options, is_anonymous=False, close_date=close_date)
