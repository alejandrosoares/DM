from django.test import TestCase

from contact.models import Contact, ContactInformation


class ContactTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {
            'name': 'John',
            'message': 'My message',
        }

    def test_create_contact_with_valid_email(self):
        self.data['email'] = 'john@gmail.com'
        Contact.create(self.data)
        first = Contact.objects.first()
        self.assertEqual(first.email, self.data['email'])
        self.assertIsNone(first.phone)

    def test_create_contact_with_valid_phone(self):
        self.data['email'] = '+541515151515'
        Contact.create(self.data)
        first = Contact.objects.first()
        self.assertEqual(first.phone, self.data['phone'])
        self.assertIsNone(first.email)

    def test_create_contact_with_invalid_email(self):
        self.data['email'] = 'john@gmail'
        with self.assertRaises(ValueError):
            Contact.create(self.data)

    def test_create_contact_with_invalid_phone(self):
        self.data['email'] = '+adsfasdf'
        with self.assertRaises(ValueError):
            Contact.create(self.data)


class ContactInformationTestCase(TestCase):

    def setUp(self):
        self.data = {
            'facebook': 'http://www.facebook.com/test123',
            'instagram': 'http://www.instagram.com/test123',
            'twitter': 'http://www.twitter.com/test123',
            'phone': '1234567890',
        }
        ContactInformation.objects.create(**self.data)

    def test_get_first(self):
        self.assertEqual(ContactInformation.get_first(), self.data)
