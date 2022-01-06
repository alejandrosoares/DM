# Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse

# Own
from .models import Publication


def PublicationView(request, code):

   try:
      publication = Publication.objects.get(code=code)
   except Publication.DoesNotExist:
      messages.info(request, "La publicación a la que intentas acceder no existe.")
      return redirect('home:home')

   publication.increase_visits()
   products = publication.products.all()

   if len(products) == 1:
      product_id = products[0].id
      return redirect(reverse('products:product', kwargs={'product_id': product_id}))
   
   context = {
      'publication': publication,
      'products': products
   }
   return render(request, 'publications/product_group.html', context)

