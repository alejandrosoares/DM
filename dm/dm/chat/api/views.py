from json import loads

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.serializers import serialize
from django.conf import settings

from services.automatization.chatbot.chat import ChatBot
from utils.views import get_data_from
from utils.response import ResponseJsonBuilder
from chat.models import Chat, ChatMessage

if settings.ENABLE_AUTOMATIC_CHATBOT:
    ChatBotService = ChatBot()


@require_http_methods(['POST'])
def get_automatic_response_view(request):
    res_builder = ResponseJsonBuilder()
    if settings.ENABLE_AUTOMATIC_CHATBOT:
        data = get_data_from(request.body)
        user_message = data['content']
        assistant_response = ChatBotService.get_response(user_message)
        res_builder.obj = {'content': assistant_response}
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
        messages = _get_serialized_data_from(chat.id)
        res_builder.obj = messages
    except Chat.DoesNotExist: 
        res_builder.set_error_with('Chat with sent id does not exist')
    return res_builder.get_response()


def _get_serialized_data_from(chat_id):
    chats = ChatMessage.objects.filter(chat__id=chat_id).order_by('created')
    messages = serialize('json', chats, fields=['content', 'created', 'created_by'])
    return loads(messages)

