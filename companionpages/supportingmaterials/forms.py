from django import forms

from .models import Article
from .models import SupportingMaterial


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['site_owner', 'status', 'status_changed', 'storage_url', 'legacy_id', ]


class SupportingMaterialForm(forms.ModelForm):

    class Meta:
        model = SupportingMaterial
        exclude = ['article', 'status', 'status_changed', 'storage_url', 'legacy_id', ]
