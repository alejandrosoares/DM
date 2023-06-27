from django.urls import path, include


app_name = "questions"
urlpatterns = [
    path('api/', include('questions.api.urls')),
]
