from django.test import TestCase

from datetime import time

from .models import Opening, ScheduleRange
from .constants import (
    SEP_SCHEDULE,
    DIC_DAYS,
    DAYS,
)


class OpeningTestCase(TestCase):

    time_format = "%H:%M"

    def setUp(self):
        self.cls = OpeningTestCase
        self.day = DAYS[1][0]
        self.weekday = 1
        self.start = time(hour=8)
        self.end = time(hour=10)
        self.opening = Opening.objects.create(day=self.day, weekday=self.weekday)
        self.schedule = ScheduleRange.objects.create(
            opening=self.opening,
            start=self.start,
            end=self.end
        )
    
    def __get_expected_schedule_range(self, start, end):
        expected_str = '{} {} {}'.format(
            start.strftime(self.cls.time_format),
            SEP_SCHEDULE,
            end.strftime(self.cls.time_format)
        )
        return expected_str

    def test_get_schedule_range(self):
        expected_str = self.__get_expected_schedule_range(self.start, self.end)
        self.assertAlmostEqual(self.opening.schedule_range, expected_str)

    def test_get_str_day(self):
        expected_day = DIC_DAYS[self.day]
        self.assertAlmostEqual(self.opening.day_str, expected_day)

    def test_update_schedule_range(self):
        new_start = time(hour=9)
        self.schedule.start = new_start
        self.schedule.save()
        expected_str = self.__get_expected_schedule_range(new_start, self.end)
        self.assertAlmostEqual(self.opening.schedule_range, expected_str)
