import logging

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from haystack.forms import FacetedSearchForm
from haystack.query import SQ

from .models import Article
from . import choices

logger = logging.getLogger('researchcompendia.compendia')


class ArticleFacetedSearchForm(FacetedSearchForm):
    compendium_type = forms.MultipleChoiceField(required=False, choices=choices.ENTRY_TYPES)
    primary_research_field = forms.MultipleChoiceField(required=False, choices=choices.RESEARCH_FIELDS)

    def __init__(self, *args, **kwargs):
        super(ArticleFacetedSearchForm, self).__init__(*args, **kwargs)
        self.query_dict = args[0]
        self.compendium_types = self.query_dict.getlist('compendium_type')
        self.research_fields = self.query_dict.getlist('primary_research_field')
        logger.debug('compendium_types %s', self.compendium_types)
        logger.debug('research_fields %s', self.research_fields)

    def search(self):
        sqs = super(ArticleFacetedSearchForm, self).search()

        if len(self.compendium_types) > 0 or len(self.research_fields) > 0:
            sq = SQ()
            for compendium_type in self.compendium_types:
                sq.add(SQ(compendium_type=compendium_type), SQ.OR)
            for research_field in self.research_fields:
                sq.add(SQ(primary_research_field=research_field), SQ.OR)
            return sqs.filter(sq)
        # otherwise just pass through
        return sqs


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
            'article_file',
            'lecture_notes_archive_file',
            'homework_archive_file',
            'solution_archive_file',
            'book_file',
            'month',
            'year',
            'pages',
            'volume',
            'number',
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
            'article_file',
            'lecture_notes_archive_file',
            'homework_archive_file',
            'solution_archive_file',
            'book_file',
            'month',
            'year',
            'pages',
            'volume',
            'number',
            'content_license',
            'code_license',
            'primary_research_field',
            'secondary_research_field',
            'notes_for_staff',
            'article_tags',
        )
