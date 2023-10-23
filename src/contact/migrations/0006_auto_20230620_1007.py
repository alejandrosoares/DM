# Generated by Django 3.2.11 on 2023-06-20 13:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contactinformation_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinformation',
            name='whatsapp',
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='phone',
            field=models.CharField(default=3755445423, max_length=17, validators=[django.core.validators.RegexValidator(message='Format: +549999999999 o 549999999999 up to 16 digits.', regex='^\\+?\\d{9,16}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]