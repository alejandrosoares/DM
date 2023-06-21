from django.views.decorators.http import require_http_methods
from django.core.cache import cache

from utils.cache.constants import CACHE_KEY_MOD_QUESTIONS
from utils.response import ResponseJsonBuilder, get_dict_from
from questions.models import Question
from contact.models import ContactInformation


@require_http_methods(['GET'])
def get_questions_view(request):
    res_builder = ResponseJsonBuilder()
    product_questions = cache.get_or_set(CACHE_KEY_MOD_QUESTIONS, get_product_questions)
    res_builder.obj = product_questions
    return res_builder.get_response(safe=False)


def get_product_questions() -> dict:
    fields = ['id', 'content']
    questions = Question.objects.all()
    phone = ContactInformation.get_first()['phone']
    info = {
        'questions': get_dict_from(questions, fields),
        'phone': phone
    }
    return info
