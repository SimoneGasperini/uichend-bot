from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext


def hello(update: Update, _: CallbackContext):
    update.message.reply_text("Hello there!")
