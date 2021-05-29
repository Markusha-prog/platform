from django.db import models


class Hackathon(models.Model):
    """ Модель хакатона """
    cover = models.ImageField(verbose_name='Обложка Хакатона', upload_to='hackathon/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(verbose_name='Название хакатона', max_length=100)
    location = models.CharField(verbose_name='Место проведения', max_length=20)
    start_event = models.DateTimeField('Дата начала мероприятия')
    end_event = models.DateTimeField('Дата окончания мероприятия')
    representative_case = models.CharField(verbose_name='Организатор', max_length=100)
    direction = models.CharField(verbose_name='Направление', max_length=100)
    prize_pool = models.IntegerField('Призовой фонд')
    target_audience = models.CharField(verbose_name='Целевая аудитория', max_length=150)
    info_case = models.TextField(verbose_name='Информация о хакатоне')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Хакатон'
        verbose_name_plural = 'Хакатоны'
