# Django
from django.urls import path

# Own
from .views import PublicationView

app_name = "publications"
urlpatterns = [
   path('<str:code>', PublicationView, name="publication")
]
