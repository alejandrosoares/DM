from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.conf import settings

from opening.models import Opening
from products.models import Category
from contact.models import ContactInformation


@require_http_methods(["GET"])
def HomeView(request):

    contact = ContactInformation.get_first()
    opening = Opening.objects.all()
    categories = Category.objects.filter(enable=True)

    context = {
        'categories': categories,
        'opening': opening,
        'contact': contact,
        'ENABLE_AUTOMATIC_CHATBOT': settings.ENABLE_AUTOMATIC_CHATBOT
    }

    return render(request, 'home/home.html', context)
