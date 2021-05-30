from django.apps import AppConfig


class CaseConfig(AppConfig):
    name = 'hackathon'
    verbose_name = "Хакатон"  # А здесь, имя которое необходимо отобразить в админке
    default_auto_field = 'django.db.models.AutoField'
