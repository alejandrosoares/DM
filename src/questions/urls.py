from django.urls import path, include
from django.conf import settings


app_name = "questions"
urlpatterns = [
    path(f'api/{settings.API_VERSION}/', include('questions.api.urls')),
]
