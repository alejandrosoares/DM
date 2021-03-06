# Generated by Django 3.2.5 on 2022-01-08 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.SmallIntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')], error_messages={'unique': 'Ya existe este día.'}, unique=True, verbose_name='Day')),
                ('str_schedules', models.CharField(blank=True, max_length=36, null=True, verbose_name='Schedules')),
                ('closed', models.BooleanField(default=False, verbose_name='Closed')),
            ],
            options={
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(choices=[('8', '8'), ('8:30', '8:30'), ('9', '9'), ('9:30', '9:30'), ('10', '10'), ('10:30', '10:30'), ('11', '11'), ('11:30', '11:30'), ('12', '12'), ('12:30', '12:30'), ('13', '13'), ('13:30', '13:30'), ('14', '14'), ('14:30', '14:30'), ('15', '15'), ('15:30', '15:30'), ('16', '16'), ('16:30', '16:30'), ('17', '17'), ('17:30', '17:30'), ('18', '18'), ('18:30', '18:30'), ('19', '19'), ('19:30', '19:30'), ('20', '20'), ('20:30', '20:30'), ('21', '21'), ('21:30', '21:30')], max_length=5, verbose_name='Start')),
                ('end', models.CharField(choices=[('8', '8'), ('8:30', '8:30'), ('9', '9'), ('9:30', '9:30'), ('10', '10'), ('10:30', '10:30'), ('11', '11'), ('11:30', '11:30'), ('12', '12'), ('12:30', '12:30'), ('13', '13'), ('13:30', '13:30'), ('14', '14'), ('14:30', '14:30'), ('15', '15'), ('15:30', '15:30'), ('16', '16'), ('16:30', '16:30'), ('17', '17'), ('17:30', '17:30'), ('18', '18'), ('18:30', '18:30'), ('19', '19'), ('19:30', '19:30'), ('20', '20'), ('20:30', '20:30'), ('21', '21'), ('21:30', '21:30')], max_length=5, verbose_name='End')),
                ('order', models.SmallIntegerField(blank=True, verbose_name='Order')),
                ('opening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='opening.opening')),
            ],
        ),
    ]
