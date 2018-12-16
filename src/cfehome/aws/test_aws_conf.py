from django.test import TestCase


class AWSConfigTest(TestCase):
    def test_import(self):
        from cfehome.aws.utils import AWS

    def test_valid_expire_hours(self):
        from django.conf import settings
        AWS_OBJECT_DOWNLOAD_HOURS = getattr(settings, 'AWS_OBJECT_DOWNLOAD_HOURS', None)
        self.assertTrue(type(AWS_OBJECT_DOWNLOAD_HOURS) == int)
