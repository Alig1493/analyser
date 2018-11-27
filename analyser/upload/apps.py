from django.apps import AppConfig


class UploadConfig(AppConfig):
    name = 'analyser.upload'

    def ready(self):
        from .signals import (post_save_input_file)

