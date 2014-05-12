from haystack import indexes

from models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    authors_text = indexes.CharField(model_attr='authors_text')
    title = indexes.CharField(model_attr='title')
    code_data_abstract = indexes.CharField(model_attr='code_data_abstract')
    compendium_type = indexes.CharField(model_attr='compendium_type', faceted=True)
    primary_research_field = indexes.CharField(model_attr='primary_research_field', faceted=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """ search over all active articles """
        return self.get_model().objects.filter(status__iexact=Article.STATUS.active)
