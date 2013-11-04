# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser
# Import the basic Django ORM models library
from django.db import models
from django.utils.translation import ugettext_lazy as _

from json_field import JSONField


# Subclass AbstractUser
class User(AbstractUser):
    # from AbstractUser we have
    # firstname, lastname, email, username

    public_name = models.CharField(max_length=150, blank=True, verbose_name=_(u'Public Name'), help_text=_(u'Publically displayed name'))
    biography = models.TextField(max_length=400, blank=True, verbose_name=_(u'Biography'))
    affiliation = models.CharField(max_length=200, verbose_name=_(u'Affiliation'), blank=True)
    country = models.CharField(max_length=200, verbose_name=_(u'Country'), blank=True)
    urls = JSONField(blank=True, verbose_name=_(u'URLs'))

    def __unicode__(self):
        return self.email
