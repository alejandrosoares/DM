from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Product

def ProductsView(request):

    print("Products lsit view")
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

        context =  {
            "product": product
            }
        return render(request, "products/product.html", context)
    
    except Product.DoesNotExist:
        pass

    return HttpResponse("Product Not Found")