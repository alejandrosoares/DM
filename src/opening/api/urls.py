from django.urls import path

from .views import get_opening_view


app_name = 'api'
urlpatterns = [
    path('', get_opening_view, name='all'),
]
