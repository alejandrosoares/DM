# Generated by Django 3.2.11 on 2023-05-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230510_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='load_img',
        ),
        migrations.AddField(
            model_name='product',
            name='optimize_image',
            field=models.BooleanField(default=False),
        ),
    ]