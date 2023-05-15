from django.urls import path, include

from .views import  product_view


app_name = "products"
urlpatterns = [
    path('<int:product_id>', product_view, name="product"),
    path('api/', include('products.api.urls'))
]
