# Generated by Django 3.2.3 on 2021-05-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_hackathon_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_QR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name=models.FileField(blank=True, max_length=254, null=True, upload_to='file_qr/%Y/%m/%d/', verbose_name='Файл QR'))),
            ],
            options={
                'verbose_name': 'Файл QR',
                'verbose_name_plural': 'Файлы QR',
            },
        ),
    ]