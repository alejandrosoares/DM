# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

# Own
from user_information.models import Queries, SearchWords, UseOfCategories
from publications.models import Publication
from opening.models import Opening
from products.models import Product, Category


@require_http_methods(["GET"])
def HomeView(request):
    """Home View"""

    # Opening
    opening = Opening.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    listWords = SearchWords.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'listWords': listWords,
        'opening': opening
    }

    return render(request, 'home/home.html', context)
