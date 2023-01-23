from django.apps import AppConfig


class MiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miapp'
    verbose_name = 'Mi primera aplicacion' #Para cambiar el nombre que se muestra en la seccion del administrador

