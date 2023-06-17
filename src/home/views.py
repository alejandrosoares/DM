from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.cache import cache

from utils.cache.constants import (
    CACHE_KEY_MOD_OPENING,
    CACHE_KEY_MOD_CATEGORIES,
    CACHE_KEY_MOD_CONTACT
)
from opening.models import Opening
from products.models import Category
from contact.models import ContactInformation


@require_http_methods(["GET"])
def HomeView(request):
    contact = cache.get_or_set(CACHE_KEY_MOD_CONTACT, ContactInformation.get_first)
    opening = cache.get_or_set(CACHE_KEY_MOD_OPENING, Opening.objects.all())
    categories = cache.get_or_set(
        CACHE_KEY_MOD_CATEGORIES,
        Category.objects.filter(enable=True)
    )

    context = {
        'categories': categories,
        'opening': opening,
        'contact': contact,
    }

    return render(request, 'home/home.html', context)
