from django.urls import path

from .views import ProductsView, ProductView

app_name = "product"
urlpatterns = [
    path('', ProductsView, name="all"),
    path('<int:product_id>', ProductView, name="product"),
]