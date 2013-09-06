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

@receiver(post_save, sender=User.member)
   


def search_form(request):
    return render(request, 'create.html')
        
class SupportingMaterial(StatusModel, TimeStampedModel):
    STATUS = Choices('active', 'inactive')
    #companion_article = models.ForeignKey(CompanionArticle)
    name = models.CharField(max_length=100)
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=1000, blank=True)
    materials_url = models.URLField(blank=True, help_text=_(u'URL to the supporting material. For example, '
                                                            u'if this is source code, this would be a url '
                                                            u'to to the code repository.'))
    tags = TaggableManager()

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
