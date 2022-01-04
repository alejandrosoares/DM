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

    day = models.SmallIntegerField(
        'Day', 
        choices=DAYS, 
        unique=True,
        error_messages= {
            'unique': 'Ya existe este día.'
        }
    )
    str_schedules = models.CharField(
        'Schedules', 
        max_length=36, 
        null=True,
        blank=True
    )
    closed = models.BooleanField('Closed', default=False)

    class Meta:
        ordering = ['day']
    
    def __update_str_schedule(self):
        """Write schedules or closed in str_schedules field"""
        
        if not self.closed:
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
        else:
            # Closed
            self.str_schedules = 'Cerrado'

    def get_day(self):
        return DIC_DAYS[self.day]

    def save(self, *args, **kwargs):

        self.__update_str_schedule()

        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return DIC_DAYS[self.day]


class Schedule(models.Model):
    """Schedule range"""

    opening = models.ForeignKey(
        Opening, 
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    start = models.CharField('Start', max_length=5, choices=HOURS)
    end = models.CharField('End',  max_length=5, choices=HOURS)
    order = models.SmallIntegerField('Order', blank=True)
    
    
    def __update_opening(self):
        """Trigger update Opening instance"""

        self.opening.save()
    
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