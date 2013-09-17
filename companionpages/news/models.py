from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class News(TimeStampedModel):
    # inherits created and modified DateTimeFields fields from TimeStampedModel
    newsbrief = models.TextField(max_length=200)
    publication_date = models.DateTimeField('publication_date')

    def published(self):
        return timezone.now() >= self.publication_date
    published.admin_order_field = 'publication_date'
    published.boolean = True
    published.short_description = _(u'Published?')

    def __unicode__(self):
        return self.newsbrief
