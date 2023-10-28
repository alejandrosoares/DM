from django.conf import settings

from typing import NamedTuple
from datetime import datetime, timedelta

from utils.request import Request
from .constants import URL_DMREC_SERVICE_TOKEN


Token = NamedTuple('Token', [('value', str), ('expiry_time', datetime)])


class AuthRecommendationService:

    def __init__(self):
        self.url = URL_DMREC_SERVICE_TOKEN
        self.client_id = settings.DMREC_CLIENT_ID
        self.client_secret = settings.DMREC_CLIENT_SECRET
        self.username = settings.DMREC_USERNAME
        self.password = settings.DMREC_PASSWORD
        self.token = None

    def get_token(self) -> Token:
        if self.token is None:
            self.token = self._get_token()
        return self.token

    def refresh_and_get_token(self) -> Token:
        self.token = self._get_token()
        return self.token

    def _get_token(self) -> str:
        response = self._get_response()
        assert response.status_code == 200, 'Error getting token'

        response_data = response.json()
        expiry_time = datetime.now() + timedelta(seconds=response_data['expires_in'])
        token = Token(response_data['access_token'], expiry_time)
        return token

    def _get_response(self):
        auth = self._get_auth()
        data = self._get_data()
        request = Request.Builder(self.url) \
            .with_post_method() \
            .with_data(data) \
            .with_auth(auth) \
            .build()
        response = request.send()
        return response

    def _get_data(self) -> dict:
        return {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password
        }

    def _get_auth(self) -> tuple[str]:
        return (self.client_id, self.client_secret)


AuthRecommendationServiceInstance = AuthRecommendationService()
