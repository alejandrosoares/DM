from django.db import models

from utils.validators import phone_validator, validate_email_or_phone
from contact.utils import extract_valid_email_or_phone


class Contact(models.Model):

    name = models.CharField("Name", max_length=15)
    email = models.EmailField("Email", null=True)
    phone = models.CharField("Phone", null=True, max_length=20)
    message = models.TextField("Message", null=True)
    answered = models.BooleanField("Answered", default=False)
    date = models.DateTimeField(
        "Contact date",
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        verbose_name = verbose_name_plural = "Contact List"
        ordering = ['-date']

    @staticmethod
    def create(data: dict) -> None:
        email_or_phone = data.get('email', '')

        if not validate_email_or_phone(email_or_phone):
            raise ValueError()

        extracted_field = extract_valid_email_or_phone(email_or_phone)
        data['email'] = extracted_field.get('email')
        data['phone'] = extracted_field.get('phone')
        Contact.objects.create(**data)

    def __str__(self):
        return self.name


class ContactInformation(models.Model):

    facebook = models.URLField("Facebook", null=True, blank=True)
    instagram = models.URLField("Instagram", null=True, blank=True)
    twitter = models.URLField("Twitter", null=True, blank=True)
    phone = models.CharField(
        "Phone",
        max_length=17,
        blank=True,
        null=True,
        validators=[phone_validator])
    whatsapp = models.BooleanField("Do you have whatsapp?", default=False)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    @staticmethod
    def get_first() -> dict[str, str | None]:
        contact = ContactInformation.objects.all().first()
        return {
            'facebook': contact.facebook if contact else None,
            'instagram': contact.instagram if contact else None,
            'twitter': contact.twitter if contact else None,
            'phone': contact.phone if contact else None,
            'whatsapp': contact.whatsapp if contact else False
        }
