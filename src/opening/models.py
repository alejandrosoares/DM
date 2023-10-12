from django.db import models

from .constants import (
    SEP_SCHEDULE,
    SEP_RANGE,
    DIC_DAYS,
    DAYS
)


class Opening(models.Model):

    day = models.PositiveSmallIntegerField(
        choices=DAYS,
        unique=True,
        error_messages={'unique': 'This day already exists.'}
    )
    weekday = models.PositiveSmallIntegerField()
    schedule_range = models.CharField(max_length=36, null=True, blank=True)
    closed = models.BooleanField(default=False)

    class Meta:
        ordering = ['day']

    @property
    def day_str(self):
        return DIC_DAYS[self.day]

    def update_schedule_range(self):
        if self.closed:
            self.schedule_range = 'Closed'
        else:
            self.__set_schedule_range()
        self.save()

    def __set_schedule_range(self):
        separator = SEP_SCHEDULE
        schedules = self.schedules.all().order_by('start')
        schedule_range = [f'{s.start_str} {separator} {s.end_str}' for s in schedules]
        self.schedule_range = SEP_RANGE.join(schedule_range)

    def __str__(self):
        return DIC_DAYS[self.day]


class ScheduleRange(models.Model):

    opening = models.ForeignKey(
        Opening,
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    start = models.TimeField()
    end = models.TimeField()

    @property
    def start_str(self):
        return self.start.strftime('%H:%M')

    @property
    def end_str(self):
        return self.end.strftime('%H:%M')

    def __str__(self):
        return f'{self.opening.day_str}: {self.start} to {self.end}'
