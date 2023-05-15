# Generated by Django 3.2.11 on 2023-05-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='enable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='normalized_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.SmallIntegerField(null=True),
        ),
    ]
