from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from utils.cache.constants import CACHE_KEY_MOD_OPENING
from .models import Opening, ScheduleRange


@receiver(post_save, sender=ScheduleRange)
def post_save_schedule(sender, instance, created, **kwargs):
    opening = instance.opening
    opening.update_schedule_range()


@receiver(post_save, sender=Opening)
def post_save_opening(sender, instance, created, **kwargs):
    cache.delete(CACHE_KEY_MOD_OPENING)
