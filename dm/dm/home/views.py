# Django
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

# Own
from user_information.models import Queries, SearchWords
from opening.models import Opening
from products.models import Product, Category


@require_http_methods(["GET"])
def HomeView(request):
    """Home View"""

    opening = Opening.objects.all()
    products = Product.objects.all()
    categories = Category.objects.filter(enable=True)

    context = {
        'products': products,
        'categories': categories,
        'opening': opening
    }

    return render(request, 'home/home.html', context)
