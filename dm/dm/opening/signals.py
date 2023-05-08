from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ScheduleRange


@receiver(post_save, sender=ScheduleRange)
def post_save_ScheduleRange(sender, instance, created, **kwargs):
    opening = instance.opening
    opening.update_schedule_range()
