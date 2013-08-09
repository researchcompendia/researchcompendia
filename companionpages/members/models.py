from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """When user is created also create a matching profile."""
    if kwargs['created']:
        Member(user = kwargs['instance']).save()


class Member(StatusModel, TimeStampedModel):
    STATUS = Choices('active', 'inactive')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    public_name = models.CharField(max_length=50)
    website = models.URLField()
    byline = models.CharField(max_length=100)
    biography = models.TextField(max_length=400)

    def __unicode__(self):
        return self.public_name
