# Generated by Django 3.2.5 on 2022-01-06 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_user'),
        ('user_information', '0002_delete_publications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dateofvisit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='productsofinterest',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserInformation',
        ),
    ]
