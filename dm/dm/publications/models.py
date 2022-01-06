# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Own
from products.models import Product
from dm.settings import (
   BITLY_URL,
   BITLY_TOKEN, 
   DOMAIN,
   BUSINNES_NAME
)

# Third parties
import json
import requests
from random import randint


class Publication(models.Model):
   """Publication
   These instance are posts to post on social networks

   Code is used for search publications
   uuid is used for generate the code field.
   """
   
   products = models.ManyToManyField(Product)

   name = models.CharField(
      "Publicacion", 
      max_length=50, 
      unique=True,
      error_messages={
         'unique': 'Ya existe una publicación con este nombre.'
      }
      )
   created = models.DateTimeField("Creacion", auto_now_add=True, auto_now=False)
   code = models.PositiveIntegerField("Code", blank=True)
   visits = models.PositiveIntegerField("Visitas", default=0)
   link = models.URLField("Link", blank=True)
   shorten_link = models.BooleanField("Acortar link", default=True)
   short_link = models.URLField("Link corto", blank=True, null=True)

   class Meta:
      verbose_name = "Publicacion"
      verbose_name_plural = "Publicaciones"
   
   def __add_code_field(self):

      codes = __class__.objects.values_list("code", flat=True)

      while True:
         code = randint(1000, 32766)
         if code not in codes:
               break

      self.code = code

   def __add_link_field(self):

      kwargs = {'code': self.code}

      self.link = '{}{}'.format(
            DOMAIN,
            reverse("publications:publication", kwargs=kwargs)
         )

   def pre_save(self):
      """Pre save tasks"""

      self.__add_code_field()
      self.__add_link_field()

   def save(self, *args, **kwargs):

      create = True if self._state.adding else False

      if create:
         self.pre_save()

      super(__class__, self).save(*args, **kwargs)

   def __str__(self):
      return self.name


@receiver(post_save, sender=Publication)
def PostSavePublication(sender, instance, created, **kwargs):
   """ Create short link through Bitly API Service """

   if instance.shorten_link and not instance.short_link:

      # Request to Bitly API
      headers = {
         'Authorization': f"{BITLY_TOKEN}",
         'Content-Type': 'application/json',
      }

      payload = {
         "long_url": instance.link,
         "title": f'{BUSINNES_NAME} - {instance.name}'
      }

      res = requests.post(
            BITLY_URL, 
            headers=headers, 
            data=json.dumps(payload)
         )
      
      if res.status_code == 201:
         json_response = res.json()
         instance.short_link = json_response['link']
         instance.save()