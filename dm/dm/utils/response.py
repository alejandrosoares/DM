from django.http import JsonResponse


class ResponseJsonBuilder:

	def __init__(self):
		self.response = {
			'status': 'ok',
			'message': 'success'
		}

	def set_error_with(self, message: str) -> None:
		self.response['status'] = 'fail'
		self.response['message'] = message

	def get_response(self) -> JsonResponse:
		return JsonResponse(self.response)