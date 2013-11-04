from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
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
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.attrs = {'enctype': 'multipart/form-data'}
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Article
        exclude = ['legacy_id', 'status_changed', ]


class SupportingMaterialForm(forms.ModelForm):

    class Meta:
        model = SupportingMaterial
        exclude = ['article', 'status_changed']
