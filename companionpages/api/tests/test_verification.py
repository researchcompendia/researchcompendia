from django.http import Http404
from django.test import TestCase

from rest_framework.test import APIRequestFactory
from api import views


class VerificationTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_404(self):
        """ Requests for non-existent Articles should get 404"""
        get = self.factory.get('/verification/999999/')
        post = self.factory.post('/verification/999999/')
        v = views.VerificationList()
        with self.assertRaises(Http404):
            v.get(get, 9999)
        with self.assertRaises(Http404):
            v.get(post, 9999)
