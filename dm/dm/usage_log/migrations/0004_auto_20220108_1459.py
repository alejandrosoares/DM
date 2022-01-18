# Generated by Django 3.2.5 on 2022-01-08 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('usage_log', '0003_auto_20220108_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorylog',
            old_name='created',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='productlog',
            old_name='created',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='querieslog',
            old_name='created',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='categorylog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='productlog',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]