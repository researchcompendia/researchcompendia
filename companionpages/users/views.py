# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

from braces.views import LoginRequiredMixin, SelectRelatedMixin

from .forms import UserForm
from .models import User


class UserDetailView(LoginRequiredMixin, SelectRelatedMixin, DetailView):
    model = User
    select_related = ['article__site_owner', 'contributor__user']

    def get_queryset(self):
        queryset = super(UserDetailView, self).get_queryset()
        return queryset.select_related(*self.select_related)


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", args=(self.request.user.id,))


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail", args=(self.request.user.id,))

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    #slug_field = "username"
    #slug_url_kwarg = "username"
