# Generated by Django 3.2.5 on 2022-01-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_rename_longlink_publication_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='short_link',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace corto'),
        ),
    ]
