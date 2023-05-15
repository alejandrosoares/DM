from django.urls import path

from .views import contact_view


app_name = "api"
urlpatterns = [
   path('', contact_view, name="contact"),
]