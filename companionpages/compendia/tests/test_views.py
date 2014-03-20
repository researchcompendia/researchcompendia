from django.test import TestCase
from users.models import User
from compendia import models

#  flake8: noqa

class DetailViewTest(TestCase):
    fixtures = ['articles.json']
    urls = 'urls'


    def test_detail_by_pk(self):
        a = models.Article.objects.get(pk=1)
        print a
        res = self.client.get('/compendia/1/')
        self.assertEqual(res.status_code, 200, "Articles should still be reachable via pk lookup")

    def test_detail_by_year(self):
        res = self.client.get('/compendia/2013.1/')
        self.assertEqual(res.status_code, 200, "Article 1 was created in 2013 and should be found in that year")
        res = self.client.get('/compendia/2014.1/')
        self.assertEqual(res.status_code, 404, "Article 1 was created in 2013, not 2014")
