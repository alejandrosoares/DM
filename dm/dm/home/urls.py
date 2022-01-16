# Django
from django.urls import path

# Own
from .views import HomeView


app_name = "home"
urlpatterns = [
    path('', HomeView, name="home")

]
