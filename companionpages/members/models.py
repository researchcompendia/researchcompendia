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
        user = kwargs['instance']
        # it's stupid to use username for public name, but let it be for now.
        member = Member(user=user, public_name=user.username)
        member.save()


class Member(StatusModel, TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    STATUS = Choices('active', 'inactive')
    public_name = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    byline = models.CharField(max_length=100, blank=True)
    biography = models.TextField(max_length=400, blank=True)

    def get_absolute_url(self):
        return 'profiles_profile_detail', (), {'username': self.user.username}
    get_absolute_url = models.permalink(get_absolute_url)

    def __unicode__(self):
        return self.public_name
