# Django
from django.urls import path

# Own
from .views import ProductView

app_name = "product"
urlpatterns = [
   path('<int:product_id>', ProductView, name="product"),
]