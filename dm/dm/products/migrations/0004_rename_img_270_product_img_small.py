# Generated by Django 3.2.5 on 2022-01-16 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220116_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img_270',
            new_name='img_small',
        ),
    ]