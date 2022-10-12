from datetime import datetime
from telegram.ext.callbackcontext import CallbackContext

from ..meeting import Meeting
from .. import utils


def poll(context: CallbackContext):
    meeting = Meeting.next(context.bot_data)
    options = ["In presenza", "Da remoto", "Assente"]
    close_date = datetime.combine(meeting.date.date(), meeting.time.time())
    context.bot.send_poll(chat_id=utils.get_chatid(), question=str(meeting),
                          options=options, is_anonymous=False, close_date=close_date)
