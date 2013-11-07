from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Hidden, Layout, Submit
from crispy_forms.bootstrap import PrependedText

from .models import Article, Contributor


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
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-creation'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.attrs = {'enctype': 'multipart/form-data'}
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            Hidden('doi', ''),
            Hidden('site_owner', '{{ user }}'),
            'title',
            'contributors',
            'code_data_abstract',
            'code_archive_file',
            'data_archive_file',
            'notes_for_staff',
            'primary_research_field',
            'secondary_research_field',
            'tags',
            Field('authorship', type='hidden'),
            Field('related_urls', type='hidden'),
            Field('paper_abstract', type='hidden'),
        )

    def save(self, **kwargs):
        kwargs.update({'commit': False})
        article = super(ArticleForm, self).save(**kwargs)
        article.save()
        for user in self.cleaned_data.get('contributors', []):
            Contributor.objects.create(article=article, user=user)
        # fake excluding our m2m intermediated relationship before
        # calling save_m2m (this assumes we haven't already excluded contributors
        self.exclude.append('contributors');
        self.save_m2m();
        # return exclude back to normal (this assumes we don't want contributors in exclude)
        self.exclude = [x for x in self.exclude if x != 'contributors']

    class Meta:
        model = Article
        # TODO I wonder if exclude is redundant since I don't list these in the layout?
        # WARNING: exclude is munged in save(), look there before you change this
        exclude = ['legacy_id', 'status_changed', ]
        widgets = {
            # TODO this is not DRY but I'm not sure how to include placeholder attr in the crispy layout
            'title': forms.TextInput(attrs={'placeholder': 'Title your compendium.'}),
            'code_data_abstract': forms.Textarea(attrs={'placeholder': 'does not need to match paper abstract'}),
        }
