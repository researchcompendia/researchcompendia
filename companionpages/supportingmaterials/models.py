from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel

from members.models import Member

from .choices import RESEARCH_FIELDS
from lib.storage import upload_path



class Collaborator(TimeStampedModel):
    member = models.ManyToManyField(
        Member,
        null=True,
        blank=True,
        help_text=_(u'Member account for the collaborator'))
    name = models.CharField(max_length=200, help_text=_(u'The name of a collaborator'))
    coder = models.BooleanField()
    author = models.BooleanField()
    affiliation = models.CharField(max_length=200, help_text=_(u'Collaborator affiliation'), blank=True)
    country = models.CharField(max_length=200, help_text=_(u'Collaborator country'), blank=True)
    author_order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['author_order', 'name']
        verbose_name = _(u'collaborator')
        verbose_name_plural = _(u'collaborators')


class Article(StatusModel, TimeStampedModel):
    def upload_callback(self, filename):
        if self.site_owner is not None:
            pathsegment = self.site_owner.user.username
        else:
            pathsegment = 'articles'
        return upload_path(pathsegment, filename)
 
    site_owner = models.ForeignKey(Member, help_text=_(u'The member who has ownership of the page'), blank=True, null=True)
    collaborators = models.ManyToManyField(Collaborator, blank=True, null=True)
    STATUS = Choices('draft', 'active')
    title = models.CharField(max_length=500, verbose_name=_(u'Article title'))
    abstract = models.TextField(max_length=5000)
    journal = models.CharField(blank=True, max_length=500, verbose_name=_(u'Journal Name'))
    article_url = models.URLField(blank=True, max_length=2000, verbose_name=_(u'Article URL'))
    storage_url = models.URLField(blank=True, max_length=2000)
    article_file = models.FileField(blank=True, upload_to=upload_callback)
    legacy_id = models.IntegerField(blank=True, null=True)
    doi = models.CharField(max_length=2000, verbose_name=_(u'The article DOI'), blank=True)
    primary_research_field = models.CharField(max_length=300, choices=RESEARCH_FIELDS,
                                              verbose_name="Primary research field", blank=True)
    secondary_research_field = models.CharField(max_length=300, choices=RESEARCH_FIELDS,
                                                verbose_name="Secondary research field", blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('researchcompendium', args=(self.id))

    class Meta(object):
        ordering = ['title']
        verbose_name = _(u'compendium')
        verbose_name_plural = _(u'compendia')


class SupportingMaterial(StatusModel, TimeStampedModel):
    def upload_callback(self, filename):
        return upload_path('materials', filename)
 
    STATUS = Choices('draft', 'active')
    article = models.ForeignKey(Article, null=True, blank=True)
    name = models.CharField(max_length=500)
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=5000, blank=True)
    materials_url = models.URLField(blank=True,
                                    max_length=2000,
                                    help_text=_(u'URL to the supporting material. For example, '
                                                u'if this is source code, this would be a url '
                                                u'to to the code repository.'))
    storage_url  = models.URLField(blank=True, max_length=2000)
    materials_file = models.FileField(blank=True, upload_to=upload_callback)

    def __unicode__(self):
        return self.name
