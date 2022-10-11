import datetime
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from datetime import datetime
from ..meeting import Meeting


def poll(update: Update, context: CallbackContext):
    meeting = Meeting(date="14/10/22", time="11:30", place="DIFA")
    question = f"UICHEND {meeting}"
    options = ["In presenza", "Da remoto", "Assente"]
    close_date = datetime.combine(meeting.date.date(), meeting.time.time())
    context.bot.send_poll(update.message.chat_id, question,
                          options, is_anonymous=False, close_date=close_date)
