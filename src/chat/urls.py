from django.urls import path, include
from django.conf import settings


app_name = "chat"
urlpatterns = [
    path(f'api/{settings.API_VERSION}/', include('chat.api.urls')),
]
