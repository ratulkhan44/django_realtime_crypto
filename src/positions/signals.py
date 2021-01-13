from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Test


# @receiver(post_save, sender=Test)
# def set_codes(sender, instance, created, *args, **kwargs):
#     if created:
#         create_all_codes()
