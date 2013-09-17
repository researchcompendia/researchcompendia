import datetime

from django.test import TestCase
from django.utils import timezone

from news import models


def create_news(newsbrief, offset):
    """Creates news offset by number of days"""
    return models.News(newsbrief, publication_date=timezone.now() + datetime.timedelta(days=offset))


class NewsTest(TestCase):

    def test_not_published(self):
        """
        Future newsbriefs should not show as published
        """
        newsbrief = create_news('Future news', offset=1)
        assert not newsbrief.published(), 'future news should not show as published'

    def test_published(self):
        """
        Past newsbriefs should show as published
        """
        newsbrief = create_news('Old news', offset=-1)
        assert newsbrief.published(), 'old news should show as published'

    def test_breaking_news_published(self):
        """
        Immediate newsbriefs should be published
        """
        newsbrief = create_news('Breaking news', offset=0)
        assert newsbrief.published(), 'Breaking news should show as published'
