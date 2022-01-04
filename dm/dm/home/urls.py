from django.urls import path
from .views import HomeView, SearchView, SearchByIdView, SearchByCategoryView, HomeWholeSalerView, ReceivingData

from .views import Pruebas,Pruebas2

app_name = "home"
urlpatterns = [
    path('', HomeView, name="home"),
    path('wholesaler', HomeWholeSalerView, name="home-wholesaler"),
    # path('products/', SearchView, name="search"),
    path('search-by-id/', SearchByIdView, name="search-by-id"),
    path('search-by-category/', SearchByCategoryView, name="search-by-category"),
    path('receiving-data/', ReceivingData, name="receiving-data"),
    path('pruebas/', Pruebas, name="pruebas"),
    path('pruebas2/', Pruebas2, name="pruebas2"),
]
