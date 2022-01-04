# Django
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Own
from .validators import validate_email, validate_phone
from .models import Contact
from utils.views import get_user

# Thrid Party
from json import loads


def get_email_or_phone(email_or_phone):
	""" Get and valid email or phone
	@param: str
	@return bool, str or bool, str or bool
	"""

	valid = email = phone = False

	if validate_email(email_or_phone) or validate_phone(email_or_phone):
		
		valid = True
		
		if '@' in email_or_phone:
			email = email_or_phone
		else:
			phone = email_or_phone
	
	return valid, email, phone


@csrf_exempt
@require_http_methods(['POST'])
def ContactView(request):

	try:
		
		data = loads(request.body)
		email_or_phone = data.get('email', False)
		valid, email, phone = get_email_or_phone(email_or_phone)

		if valid:
			data['user'] = get_user(request.COOKIES)
			data['email'] = email
			data['phone'] = phone

			Contact.objects.create(**data)

			return JsonResponse({"status": "ok"})

		raise ValueError('Invalid email or phone')

	except JSONDecodeError:
		error_message = 'An error has happened.'
	except ValueError:
		error_message = 'Email or phone with invalid format.'
	
	return JsonResponse({
		"status": "fail",
		"message": error_message
		})

