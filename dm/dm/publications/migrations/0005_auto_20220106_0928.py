# Generated by Django 3.2.5 on 2022-01-06 12:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_auto_20220106_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='code',
            field=models.CharField(max_length=40, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(error_messages={'unique': 'Ya existe una publicación con este nombre.'}, max_length=50, unique=True, verbose_name='Publicacion'),
        ),
    ]
