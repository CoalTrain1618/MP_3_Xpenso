from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

#this triggers when user instance is saved. Causing it to check if new use is created,
# then proceeds to create the user profile link.
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Ensures anytime the User is saved, the realting profile is also saved.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)