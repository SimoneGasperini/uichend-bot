from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler

from uichend_bot import utils
from uichend_bot.commands.hello_cmd import hello
from uichend_bot.jobs.poll_job import poll


def run_bot():

    utils.set_timezone()
    token = utils.get_token()

    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("hello", hello))
    updater.job_queue.run_once(poll, when=20)

    updater.start_polling()
    updater.idle()
