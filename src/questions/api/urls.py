from django.urls import path

from .views import get_questions_view


app_name = "api"
urlpatterns = [
    path('questions/', get_questions_view, name="questions"),
]
