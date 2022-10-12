from datetime import datetime
from . import utils


class Meeting:

    def __init__(self, date, time, place):
        self.date = date
        self.time = time
        self.place = place

    def __repr__(self):
        weekday = self.date.strftime("%A")
        date_str = self.date.strftime("%d/%m/%y")
        time_str = self.time.strftime("%H:%M")
        return f"UICHEND meeting\n{weekday} {date_str} - {time_str}\n{self.place}"

    @classmethod
    def next(cls, bot_data):
        if "meetings" not in bot_data:
            bot_data["meetings"] = []
            append_first_meeting(bot_data)
        date_next = bot_data["meetings"][-1].date + utils.get_timedelta()
        time_next = utils.get_default_time()
        place_next = utils.get_default_place()
        next_meeting = cls(date=date_next, time=time_next, place=place_next)
        bot_data["meetings"].append(next_meeting)
        return next_meeting


def append_first_meeting(bot_data):
    first_meeting = Meeting(date=datetime.strptime("07/10/22", "%d/%m/%y"),
                            time=datetime.strptime("11:30", "%H:%M"),
                            place="DIFA - Aula riunioni (1° piano)")
    bot_data["meetings"].append(first_meeting)
