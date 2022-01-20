# Generated by Django 3.2.5 on 2022-01-18 13:17

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_img_270_product_img_small'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Original')),
                ('img_small', models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Small version')),
                ('original_webp', models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Original webp')),
                ('img_small_webp', models.ImageField(null=True, upload_to=products.models.upload_img_product, verbose_name='Small webp')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]