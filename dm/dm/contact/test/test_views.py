from json import loads

from django.test import TestCase, Client
from django.urls import reverse


class ContactViewTestCase(TestCase):
    pass

    def setUp(self):
        self.client = Client()
        self.contact_url = reverse("contact:contact")
        self.data = {
            'name': 'John',
            'message': 'My message',
        }
        
    def test_create_contact_with_valid_email(self):
        self.data['email'] = 'john@gmail.com'
        res = self.client.post(
            self.contact_url, 
            self.data,
            content_type="application/json",
            HTTP_ACCEPT="application/json",
            )
        data_res = loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data_res['status'], 'ok')

    def test_create_contact_with_invalid_email(self):
        self.data['email'] = 'john@gmail'
        res = self.client.post(self.contact_url, self.data)
        data_res = loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data_res['status'], 'fail')
        