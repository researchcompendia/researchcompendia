# -*- coding: utf-8 -*-
from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = User

        fields = ("first_name", "last_name", "public_name", "affiliation", "biography", "country")
