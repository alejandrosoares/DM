# Generated by Django 3.2.5 on 2022-01-07 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_brand_name_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Brands'),
        ),
    ]
