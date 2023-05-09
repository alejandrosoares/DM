from django.views.decorators.http import require_http_methods
from django.conf import settings

from utils.response import ResponseJsonBuilder
from chat.models import Chat
from chat.api.utils import (
    get_and_save_user_message,
    get_and_save_automatic_message,
    get_message_of
)


@require_http_methods(['POST'])
def get_automatic_response_view(request):
    res_builder = ResponseJsonBuilder()
    if settings.ENABLE_AUTOMATIC_CHATBOT:
        user_message = get_and_save_user_message(request.body)
        res_builder.obj = get_and_save_automatic_message(user_message)
    else:
        res_builder.set_error_with('Unavailable service')
    return res_builder.get_response()


@require_http_methods(['POST'])
def generate_new_chat_view(request):
    res_builder = ResponseJsonBuilder()
    chat = Chat.objects.create()
    res_builder.obj = {'id': chat.uuid}
    return res_builder.get_response()


@require_http_methods(['GET'])
def get_chat_messages(request):
    res_builder = ResponseJsonBuilder()
    uuid = request.GET.get('chatId', None)
    try:
        chat = Chat.objects.get(uuid=uuid)   
    except Chat.DoesNotExist: 
        res_builder.set_error_with('Chat with sent id does not exist')
    else:
        messages = get_message_of(chat)
        res_builder.obj = messages
    return res_builder.get_response()

