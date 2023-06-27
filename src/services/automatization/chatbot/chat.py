from services.chatgpt.chat_api import ChatGPTAPI, ChatMessage
from .topics import Topic
from .context import get_chatbot_context


class ChatBot:

    _chat = ChatGPTAPI()

    def get_response(self, message: str) -> str:
        prompt = self.__get_prompt(message)
        chat_message = ChatMessage(prompt)
        chat_response = __class__._chat.send(chat_message)
        topic_key = Topic.get_topic_key_from(chat_response.content)
        assistant_response = Topic.respond_by(topic_key)
        return assistant_response

    def __get_prompt(self, message: str) -> str:
        context = get_chatbot_context()
        format_msg = self.__format_message(message)
        prompt = context + format_msg
        return prompt

    def __format_message(self, message: str) -> str:
        return f"User question: '''{message}'''"
