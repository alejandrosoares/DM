from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Contact
from utils.views import get_user

from json import loads

require_http_methods(['POST'])
def ContactView(request):
	
	data = loads(request.body)

	try:
		name = data.get('name', False)
		message = data.get('message', False)
		email_phone =data.get('email', False)

		Contact.objects.create(
			name = name, 
			message = message, 
			email = email_phone if '@' in email_phone else False,
			phone = str(email_phone) if '@' not in email_phone else False,
			user = get_user(request.COOKIES)
		)

		response = JsonResponse({"status":"ok"})
	except:
		response = JsonResponse({"status":"fail"})

	return response
