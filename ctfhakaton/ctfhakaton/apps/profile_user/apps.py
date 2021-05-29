from django.apps import AppConfig


class ProfileUserConfig(AppConfig):
    name = 'profile_user'
    verbose_name = "Профили пользователей"  # А здесь, имя которое необходимо отобразить в админке
    default_auto_field = 'django.db.models.AutoField'