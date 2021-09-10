# -*- coding: utf-8 -*-

from ics import Calendar, Event, DisplayAlarm
from datetime import datetime, timedelta
from dateutil import tz


class CalendarGenerator:
    def __init__(self, file_name: str, timetable_dict: dict, alarm_to_events_hours: int = 1):
        self.filename = file_name
        self.timetable_dict = timetable_dict
        self.calendar = Calendar()
        self.alarm_to_events_hours = -alarm_to_events_hours
        self.timezone = tz.gettz("Europe/Moscow")

    def generate_calendar_events(self):
        for date_obj, day_dict in self.timetable_dict.items():
            for time_obj, event_dict in day_dict['lessons'].items():
                datetime_obj = datetime.combine(datetime.strptime(date_obj, '%d.%m.%Y'),
                                                datetime.strptime(time_obj, "%H:%M").time())
                datetime_end_obj = datetime_obj + timedelta(hours=1, minutes=30)

                datetime_start_obj = datetime_obj.replace(tzinfo=self.timezone).astimezone(tz.tzutc())
                datetime_end_obj = datetime_end_obj.replace(tzinfo=self.timezone).astimezone(tz.tzutc())

                if event_dict:
                    event = Event()
                    event.name = event_dict['discipline']
                    event.description = event_dict['discipline'] + '\n' + 'Преподаватель: ' + event_dict['teacher']
                    event.location = 'Аудитория: ' + event_dict['room']
                    event.begin = datetime_start_obj
                    event.end = datetime_end_obj

                    alarm = DisplayAlarm()
                    alarm.trigger = timedelta(hours=self.alarm_to_events_hours)
                    alarm.display_text = event.description

                    event.alarms.append(alarm)
                    self.calendar.events.add(event)

    def create_ics_file(self):
        filename = self.filename + '.ics'
        with open(filename, 'w', encoding='utf-8', newline='') as my_file:
            my_file.writelines(self.calendar)

    def create_timetable(self):
        self.generate_calendar_events()
        self.create_ics_file()

    def return_calendar_as_text(self):
        return self.calendar
