# Generated by Django 3.2.11 on 2023-06-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_brand_name'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['enable'], name='category_enable_idx'),
        ),
    ]
