from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """ Группы пользователя """
    group = models.CharField('Группа', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Team(models.Model):
    """ Команда участника """
    team_name = models.CharField('Команда', max_length=100, blank=True, null=True)
    team_verification = models.BooleanField(verbose_name='Подтверждение команды', default=False, null=True)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class Tag(models.Model):
    """ Теги пользователя"""
    tag_name = models.CharField('Тег', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Profile(models.Model):
    """ Модель профиля пользователя """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    verification = models.BooleanField(verbose_name='Подтверждение пользователя', default=False, null=True)
    search_team = models.BooleanField(verbose_name='Поиск команды', default=False, null=True)
    photo = models.ImageField(verbose_name='Аватар пользователя', upload_to='users/%Y/%m/%d',
                              default='default_profil.jpg', blank=True, null=True)
    git = models.CharField(verbose_name='Профиль пользователя Git', max_length=100, blank=True, null=True)
    telegram = models.CharField(verbose_name='Профиль пользователя Telegram', max_length=100, blank=True, null=True)
    group_user = models.ForeignKey(Group, on_delete=models.SET_NULL, verbose_name='Группа', null=True)
    team_user = models.ForeignKey(Team, on_delete=models.SET_NULL, verbose_name='Команда', null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги пользователя')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
