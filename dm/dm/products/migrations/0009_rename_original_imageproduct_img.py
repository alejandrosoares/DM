# Generated by Django 3.2.5 on 2022-01-18 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220118_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageproduct',
            old_name='original',
            new_name='img',
        ),
    ]