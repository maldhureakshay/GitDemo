from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User

@receiver(post_save, sender=User, dispatch_uid="user_save")
def user_save(sender, instance, **kwargs):
     print("User Created   ---------------"+instance.user_email)
     