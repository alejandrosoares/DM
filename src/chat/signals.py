from django.db.models.signals import (
    pre_save,
)
from django.dispatch import receiver

from .models import ChatDocument


@receiver(pre_save, sender=ChatDocument)
def pre_save_products(sender, instance, **kwargs):
    instance.title = instance.title.upper()
    instance.source = instance.source.lower().replace(' ', '-')