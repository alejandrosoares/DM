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


def get_recommedations_products(categories):
   auxiliary = []
   recommendations = []

   for c in categories:
         products = Product.objects.filter(category=c)
         auxiliary.extend(products)

   # Clear repeated
   for product in auxiliary:
      if product not in recommendations:
         recommendations.append(product)

   if len(recommendations) > 12:
      recommendations = recommendations[:12]
   
   index_last_item =  len(recommendations) - 1
   start = 0
   end = 3
   auxiliary = []

   for _ in range(3):
      auxiliary.append(recommendations[start: end])
      start = end
      end = end + 3
      if end > index_last_item:
         end = index_last_item

   return auxiliary

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

