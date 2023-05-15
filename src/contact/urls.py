from django.urls import path, include


app_name = "contact"
urlpatterns = [
   path('', include('contact.api.urls')),
]