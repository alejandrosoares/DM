from django.db import models

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

    def __str__(self):
        return self.name
