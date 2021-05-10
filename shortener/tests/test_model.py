from django.test import TestCase
from ..models import UrlList


class SimpleTest(TestCase):
    def test_creating_model(self):
        UrlList.objects.create(OriginalUrl='TestCase1', ShortenedUrl='TestCase2')
        original_url = UrlList.objects.filter(OriginalUrl='TestCase1').first()
        self.assertEqual(original_url.ShortenedUrl, 'TestCase2')