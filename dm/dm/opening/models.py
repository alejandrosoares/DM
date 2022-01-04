from django.db import models

from .variables import DIC_DAYS, DAYS, HOURS

class Opening(models.Model):
    """Opening Times"""

    day = models.SmallIntegerField("Day", choices=DAYS)
    start = models.SmallIntegerField("Start", choices=HOURS)
    end = models.SmallIntegerField("End", choices=HOURS)
    order = models.SmallIntegerField("Order", blank=True)
    closed = models.BooleanField("Closed", default=False)

    class Meta:
        ordering = ['day']
    
    def get_day(self):
        return DIC_DAYS[self.day]

    def get_status(self):
        if self.closed:
            return 'Cerrado'
        
        return f'{self.start} a {self.end}'

    def __str__(self):
        return "{} - {}".format(
            self.get_day(),
            self.get_status()
        )


