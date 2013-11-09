from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Article, Contributor


class ArticleUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-update'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.attrs = {'enctype': 'multipart/form-data'}
        self.helper.add_input(Submit('submit', 'Save'))

    def save(self):
        article = super(ArticleUpdateForm, self).save(commit=False)
        # noop

    class Meta:
        model = Article
        fields = (
            'status',
            'contributors',
            'authorship',
            'article_url',
            'doi',
            'journal',
            'code_data_abstract',
            'code_archive_file',
            'data_archive_file',
            'related_urls',
            'primary_research_field',
            'secondary_research_field',
            'notes_for_staff',
            'tags',
            'paper_abstract',
            'article_file',
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
        # NOTE: I had a crispy Layout, but it seemed to have a weird interaction with save().

    def save(self):
        article = super(ArticleForm, self).save(commit=False)
        article.save()
        for user in self.cleaned_data.get('contributors', []):
            Contributor.objects.create(article=article, user=user)

    class Meta:
        model = Article
        fields = (
            'status',
            'title',
            'contributors',
            'article_url',
            'doi',
            'journal',
            'code_data_abstract',
            'code_archive_file',
            'data_archive_file',
            'article_file',
            'primary_research_field',
            'secondary_research_field',
            'notes_for_staff',
            'tags',
            # hidden elements
            'site_owner',
            'authorship',
            'paper_abstract',
            'related_urls',
        )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title your compendium.'}),
            'code_data_abstract': forms.Textarea(attrs={'placeholder': 'does not need to match paper abstract'}),
            'journal': forms.TextInput(attrs={'placeholder': 'if applicable'}),
            # set this via javascript or allow the user to enter it
            'doi': forms.TextInput(attrs={'placeholder': 'if applicable'}),
            # set all these via javascript
            'site_owner': forms.MultipleHiddenInput(),
            'authorship': forms.HiddenInput(),
            'related_urls': forms.HiddenInput(),
            'paper_abstract': forms.HiddenInput(),
        }
