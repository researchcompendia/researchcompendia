from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['site_owner', 'status', 'status_changed', 'storage_url','legacy_id',]
