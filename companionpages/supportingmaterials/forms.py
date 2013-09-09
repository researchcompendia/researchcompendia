from django import forms
from django.forms import ModelForm
from model_utils.models import StatusModel, TimeStampedModel
from model_utils.choices import Choices

from django.db import models
from members.models import Member
from taggit.managers import TaggableManager

class Article(models.Model): # StatusModel, TimeStampedModel):
    corresponding_author = models.ForeignKey(Member, help_text=(u'The primary point of contact'))
    #STATUS=Choices('active', 'inactive')
    title = models.CharField(max_length=100, help_text=(u'Title of the publication'))
    abstract = models.TextField(max_length=500)
    document = models.FileField(upload_to='papers', blank=True)
    article_url = models.URLField(blank=True, help_text=(u'URL to the paper.'))
    #slug = models.SlugField(unique=True)
    #tags = TaggableManager()
    def __unicode__(self):
        return self.title

class CompanionForm(ModelForm):
	class Meta:
		model = Article
        fields = ['corresponding_author', 'title', 'abstract','document', 'article_url']
        
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()