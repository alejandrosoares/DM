# Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# Own
from .models import Publication


def PublicationView(request, code):

   try:
      p = Publication.objects.get(code=code)
   except Publication.DoesNotExist:
      messages.info(request, "La publicación a la que intentas acceder no existe.")
      return redirect('home:home')
   
   

   return HttpResponse("Hola mundo")   

