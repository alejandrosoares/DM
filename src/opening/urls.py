from django.urls import path, include
from django.conf import settings


app_name = "opening"
urlpatterns = [
    path(f'api/{settings.API_VERSION}/', include('opening.api.urls')),
]
