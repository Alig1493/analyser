from django.db.models.signals import post_save
from django.dispatch import receiver

from analyser.upload.tasks import process_file
from .models import File


@receiver(post_save, sender=File)
def post_save_input_file(sender, instance, **kwargs):
    print("Inside signals")
    process_file(filename=instance.file_field.name)
