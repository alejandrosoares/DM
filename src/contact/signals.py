from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver
from django.core.cache import cache

from utils.cache.constants import CACHE_KEY_MOD_CONTACT, CACHE_KEY_MOD_QUESTIONS
from .models import ContactInformation


@receiver(post_save, sender=ContactInformation)
def post_save_contact(sender, instance, **kwargs):
    cache.delete(CACHE_KEY_MOD_CONTACT)
    cache.delete(CACHE_KEY_MOD_QUESTIONS)
