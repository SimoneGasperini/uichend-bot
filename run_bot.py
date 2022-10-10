from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler

with open("../__token__.txt") as file:
    token = file.read()

updater = Updater(token=token, use_context=True)


def hello(update: Update, context: CallbackContext):
    update.message.reply_text("Hello there!")


updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
