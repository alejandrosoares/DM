# Django
from django.urls import path

# Own
from .views import ProductsView, ProductView

app_name = "products"
urlpatterns = [
   path('', ProductsView, name="all"),
   path('<int:product_id>', ProductView, name="product")
]