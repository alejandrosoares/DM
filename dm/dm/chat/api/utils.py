from json import loads

from django.core.serializers import serialize
from django.conf import settings

from services.automatization.chatbot.chat import ChatBot
from utils.views import get_data_from
from chat.models import Chat, ChatMessage, ChatRole


if settings.ENABLE_AUTOMATIC_CHATBOT:
    ChatBotService = ChatBot()


def get_and_save_user_message(req_body: bytes) -> dict:
    user_message = get_data_from(req_body)
    _save_message(user_message)
    return user_message


def get_and_save_automatic_message(user_message: dict) -> dict:
    assistant_response = ChatBotService.get_response(user_message['content'])
    assistant_data = {
        'content': assistant_response,
        'chatId': user_message['chatId'],
        'role': ChatRole.ASSISTANT.value
        }
    _save_message(assistant_data)
    return assistant_data


def get_message_of(chat: Chat) -> list[dict]:
    chats = ChatMessage.objects.filter(chat__id=chat.id).order_by('created')
    messages = serialize('json', chats, fields=['content', 'created', 'created_by']) 
    return loads(messages)


def _save_message(data: dict) -> None:
    chat_uuid = data['chatId']
    content = data['content']
    created_by = data['role']
    ChatMessage.create(chat_uuid=chat_uuid, content=content, created_by=created_by)



