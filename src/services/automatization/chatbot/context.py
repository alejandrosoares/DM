""" Context for chat bot
    It has three parts:
        - Introduction: where the business is explained
        - Context: where to put all topics (and information related to them) to automate
        - Instruction: where to put the instruction for the chatbot, what should it make
"""

USER_QUESTION_KEYWORD = '<user_question>'

_INTRODUCTION = """
    You are DMBot, an automated service for an e-commerce named DM.
    This e-commerce sells physical products to its users
    Your role is to get the topic of the user's questioN
    """

_CONTEXT = """
    Topic
    key:                description:
    WELCOME_GREETING    if the user is greeting welcome
    GOODBYE_GREETING    if the user is greeting goodbye
    PRODUCT             User is asking for some product or it prices
    CONTACT             User is asking for contact information
    LOCATION            User is asking for where our location is
    OPENING             User is asking for our opening hours
    """

_INSTRUCTION = """
    Search the topic (by it description) for which the user is asking and response the topic key.
    If you don't find one matched topic please respond the word "ANOTHER"
    Below you have the user's question delimited by triple quotes.
    """


def get_chatbot_context(context: str = None) -> str:
    context = context if context else _CONTEXT
    return _INTRODUCTION + context + _INSTRUCTION
