from django.views.decorators.http import require_http_methods

from utils.response import ResponseJsonBuilder
from opening.models import Opening
from .utils import (
    ScheduleInformationChecker
)


@require_http_methods(['GET'])
def get_opening_view(request):
    response_builder = ResponseJsonBuilder()
    openings = Opening.objects.all()
    response_builder.obj = convert_to_list(openings)
    return response_builder.get_response()


def convert_to_list(openings):
    res = {}
    for opening in openings:
        schedule_checker = ScheduleInformationChecker(opening)
        schedule_information = schedule_checker.get_information()
        res[opening.weekday] = {
            'day': opening.day_str,
            'schedule': opening.schedule_range,
            'isWeekday': schedule_information.is_weekday,
            'open': {
                'isOpen':  schedule_information.is_open,
                'message': schedule_information.message
            }
        }
    return res
