from django.db import models

from user_information.models import UserInformation

class Contact(models.Model):

    name = models.CharField("Name", max_length=15)
    email = models.EmailField("Email", null=True)
    phone = models.CharField("Phone", null=True, max_length=20)
    message = models.TextField("Message", null=True)
    answered = models.BooleanField("Answered", default=False)
    user = models.ForeignKey(
        UserInformation,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="User ID"
    )
    date = models.DateTimeField(
        "Contact date",
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        verbose_name = verbose_name_plural = "Contact List"
        ordering = ['-date']

    def __str__(self):
        return self.name
