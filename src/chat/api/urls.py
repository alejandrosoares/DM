from django.urls import path

from .views import (
    get_automatic_response_view,
    generate_new_chat_view,
    get_chat_messages,
)


app_name = "api"
urlpatterns = [
    path('', get_automatic_response_view, name="automatic-chatbot"),
    path('new-chat/', generate_new_chat_view, name="new-chat"),
    path('get-messages/', get_chat_messages, name="get-messages")
]
