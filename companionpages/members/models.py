from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager


# I'm not sure I want this to happen this way
# it barfs when creating a superuser during syncdb. so
# one solution is to skip that step and create a superuser
# with createsuperuser. because otherwise I'd like to generate
# member profiles
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """When user is created also create a matching profile."""
    if kwargs['created']:
        user = kwargs['instance']
        # TODO: Defaulting to public name from username, is a privacy violation,
        # what is a better method for handling this?
        member = Member(user=user, public_name=user.username, gravatar_email=user.email)
        member.save()


class Member(StatusModel, TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    STATUS = Choices('active', 'inactive')
    public_name = models.CharField(max_length=20, help_text=_(u'Publically displayed name'))
    website = models.URLField(blank=True)
    byline = models.CharField(max_length=100, blank=True, help_text=_(u'A short description for your profile'))
    biography = models.TextField(max_length=400, blank=True, help_text=_(u'A short biographical description'))
    gravatar_email = models.EmailField(blank=True, help_text=_(u'a private email associated with your gravatar account'))
    tags = TaggableManager(blank=True)

    # TODO: should the permalink for a member be based on their username? This may violate their privacy.
    def get_absolute_url(self):
        return 'profiles_profile_detail', (), {'username': self.user.username}
    get_absolute_url = models.permalink(get_absolute_url)

    def __unicode__(self):
        return self.public_name
