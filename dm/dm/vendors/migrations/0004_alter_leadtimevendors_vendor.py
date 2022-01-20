# Generated by Django 3.2.5 on 2022-01-18 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_alter_leadtimevendors_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadtimevendors',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_times', to='vendors.vendor'),
        ),
    ]
