from datetime import datetime
from telegram.ext.callbackcontext import CallbackContext
from uichend_bot import utils


class Meeting:

    def __init__(self, date, time, place):
        self.date = date
        self.time = time
        self.place = place

    @classmethod
    def next(cls, bot_data):
        meeting_date = bot_data["meetings"][-1].date
        if meeting_date < datetime.today().date():
            next_meeting_date = meeting_date + utils.get_timedelta_between_meetings()
        else:
            next_meeting_date = meeting_date
        next_meeting_time = utils.get_default_time_meeting()
        next_meeting_place = utils.get_default_place_meeting()
        next_meeting = cls(date=next_meeting_date,
                           time=next_meeting_time,
                           place=next_meeting_place)
        bot_data["meetings"].append(next_meeting)
        return next_meeting

    @property
    def datetime(self):
        return datetime.combine(self.date, self.time)

    def to_string(self):
        weekday = self.date.strftime("%A")
        date_str = self.date.strftime("%d/%m/%y")
        time_str = self.time.strftime("%H:%M")
        return f"UICHEND meeting\n{weekday} {date_str} - {time_str}\n{self.place}"


class Poll:

    def __init__(self, question, options):
        self.question = question
        self.options = options

    @classmethod
    def for_meeting(cls, meeting):
        question = meeting.to_string()
        options = options = ["In presenza", "Da remoto", "Assente"]
        return cls(question=question, options=options)


def meeting_poll(context: CallbackContext):
    meeting = Meeting.next(bot_data=context.bot_data)
    poll = Poll.for_meeting(meeting=meeting)
    context.bot.send_poll(chat_id=utils.get_chatid(), is_anonymous=False,
                          question=poll.question, options=poll.options, close_date=meeting.datetime)
