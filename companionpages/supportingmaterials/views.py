from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import CompanionForm
from .models import CompanionArticle

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


class CompanionArticleListView(generic.ListView):
    model = CompanionArticle
    template_name = 'supportingmaterials/index.html'
    context_object_name = 'companion_article_list'


class CompanionArticleDetailView(generic.DetailView):
    model = CompanionArticle
    template_name = 'supportingmaterials/detail.html'
