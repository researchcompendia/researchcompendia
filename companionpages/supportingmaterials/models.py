from django.db import models

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel

from members.models import Member


class CompanionArticle(StatusModel, TimeStampedModel):
    corresponding_author = models.ForeignKey(Member, help_text=u'The primary point of contact')
    # how to represent collaborators? Members? but don't want them to be required to be
    STATUS = Choices('active', 'inactive')
    title = models.CharField(max_length=100, help_text=u'Title of the publication')
    abstract = models.TextField(max_length=500)
    document = models.FileField(upload_to='papers', blank=True)
    article_url = models.URLField(blank=True, help_text=u'URL to the paper.')
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


class SupportingMaterial(StatusModel, TimeStampedModel):
    STATUS = Choices('active', 'inactive')
    companion_article = models.ForeignKey(CompanionArticle)
    name = models.CharField(max_length=100)
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=1000, blank=True)
    materials_url = models.URLField(blank=True, help_text=u'URL to the supporting material. For example, '
                                                          u'if this is source code, this would be a url '
                                                          u'to to the code repository.')

    def __unicode__(self):
        return self.name
