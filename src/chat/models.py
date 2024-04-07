import uuid

from django.db import models


class ChatRole(models.TextChoices):
    USER = 'U', 'user'
    SYSTEM = 'S', 'system'
    ASSISTANT = 'A', 'assistant'


class Chat(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['uuid'], name='chat_uuid_idx')
        ]

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
    def create(chat_uuid, content, created_by):
        chat = Chat.objects.get(uuid=chat_uuid)
        ChatMessage.objects.create(chat=chat, content=content, created_by=created_by)

    def __str__(self):
        time = self.created.strftime('%d.%m.%Y %H:%M')
        return f'{self.chat.shorted_id} - {time} - {self.created_by}:{self.content}'


class ChatDocument(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    is_enabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
