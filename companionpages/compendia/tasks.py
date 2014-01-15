from httplib import responses as status_names
from django.conf import settings

from celery import shared_task
from celery.utils.log import get_task_logger
import requests

from . import models

logger = get_task_logger('researchcompendia.tasks')


@shared_task
def check_all_article_downloads():
    logger.info('checking downloads for all articles')
    articles = models.Article.objects.all()
    check_queryset_downloads(articles)


@shared_task
def check_selected_article_downloads(ids=[]):
    logger.info('checking downloads for selected articles %s', ids)
    articles = models.Article.objects.filter(id__in=ids)
    check_queryset_downloads(articles)


@shared_task
def check_selected_status_article_downloads(status):
    logger.info('checking downloads for selected status %s', status)
    articles = models.Article.objects.filter(status=status)
    check_queryset_downloads(articles)


"""
I don't know if there is a better place for these.
"""


def check_queryset_downloads(queryset):
    for article in queryset:
        check_article_downloads(article)


def check_article_downloads(article):
    """ verify that urls to all files in an Article are still available
    """
    logger.info('checking downloads for article %s', article.id)
    for archive_file, archive_type in [(article.code_archive_file, 'code'), (article.data_archive_file, 'data')]:
        if archive_file != '':
            check_file_availability(archive_file)
        else:
            logger.debug('article %s has no %s archive file', article.id, archive_type)


def check_file_availability(file_field):
    # TODO: should it use the url attribute for FileFields rather than constructing it by hand?
    file_url = settings.S3_URL + file_field.name.lstrip('/')
    logger.debug('checking file %s', file_url)
    try:
        r = requests.head(file_url)
        if not r.ok:
            logger.critical('unavailable file. Status: %s %s URL: %s', r.status_code, status_names[r.status_code], file_url)
    except requests.exception.RequestsException:
        logger.exception('a requests exception occured while trying to access the url: %s', file_url)
    else:
        logger.info('available file. URL: %s', file_url)
