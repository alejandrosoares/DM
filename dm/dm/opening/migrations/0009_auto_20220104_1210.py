# Generated by Django 3.2.5 on 2022-01-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opening', '0008_auto_20220104_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opening',
            name='str_schedule',
        ),
        migrations.AddField(
            model_name='opening',
            name='str_schedules',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Schedules'),
        ),
    ]