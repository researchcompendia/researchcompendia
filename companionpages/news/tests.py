import datetime

from django.test import TestCase
from django.utils import timezone

from .models import News

def create_news(newsbrief, offset):
    """Creates news offset by number of days"""
    return News(newsbrief, publication_date=timezone.now() + datetime.timedelta(days=offset))

class NewsTest(TestCase):

    def test_not_published(self):
        """
        Future newsbriefs should not show as published
        """
        newsbrief = create_news('Future news', offset=1)
        self.assertFalse(newsbrief.published(),
                msg="future news should not show as published")

    def test_published(self):
        """
        Past newsbriefs should show as published
        """
        newsbrief = create_news('Old news', offset=-1)
        self.assertTrue(newsbrief.published(), msg="old news should show as published")

    def test_breaking_news_published(self):
        """
        Immediate newsbriefs should be published
        """
        newsbrief = create_news('Breaking news', offset=0)
        self.assertTrue(newsbrief.published(),
                msg="Breaking news should show as published")

