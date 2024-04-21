from django.urls import path

from .views import get_categories, get_products_view, get_recommended_products_view


app_name = 'api'
urlpatterns = [
    path('categories/', get_categories, name="get-categories"),
    path('products/', get_products_view, name="get-products"),
    path(
        'recommended-products/<int:product_id>',
        get_recommended_products_view,
        name="get-recommended-products"),
]
