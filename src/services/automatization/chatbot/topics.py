"""Topics that the chatbot should be able to automate"""

from collections import namedtuple

from services.automatization.chatbot.actions import (
    get_contact,
    get_location,
    get_opening_hours,
    get_products,
    get_welcome_greeting,
    get_goodbye_greeting,
    get_another_action
)


_Topic = namedtuple('Topic', ['key', 'description', 'response'])


_TOPICS = [
    _Topic(
        'PRODUCT',
        'User is asking for some product or it price',
        get_products),
    _Topic(
        'CONTACT',
        'User is asking for contact information',
        get_contact),
    _Topic(
        'LOCATION',
        'User is asking for where our location is',
        get_location),
    _Topic(
        'OPENING',
        'User is asking for our opening hours',
        get_opening_hours),
    _Topic(
        'WELCOME_GREETING',
        'if the user is greeting welcome',
        get_welcome_greeting),
    _Topic(
        'GOODBYE_GREETING',
        'If the user is greeting goodby',
        get_goodbye_greeting),
    _Topic(
        'ANOTHER',
        'If the user is asking about something that isn\'t in all previous topics',
        get_another_action),
    ]


class Topic:

    @staticmethod
    def respond_by(topic_key: str) -> str | None:
        for topic in _TOPICS:
            if topic_key == topic.key:
                return topic.response()
        return None

    def get_topic_key_from(content: str) -> str:
        topic_key = content.replace('Topic:', '').replace(' ', '')
        return topic_key

