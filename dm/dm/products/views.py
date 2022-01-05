# Django
from django.http import Http404, JsonResponse
from django.shortcuts import render

# Own
from .models import Product


def ProductsView(request):
   """ Products View.
   Get Product JSON list
   @return: json
   """
   DOMAIN = request.get_host()
   products = Product.objects.all()
   product_list = []

   for p in products:
      product =  {
         "id": p.id, 
         "name": p.name, 
         "price": p.price,
         "code": p.code,
         "img": f"http://{DOMAIN}{p.img.url}"            
         }   
      product_list.append(product)

   return JsonResponse(product_list, safe=False)


def ProductView(request, product_id):
   """Product View."""

   try:
      product = Product.objects.get(id=product_id)
      context = {"product": product}

   except Product.DoesNotExist:
      raise Http404("Product Not Found")

   return render(request, "products/product.html", context)
