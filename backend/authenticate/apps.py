from django.apps import AppConfig


class AuthenticateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticate'
    verbose_name = 'Авторизация'
    verbose_name_plural = 'Авторизации'
