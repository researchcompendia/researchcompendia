from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Article


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

    """
    # BROKEN this causes issue 74 ImproperlyConfigured: No URL to redirect to during a compendia
    def save(self):
        article = super(ArticleUpdateForm, self).save(commit=False)
        article.save()
        article.contributors.clear()
        for user in self.cleaned_data.get('contributors', []):
            Contributor.objects.create(article=article, user=user)
    """

    class Meta:
        model = Article
        fields = (
            'status',
            'compendium_type',
            'title',
            'authors_text',
            'article_url',
            'doi',
            'journal',
            'code_data_abstract',
            'code_archive_file',
            'data_archive_file',
            'month',
            'year',
            'pages',
            'volume',
            'number',
            'article_file',
            'content_license',
            'code_license',
            'primary_research_field',
            'secondary_research_field',
            'notes_for_staff',
            'article_tags'
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
        # NOTE: I had a crispy Layout, but it kept failing on save and I need to troubleshoot if we want to use Layout

    class Meta:
        model = Article
        fields = (
            'status',
            'compendium_type',
            'title',
            'authors_text',
            'article_url',
            'doi',
            'journal',
            'code_data_abstract',
            'code_archive_file',
            'data_archive_file',
            'month',
            'year',
            'pages',
            'volume',
            'number',
            'article_file',
            'content_license',
            'code_license',
            'primary_research_field',
            'secondary_research_field',
            'notes_for_staff',
            'article_tags',
        )
