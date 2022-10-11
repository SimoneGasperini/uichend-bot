from datetime import datetime


class Meeting:

    def __init__(self, date, time, place):
        self.date = datetime.strptime(date, "%d/%m/%y")
        self.time = datetime.strptime(time, "%H:%M")
        self.place = place

    def __repr__(self):
        weekday = self.date.strftime("%A")
        date_str = self.date.strftime("%d/%m/%y")
        time_str = self.time.strftime("%H:%M")
        return f"meeting\n{weekday} {date_str} - {time_str} - {self.place}"
