import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)

@receiver(post_save,sender=AUTH_USER_MODEL)
def create_user_profile(sender,instace,created,**kwargs):
    if created:
        Profile.objects.create(user=instace)

@receiver(post_save,sender=AUTH_USER_MODEL)
def save_user_profile(sender,instance,created,**kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")