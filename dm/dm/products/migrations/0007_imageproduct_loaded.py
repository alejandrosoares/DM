# Generated by Django 3.2.5 on 2022-01-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_load_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageproduct',
            name='loaded',
            field=models.BooleanField(default=False, verbose_name='Loaded'),
        ),
    ]
