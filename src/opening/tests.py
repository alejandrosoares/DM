from django.test import TestCase

from .models import Opening, ScheduleRange
from .constants import (
    SEP_SCHEDULE,
    DIC_DAYS,
    DAYS,
)


class OpeningTestCase(TestCase):

    def setUp(self):
        self.day = DAYS[1][0]
        self.start = "8"
        self.end = "10"
        self.opening = Opening.objects.create(day=self.day)
        self.schedule = ScheduleRange.objects.create(
            opening=self.opening,
            start=self.start,
            end=self.end
        )

    def test_get_schedule_range(self):
        expected_str = f'{self.start} {SEP_SCHEDULE} {self.end}'
        self.assertAlmostEqual(self.opening.schedule_range, expected_str)

    def test_get_str_day(self):
        expected_day = DIC_DAYS[self.day]
        self.assertAlmostEqual(self.opening.get_str_day(), expected_day)

    def test_update_schedule_range(self):
        new_start = "9"
        self.schedule.start = new_start
        self.schedule.save()
        expected_str = f'{new_start} {SEP_SCHEDULE} {self.end}'
        self.assertAlmostEqual(self.opening.schedule_range, expected_str)
