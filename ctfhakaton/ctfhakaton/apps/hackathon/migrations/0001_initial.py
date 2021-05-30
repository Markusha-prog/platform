# Generated by Django 3.2.3 on 2021-05-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название хакатона')),
                ('location', models.CharField(max_length=20, verbose_name='Место проведения')),
                ('start_event', models.DateTimeField(auto_now=True, verbose_name='Дата начала мероприятия')),
                ('end_event', models.DateTimeField(auto_now=True, verbose_name='Дата окончания мероприятия')),
                ('representative_case', models.CharField(max_length=100, verbose_name='Организатор')),
                ('direction', models.CharField(max_length=100, verbose_name='Направление')),
                ('prize_pool', models.IntegerField(verbose_name='Призовой фонд')),
                ('target_audience', models.CharField(max_length=150, verbose_name='Целевая аудитория')),
                ('info_case', models.TextField(verbose_name='Информация о хакатоне')),
            ],
            options={
                'verbose_name': 'Хакатон',
                'verbose_name_plural': 'Хакатоны',
            },
        ),
    ]