# Django
from django.http import Http404, JsonResponse
from django.shortcuts import render

# Own
from .models import Product, Category


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


def get_recommedations_products(categories, exclude_id=None):
   """ Get recommendations products
   @param: products.Category
   @return: list
   """

   initial_list = []
   clean_list = []
   number_of_items = 4

   for c in categories:
         products = Product.objects.filter(category=c)

         if exclude_id:
            products.exclude(id=exclude_id)
            
         initial_list.extend(products)

   # Clear repeated
   for product in initial_list:
      if product not in clean_list:
         clean_list.append(product)

   if len(clean_list) > number_of_items:
      clean_list = clean_list[:number_of_items]
   
   return clean_list

def ProductView(request, product_id):
   """Product View."""

   try:
      product = Product.objects.get(id=product_id)
      categories = product.category.all()
      recommendations = get_recommedations_products(categories)

      context = {
         "product": product,
         "recommendations": recommendations
         }

   except Product.DoesNotExist:
      raise Http404("Product Not Found")

   return render(request, "products/product.html", context)

