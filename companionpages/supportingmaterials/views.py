<<<<<<< HEAD
# Create your views here.
from django.shortcuts import render
from .forms import CompanionForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def companion(request):
    if request.method == 'POST':
        form = CompanionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = CompanionForm()
    return render(request, 'create.html', {'form': form})
=======
from django.views import generic
from .models import CompanionArticle

class CompanionArticleListView(generic.ListView):
    model = CompanionArticle
    template_name = 'supportingmaterials/index.html'
    context_object_name = 'companion_article_list'
>>>>>>> 9e0b123e4dc094ba619854c74cd5a0053e84dc8c
