from collections import namedtuple

_Topic = namedtuple('Topic', ['key', 'description', 'response'])

_TOPICS = [
    _Topic('PRODUCT', 'User asks for some product or it price', 'it costs 10 francs'),
    _Topic('CONTACT', 'User asks for contact information', 'Call me at 444444444'),
    _Topic('LOCATION', 'User asks for where our location is', 'We are in Katstrasse 404. We wait you!!'),
    _Topic('ANOTHER', 'If the user is asking about something that isn\'t in all previous topics', 'I will put with a vendor. Just a moment please')
]

def search_response_by(topic_key: str) -> str | None:
    for topic in _TOPICS:
        if topic_key == topic.key:
            return topic.response
    return None

__all__ = [
    search_response_by,
]
