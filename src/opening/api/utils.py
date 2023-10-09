from typing import NamedTuple, Optional
from enum import Enum
from datetime import datetime, time, timedelta

from opening.models import Opening, ScheduleRange


class ScheduleInformationMessage(Enum):
    OPEN = 'Open'
    CLOSE = 'Close'
    OPEN_CLOSING = 'Open, closing soon'
    CLOSE_OPENING = 'Close, opening soon'


ScheduleInformation = NamedTuple('ScheduleInformation', [
    ('is_weekday', bool), 
    ('is_open', bool), 
    ('message', str)
    ]
)


class ScheduleInformationChecker:

    def __init__(self, opening: Opening):
        self.now = datetime.now()
        self.opening = opening
        self.schedules = self.opening.schedules.all()
        self.is_weekday = False
        self.is_open = False
        self.is_opening_soon = False
        self.is_closing_soon = False
        self.message = ScheduleInformationMessage.CLOSE.value
    
    def get_information(self) -> ScheduleInformation:
        self.is_weekday = self.__is_current_weekday()
        if not self.is_weekday:
            return self.__build_information()
        
        print(self.is_weekday)
        open_schedule = self.__get_open_schedule_if_exists()
        if open_schedule:
            self.is_open = True
            self.is_closing_soon = self.__is_soon_to_close(open_schedule)
            self.message = self.__get_open_message()
            open_information = self.__build_information()
        else:
            close_schedule = self.__get_close_schedule_soon_to_open_if_exists()
            self.is_opening_soon = True if close_schedule else False
            self.message = self.__get_close_message()
            open_information = self.__build_information()
        return open_information
    
    def __get_open_schedule_if_exists(self) -> Optional[ScheduleRange]:
        for schedule in self.schedules:
            if self.__is_open(schedule):
                return schedule
        return None

    def __get_close_schedule_soon_to_open_if_exists(self) -> Optional[ScheduleRange]:
        for schedule in self.schedules:
            if self.__is_soon_to_open(schedule):
                return schedule
        return None
    
    def __is_open(self, schedule: ScheduleRange) -> bool:
        is_open = schedule.start <= self.now.time() <= schedule.end
        return is_open
    
    def __is_soon_to_open(self, schedule: ScheduleRange) -> bool:
        start_date = self.__get_today_date_with_custom_time(schedule.start)
        end_date = self.__get_today_date_with_custom_time(schedule.end)
        end_limit = end_date + timedelta(hours=-1)
        start_limit = start_date + timedelta(hours=-2)
        is_soon_to_open = (start_limit <= self.now) and (self.now < end_limit)
        return is_soon_to_open
    
    def __is_soon_to_close(self, schedule: ScheduleRange) -> bool:
        end_date = self.__get_today_date_with_custom_time(schedule.end)
        end_limit = end_date + timedelta(hours=-1)
        is_soon_to_close = end_limit <= self.now
        return is_soon_to_close

    def __build_information(self) -> ScheduleInformation:
        return ScheduleInformation(is_weekday=self.is_weekday, is_open=self.is_open, message=self.message)

    def __is_current_weekday(self) -> bool:
        current_weekday = self.now.isoweekday()
        return current_weekday == self.opening.weekday
    
    def __get_open_message(self) -> str:
        message = ScheduleInformationMessage.OPEN_CLOSING.value if self.is_closing_soon else ScheduleInformationMessage.OPEN.value
        return message 
    
    def __get_close_message(self) -> str:
        message = ScheduleInformationMessage.CLOSE_OPENING.value if self.is_opening_soon else ScheduleInformationMessage.CLOSE.value
        return message
    
    def __get_today_date_with_custom_time(self, time: time) -> datetime:
        today = datetime(
            year=self.now.year, 
            month=self.now.month, 
            day=self.now.day,
            hour=time.hour,
            minute=time.minute
        )
        return today
