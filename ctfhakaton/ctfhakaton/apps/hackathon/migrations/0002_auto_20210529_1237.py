# Generated by Django 3.2.3 on 2021-05-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='end_event',
            field=models.DateTimeField(verbose_name='Дата окончания мероприятия'),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='start_event',
            field=models.DateTimeField(verbose_name='Дата начала мероприятия'),
        ),
    ]