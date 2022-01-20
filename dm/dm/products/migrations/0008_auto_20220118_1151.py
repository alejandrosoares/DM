# Generated by Django 3.2.5 on 2022-01-18 14:51

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_imageproduct_loaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_small_webp',
            field=models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Small webp'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_small',
            field=models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Small version'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_webp',
            field=models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Original webp'),
        ),
    ]
