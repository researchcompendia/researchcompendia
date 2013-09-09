from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager
from django.shortcuts import render
from django.conf.urls.static import static

from members.models import Member
from django.http import HttpResponse
from django.forms import ModelForm
from .forms import UploadFileForm
from .forms import CompanionForm

<<<<<<< HEAD
@receiver(post_save, sender=User.member)
   
=======

class CompanionArticle(StatusModel, TimeStampedModel):
    corresponding_author = models.ForeignKey(Member, help_text=_(u'The primary point of contact'))
    # how to represent collaborators? Members? but don't want them to be required to be
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
>>>>>>> 9e0b123e4dc094ba619854c74cd5a0053e84dc8c


def search_form(request):
    return render(request, 'create.html')
        
class SupportingMaterial(StatusModel, TimeStampedModel):
    STATUS = Choices('active', 'inactive')
<<<<<<< HEAD
    #companion_article = models.ForeignKey(CompanionArticle)
    name = models.CharField(max_length=100)
=======
    companion_article = models.ForeignKey(CompanionArticle)
    name = models.CharField(max_length=500)
>>>>>>> 9e0b123e4dc094ba619854c74cd5a0053e84dc8c
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=5000, blank=True)
    materials_url = models.URLField(blank=True, help_text=_(u'URL to the supporting material. For example, '
                                                            u'if this is source code, this would be a url '
                                                            u'to to the code repository.'))
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.name
        
def upload_file(request):
	UploadFileForm(request.POST)
	if request.method == 'POST':
        	form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
	else:
		form = UploadFileForm()
	return render_to_response('create.html', {'form': form})
