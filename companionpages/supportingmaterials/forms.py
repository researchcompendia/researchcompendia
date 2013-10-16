from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText

from .models import Article, SupportingMaterial


class DoiForm(forms.Form):

    doi = forms.CharField(required=False, label='')

    def __init__(self, *args, **kwargs):
        super(DoiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'doiref'
        self.helper.layout = Layout(
            PrependedText('doi', 'doi:'),
        )


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['site_owner', 'status', 'status_changed', 'storage_url', 'legacy_id', ]


class SupportingMaterialForm(forms.ModelForm):

    class Meta:
        model = SupportingMaterial
        exclude = ['article', 'status', 'status_changed', 'storage_url', 'legacy_id', ]
