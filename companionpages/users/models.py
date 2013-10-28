# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class User(AbstractUser):

    public_name = models.CharField(max_length=150, blank=True, verbose_name=_(u'Public Name'), help_text=_(u'Publically displayed name'))
    byline = models.CharField(max_length=150, blank=True, verbose_name=_(u'Byline'),  help_text=_(u'A short description for your profile'))
    biography = models.TextField(max_length=400, blank=True, verbose_name=_(u'Biography'))

    def __unicode__(self):
        return self.email
