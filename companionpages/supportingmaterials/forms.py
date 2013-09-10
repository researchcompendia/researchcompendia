from django import forms
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render, render_to_response

from .models import CompanionArticle

class CompanionForm(ModelForm):
	class Meta:
		model = CompanionArticle
        fields = ['corresponding_author', 'title', 'abstract','document', 'article_url']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()


def search_form(request):
    return render(request, 'create.html')
        

def handle_uploaded_file(request):
    """ stub """
    # maybe this didn't get checked in yet?
    pass


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
