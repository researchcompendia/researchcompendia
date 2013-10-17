from django.test import TestCase

from rest_framework.test import APIRequestFactory
from api import views


class DoiTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_missing_params(self):
        """ Tests that missing params return a bad request status """
        request = self.factory.post('/dois', format='json')
        response = views.doi_crossref(request)
        assert response.status_code == 400, 'missing doi should cause http status 400, not %d' % (response.status_code)
