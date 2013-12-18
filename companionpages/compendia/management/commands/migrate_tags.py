import logging
from compendia.management.base import BaseArticleCommand
from compendia.models import Article


logger = logging.getLogger(__name__)


class Command(BaseArticleCommand):

    def handle_all(self):
        logger.info('migrating tags for all unmigrated articles')
        articles = Article.objects.filter(tags__isnull=False).exclude(tags__name__in=['migrated'])
        self.handle_queryset(articles)

    def handle_status(self, status):
        logger.info('checking downloads for unmigrated selected status %s', status)
        articles = Article.objects.filter(tags__isnull=False, status=status).exclude(tags__name__in=['migrated'])
        self.handle_queryset(articles)

    def handle_selected(self, ids):
        logger.info('migrating tags for selected unmigrated articles %s', ids)
        articles = Article.objects.filter(tags__isnull=False, id__in=ids).exclude(tags__name__in=['migrated'])
        self.handle_queryset(articles)

    def handle_queryset(self, queryset):
        logger.info('migrating %s results', len(queryset))
        for article in queryset:
            self.migrate_article(article)

    def migrate_article(self, article):
        """ copy names from tags to article_tags and mark tags as migrated
        """
        logger.info('migrating article %s', article.id)
        tags = article.tags.all()
        for t in tags:
            logger.info('adding %s', t.name)

            article.article_tags.add(t.name)
        article.tags.add('migrated')
        logger.info('migrated %s', article.id)
