from django.db import models

from companionpages.members import Member


class CompanionArticle(models.Model):
    corresponding_author = models.OneToOneField(members.Member, help_text=u'The primary point of contact')
    collaborators = models.ManyToManyField(members.Member, blank=True, help_text=u'Co-authors and collaborators')
    title = models.CharField(max_length=100, help_text=u'Title of the publication')
    abstract = models.TextField(max_length=500)
    document = models.FileField(upload_to='papers', blank=True)
    article_url = models.URLField(blank=True, help_text=u'URL to the paper. For example, if this is a published paper, '
                                                        u'this would be the journal url to the paper.')
    slug = models.SlugField(unique=True, blank=True)


class SupportingMaterial(models.Model):
    materials = models.ForeignKey(CompanionArticle)
    name = models.CharField(max_length=100)
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=1000, blank=True)
    materials_url = models.URLField(blank=True, blank=True, help_text=u'URL to the supporting material. For example, '
                                                                      u'if this is source code, this would be a url '
                                                                      u'to to the code repository.')
