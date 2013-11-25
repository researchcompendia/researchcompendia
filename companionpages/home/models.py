from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Faq(TimeStampedModel):
    # inherits created and modified DateTimeFields fields from TimeStampedModel
    question = models.TextField(max_length=200)
    answer = models.TextField(
        max_length=3000,
        help_text=_(u'The answer to the question can be written in Markdown syntax'))
    index = models.IntegerField(blank=True, null=True, verbose_name=_(u'Question Order'))

    def get_absolute_url(self):
        return reverse('faq', args=(self.id,))

    def __unicode__(self):
        return self.question[:10]

    class Meta(object):
        ordering = ['index']
