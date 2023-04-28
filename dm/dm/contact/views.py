from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from json.decoder import JSONDecodeError

from utils.validators import (
    validate_email_or_phone,
)
from utils.views import (
    get_data_from,
)
from utils.response import ResponseJsonBuilder
from .models import Contact


@csrf_exempt
@require_http_methods(['POST'])
def contact_view(request):

    response_builder = ResponseJsonBuilder()

    try:
        data = get_data_from(request.body)
        Contact.create(data)
    except JSONDecodeError:
        response_builder.set_error_with('An error has happened.')
    except ValueError:
        response_builder.set_error_with('Invalid email or phone.')

    return response_builder.get_response()


