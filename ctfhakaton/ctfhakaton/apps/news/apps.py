from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = "Новости"  # А здесь, имя которое необходимо отобразить в админке
    default_auto_field = 'django.db.models.AutoField'