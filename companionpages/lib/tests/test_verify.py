# -*- coding: utf-8 -*-
from django.test import TestCase

from lib import verify

#  flake8: noqa

class VerifyTests(TestCase):

    def test_zip_basename(self):
        name = verify.get_zip_basename('abc')
        assert name == 'abc'
        name = verify.get_zip_basename('abc.zip')
        assert name == 'abc'

    def test_validate_request(self):
        status, reason = verify.validate({})
        assert status is False
        assert reason == 'missing information in request'

        status, reason = verify.validate({'id': '123'})
        assert status is False
        assert reason == 'missing information in request'

        status, reason = verify.validate({'path_to_target': 'target'})
        assert status is False
        assert reason == 'missing information in request'

        status, reason = verify.validate({'id': '123', 'path_to_target': 'not a file'})
        assert status is False
        assert reason == 'target is not a zipfile'
