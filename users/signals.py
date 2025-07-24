from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,UserProfile


@receiver(post_save, sender=User)   #this is using the signals post_save
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)