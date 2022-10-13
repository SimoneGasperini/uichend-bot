from datetime import datetime
from telegram.ext.updater import Updater
from telegram.ext.picklepersistence import PicklePersistence
from telegram.ext.commandhandler import CommandHandler
from uichend_bot import utils
from uichend_bot.cmds.hello import hello
from uichend_bot.jobs.meeting_poll import meeting_poll, first_meeting


def run_bot():

    updater = Updater(token=utils.get_token(), use_context=True,
                      persistence=PicklePersistence(utils.get_pickle_db()))
    if "meetings" not in updater.dispatcher.bot_data:
        updater.dispatcher.bot_data["meetings"] = [first_meeting]

    updater.dispatcher.add_handler(CommandHandler("hello", hello))

    interval_poll = utils.get_timedelta_between_meetings()
    poll_date = updater.dispatcher.bot_data["meetings"][-1].date - \
        utils.get_timedelta_poll_meeting()
    poll_time = utils.get_default_time_poll()
    first_poll = datetime.combine(poll_date, poll_time)
    first_poll = utils.convert_datetime_timezone(first_poll)
    updater.job_queue.run_repeating(meeting_poll,
                                    interval=interval_poll,
                                    first=first_poll)

    updater.start_polling()
    updater.idle()
