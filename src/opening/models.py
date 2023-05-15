from django.db import models

from .constants import (
    SEP_SCHEDULE,
    DIC_DAYS,
    DAYS,
    HOURS,
    ORDER_OF_HOURS
)


class Opening(models.Model):

    day = models.SmallIntegerField(
        choices=DAYS,
        unique=True,
        error_messages={'unique': 'This day already exists.'}
    )
    schedule_range = models.CharField(max_length=36, null=True, blank=True)
    closed = models.BooleanField(default=False)

    class Meta:
        ordering = ['day']

    def update_schedule_range(self):
        if self.closed:
            self.schedule_range = 'Closed'
        else:
            self.__set_schedule_range()

        self.save()
    
    def __set_schedule_range(self):
        sep_schedule = SEP_SCHEDULE
        schedules = self.schedulerange_set.all().order_by('order')
        schedule_range = ''

        for sch in schedules:
            schedule_range += '{} {} {} - '.format(
                sch.start,
                sep_schedule,
                sch.end
            )

        schedule_range = schedule_range[:-3]  # Removing last dash
        self.schedule_range = schedule_range

    def get_str_day(self):
        return DIC_DAYS[self.day]

    def __str__(self):
        return DIC_DAYS[self.day]


class ScheduleRange(models.Model):

    opening = models.ForeignKey(Opening, on_delete=models.CASCADE)
    start = models.CharField(max_length=5, choices=HOURS)
    end = models.CharField(max_length=5, choices=HOURS)
    order = models.SmallIntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.__update_order()
        super(__class__, self).save(*args, **kwargs)

    def __update_order(self):
        self.order = ORDER_OF_HOURS[self.start]

    def __str__(self):
        day = self.opening.get_str_day()
        return f'{day}: {self.start} to {self.end}'
