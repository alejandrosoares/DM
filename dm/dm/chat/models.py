import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ChatRole(models.TextChoices):
    USER = 'U', _('user')
    SYSTEM = 'S', _('system')
    ASSISTANT = 'A', _('assistant')


class Chat(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    @property
    def shorted_id(self):
        shorted_id = str(self.uuid)[:6]
        return shorted_id

    def __str__(self):
        return str(self.uuid)


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.CharField(max_length=1, choices=ChatRole.choices)

    @staticmethod
    def create(chat_id, content, created_by):
        chat = Chat.objects.get(uuid=chat_id)
        ChatMessage.objects.create(chat=chat, content=content, created_by=created_by)

    def __str__(self):
        time = self.created.strftime('%d.%m.%Y %H:%M')
        return f'{self.chat.shorted_id} - {time} - {self.created_by}:{self.content}'
    
