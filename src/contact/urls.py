from django.urls import path, include
from django.conf import settings


app_name = "contact"
urlpatterns = [
    path(f'api/{settings.API_VERSION}/', include('contact.api.urls')),
]
