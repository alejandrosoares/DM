from django.urls import path, include
from django.conf import settings

from .views import product_view


app_name = "products"
urlpatterns = [
    path('<int:product_id>', product_view, name="product"),
    path(f'api/{settings.API_VERSION}/', include('products.api.urls'))
]
