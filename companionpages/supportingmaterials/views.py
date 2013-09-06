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
