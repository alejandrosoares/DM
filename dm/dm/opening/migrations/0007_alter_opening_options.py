# Generated by Django 3.2.5 on 2022-01-04 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opening', '0006_alter_opening_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opening',
            options={'ordering': ['day']},
        ),
    ]
