from django.db import models

DAYS = [
    (1, "Lunes"),
    (2, "Martes"),
    (3, "Miércoles"),
    (4, "Jueves"),
    (5, "Viernes"),
    (6, "Sábado"),
    (7, "Domingo")
]

HOURS = [
    (1, "8"),
    (2, "8:30"),
    (3, "9"),
    (4, "9:30"),
    (5, "10"),
    (6, "10:30"),
    (7, "11"),
    (8, "11:30"),
    (9, "12"),
    (10, "12:30"),
    (11, "13"),
    (12, "13:30"),
    (13, "14"),
    (14, "14:30"),
    (15, "15"),
    (16, "15:30"),
    (17, "16"),
    (18, "16:30"),
    (19, "17"),
    (20, "17:30"),
    (21, "18"),
    (22, "18:30"),
    (23, "19"),
    (24, "19:30"),
    (25, "20"),
    (26, "20:30"),
    (27, "21"),
    (28, "21:30")
]

class Schedule(models.Model):
    day = models.SmallIntegerField("Day", choices=DAYS)
    start = models.SmallIntegerField("Start", choices=HOURS)
    end = models.SmallIntegerField("End", choices=HOURS)
    order = models.SmallIntegerField("Order", blank=True)
    closed = models.BooleanField("Closed", default=False)

    def __assign_order(self):
        self.order = 0

    def save(self, *args, **kwargs):

        created = True if self._state.adding else False

        if created:
            self.__assign_order()

        super(__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.day} - {self.start} - {self.end}"

