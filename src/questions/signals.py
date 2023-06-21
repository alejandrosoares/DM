from django.db.models.signals import (
    post_save,
    post_delete,
)
from django.dispatch import receiver
from django.core.cache import cache

from utils.cache.constants import CACHE_KEY_MOD_QUESTIONS
from .models import Question


@receiver(post_save, sender=Question)
def post_save_questions(sender, instance, **kwargs):
    cache.delete(CACHE_KEY_MOD_QUESTIONS)


@receiver(post_delete, sender=Question)
def post_delete_questions(sender, instance, **kwargs):
    cache.delete(CACHE_KEY_MOD_QUESTIONS)
