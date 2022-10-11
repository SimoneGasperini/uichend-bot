from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from uichend_bot.commands.hello_cmd import hello
from uichend_bot.commands.poll_cmd import poll


def run_bot():
    with open("../__token__.txt") as file:
        token = file.read()
    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("hello", hello))
    updater.dispatcher.add_handler(CommandHandler("poll", poll))
    updater.start_polling()
