# Django
from django.urls import path

# Own
from .views import (
   HomeView, 
   SearchView, 
   SearchByIdView, 
   SearchByCategoryView, 
   ReceivingData
)
from .views import Pruebas,Pruebas2

app_name = "home"
urlpatterns = [
    path('', HomeView, name="home"),
    # path('products/', SearchView, name="search"),
    path('search-by-id/', SearchByIdView, name="search-by-id"),
    path('search-by-category/', SearchByCategoryView, name="search-by-category"),
    path('receiving-data/', ReceivingData, name="receiving-data"),
    path('pruebas/', Pruebas, name="pruebas"),
    path('pruebas2/', Pruebas2, name="pruebas2"),
]
