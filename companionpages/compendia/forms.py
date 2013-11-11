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
        self.helper.add_input(Submit('submit', 'Update'))

    def save(self):
        article = super(ArticleUpdateForm, self).save(commit=False)
        article.save()
        article.contributors.clear()
        for user in self.cleaned_data.get('contributors', []):
            Contributor.objects.create(article=article, user=user)

    class Meta:
        model = Article
        fields = (
            'status',
            'site_owner',
            'authors_text',
            'article_url',
            'doi',
            'journal',
            'code_data_abstract',
            'code_archive_file',
            'data_archive_file',
            'related_urls',
            'content_license',
            'code_license',
            'compendium_type',
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

    """
    def save(self):
        article = super(ArticleForm, self).save(commit=False)
        article.save()
        for user in self.cleaned_data.get('contributors', []):
            Contributor.objects.create(article=article, user=user)
    """

    class Meta:
        model = Article
        fields = (
            'site_owner',
            'status',
            'title',
            'authors_text',
            'article_url',
            'doi',
            'journal',
            'code_data_abstract',
            'code_archive_file',
            'data_archive_file',
            'article_file',
            'content_license',
            'code_license',
            'compendium_type',
            'primary_research_field',
            'secondary_research_field',
            'paper_abstract',
            'notes_for_staff',
            'tags',
            # hidden elements
            'site_owner',
            'paper_abstract',
        )
        #widgets = {
            # set this via javascript or allow the user to enter it
            # set all these via javascript
            #'site_owner': forms.MultipleHiddenInput(),
        #}
