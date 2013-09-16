from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager

from members.models import Member


class Collaborator(TimeStampedModel):
    member = models.ForeignKey(Member, null=True, blank=True,
            help_text=_(u'Member account for a collaborator who is also a RunMyCode member'))
    name = models.TextField(max_length=200, help_text=_(u'The name of a collaborator'))
    coder = models.BooleanField()
    author = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['name']
        verbose_name = _(u'collaborator')
        verbose_name_plural = _(u'collaborators')


class CompanionArticle(StatusModel, TimeStampedModel):
    corresponding_author = models.ForeignKey(Member, help_text=_(u'The primary point of contact'))
    collaborators = models.ManyToManyField(Collaborator, blank=True, null=True)

    STATUS = Choices('active', 'inactive')
    title = models.CharField(max_length=500, help_text=_(u'Title of the publication'))
    abstract = models.TextField(max_length=5000)
    document = models.FileField(upload_to='papers', blank=True)
    journal = models.CharField(blank=True, max_length=500, help_text=_(u'Journal Name'))
    article_url = models.URLField(blank=True, help_text=_(u'URL to the paper.'))
    slug = models.SlugField(unique=True)
    tags = TaggableManager(blank=True)
    legacy_id = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rmc_companionpage', args=(self.id) )

    class Meta(object):
        ordering = ['title']
        verbose_name = _(u'companion page')
        verbose_name_plural = _(u'companion pages')


class SupportingMaterial(StatusModel, TimeStampedModel):
    STATUS = Choices('active', 'inactive')
    companion_article = models.ForeignKey(CompanionArticle)
    name = models.CharField(max_length=500)
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=5000, blank=True)
    materials_url = models.URLField(blank=True, help_text=_(u'URL to the supporting material. For example, '
                                                            u'if this is source code, this would be a url '
                                                            u'to to the code repository.'))
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.name

