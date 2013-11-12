from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from api import views
from users.models import User


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='firstuser', email='first@example.com', password='fake')

    def test_not_authorized(self):
        """ Tests that an unauthenticed request fails """
        request = self.factory.get('/s3/signatures/?s3_object_name=1', format='json')
        response = views.s3signatures(request)
        assert response.status_code == 401, 'unauthorized attempt should cause http status 401, not %d' % (response.status_code)

    def test_missing_params(self):
        """ Tests that missing params return a bad request status """
        request = self.factory.get('/s3/signatures/', format='json')
        request.user = self.user
        force_authenticate(request, user=self.user)
        response = views.s3signatures(request)
        assert response.status_code == 400, 'missing s3_object_name should cause http status 400, not %d' % (response.status_code)

    def test_success(self):
        request = self.factory.get('/s3/signatures/?s3_object_name=1', format='json')
        request.user = self.user
        force_authenticate(request, user=self.user)
        response = views.s3signatures(request)
        assert response.status_code == 200, 'successful message should return http status 200, not %d' % (response.status_code)
