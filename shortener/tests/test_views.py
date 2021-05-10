from django.test import TestCase
from ..models import UrlList


class ViewsTestCase(TestCase):
    def test_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        UrlList.objects.create(OriginalUrl="https://google.com", ShortenedUrl="2137")
        obj = UrlList.objects.all().first()
        response = self.client.get('/shorted/' + str(obj.ShortenedUrl))
        self.assertEqual(response.status_code, 301)
        response = self.client.get('/shorted/10/')
        self.assertEqual(response.status_code, 404)
