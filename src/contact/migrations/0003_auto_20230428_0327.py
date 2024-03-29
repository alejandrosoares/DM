# Generated by Django 3.2.11 on 2023-04-28 06:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactinformation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactinformation',
            options={'verbose_name': 'Contact Information', 'verbose_name_plural': 'Contact Information'},
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='whatsapp',
            field=models.BooleanField(default=False, verbose_name='Do you have whatsapp?'),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Format: +549999999999 o 549999999999 up to 16 digits.', regex='^\\+?\\d{9,16}$')], verbose_name='Phone'),
        ),
    ]
