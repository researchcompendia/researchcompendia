from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager

from users.models import User
from lib.storage import upload_path
from . import choices


class Article(StatusModel, TimeStampedModel):
    def upload_callback(self, filename):
        return upload_path('articles', filename)

    site_owner = models.ForeignKey(User, verbose_name=_(u'Compendia Owner'))
    contributors = models.ManyToManyField(User, through='Contributor', related_name='contributors',
                                          help_text=_(u'Users who have contributed to this compendium'))
    # TODO: I know this is sloppy, and need advice on a better way to handle it.
    authorship = models.TextField(max_length=500, blank=True, help_text=_(u'Text containing authors as shown in the paper.'))
    STATUS = choices.STATUS
    title = models.CharField(max_length=500, verbose_name=_(u'Title'))
    abstract = models.TextField(max_length=5000, blank=True)
    journal = models.CharField(blank=True, max_length=500, verbose_name=_(u'Journal Name'))
    article_url = models.URLField(blank=True, max_length=2000, verbose_name=_(u'URL'))
    article_file = models.FileField(blank=True, upload_to=upload_callback)
    legacy_id = models.IntegerField(blank=True, null=True, verbose_name=_(u'RunMyCode ID'), help_text=_(u'Only used for old RunMyCode pages'))
    doi = models.CharField(max_length=2000, verbose_name=_(u'DOI'), blank=True)
    primary_research_field = models.CharField(max_length=300, choices=choices.RESEARCH_FIELDS,
                                              verbose_name=_(u'Primary research field'), blank=True)
    secondary_research_field = models.CharField(max_length=300, choices=choices.RESEARCH_FIELDS,
                                                verbose_name=_(u'Secondary research field'), blank=True)
    notes_for_staff = models.TextField(max_length=5000, blank=True, verbose_name=_(u'Notes for staff'),
                                       help_text=_(u'Private notes to the staff for help in creating your research'
                                                   u'compendium, including links to data and code if not uploaded'))
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('compendium', args=(self.id,))

    class Meta(object):
        ordering = ['title']
        verbose_name = _(u'compendium')
        verbose_name_plural = _(u'compendia')


class Contributor(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=(u'Contributing User'))
    article = models.ForeignKey(Article, verbose_name=_(u'Article'))
    role = models.CharField(max_length=50, choices=choices.CONTRIBUTOR_ROLES,
                            verbose_name=_(u'Contributing Role'),
                            blank=True)
    primary = models.BooleanField(verbose_name=_(u'Primary Contributor?'))
    citation_order = models.IntegerField(blank=True, null=True, verbose_name=_(u'Citation Order'))

    def __unicode__(self):
        return '%s contributor for %s' % (self.user, self.article)

    class Meta(object):
        ordering = ['citation_order', 'user']
        verbose_name = _(u'contributor')
        verbose_name_plural = _(u'contributors')


class SupportingMaterial(StatusModel, TimeStampedModel):
    def upload_callback(self, filename):
        return upload_path('materials', filename)

    STATUS = choices.STATUS
    article = models.ForeignKey(Article, verbose_name=(u'Article'))
    name = models.CharField(max_length=100, verbose_name=_(u'Name'), help_text=_(u'Provide a name for the supporting material.'))
    archive_file = models.FileField(upload_to=upload_callback, blank=True, verbose_name=_(u'Archive File'), help_text=_(u'File containing the materials'))
    description = models.TextField(max_length=5000, blank=True)
    materials_url = models.URLField(blank=True,
                                    max_length=2000,
                                    help_text=_(u'URL to the supporting material. For example, '
                                                u'if this is source code, this would be a url '
                                                u'to to the code repository.'))
    description_file = models.FileField(blank=True, upload_to=upload_callback,
                                        verbose_name=_(u'Materials Description'),
                                        help_text=_(u'File containing description of the materials'))
    materials_type = models.CharField(max_length=200, choices=choices.MATERIAL_TYPES)
    tags = TaggableManager()

    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['name']
        verbose_name = _(u'supporting material')
        verbose_name_plural = _(u'supporting materials')
