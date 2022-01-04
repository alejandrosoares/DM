# Django
from django.db import models

# Own
from .variables import (
    DIC_DAYS, 
    DAYS, 
    HOURS,
    REFERENCE_HOURS
)


class Opening(models.Model):
    """Opening Times"""

    day = models.SmallIntegerField("Day", choices=DAYS)
    str_schedules = models.CharField(
        "Schedules", 
        max_length=36, 
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['day']
    
    def update_str_schedule(self):

        scheds = self.schedules.all().order_by('order')
        str_schedules = ''
        last_item = scheds.last()

        for sched in scheds:
            # Add schedule to str_schedule
            str_schedules += '{} a {}'.format(
                sched.start,
                sched.end
            )
            if not sched == last_item:
                # Is not last item
                str_schedules += ' - '

        self.str_schedules = str_schedules
        self.save()

    def get_day(self):
        return DIC_DAYS[self.day]

    def __str__(self):
        return DIC_DAYS[self.day]


class Schedule(models.Model):
    """Schedule range"""

    opening = models.ForeignKey(
        Opening, 
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    start = models.CharField("Start", max_length=5, choices=HOURS)
    end = models.CharField("End",  max_length=5, choices=HOURS)
    order = models.SmallIntegerField("Order", blank=True)
    closed = models.BooleanField("Closed", default=False)
    
    def get_status(self):
        """Get status of schedule"""

        if self.closed:
            return 'Cerrado'
        
        return f'{self.start} a {self.end}'
    
    def __update_opening(self):
        """Trigger update schedules"""

        self.opening.update_str_schedule()
    
    def __set_schedule_order(self):
        """Set schedule order
        
        Stablish the order of the schedule based in REFERENCE_HOURS
        and self.start value
        """
        self.order = REFERENCE_HOURS[self.start]

    def save(self, *args, **kwargs):

        self.__set_schedule_order()

        super(__class__, self).save(*args, **kwargs)

        self.__update_opening()

    def __str__(self):
        return self.opening.get_day()