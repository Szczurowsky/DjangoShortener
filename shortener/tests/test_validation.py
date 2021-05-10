from django.test import TestCase
from ..forms import ShortUrlForm
from ..models import UrlList

class ValidationTestCase(TestCase):
    def test_validation(self):
        # With valid url
        form_data = {'url': 'https://google.com'}
        form = ShortUrlForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
        # With empty url
        form_data = {'url': None}
        form = ShortUrlForm(data=form_data)
        print()
        self.assertEqual(form.is_valid(), False)
        # With existing url
        UrlList.objects.create(OriginalUrl='https://google.com', ShortenedUrl='2137')
        form_data = {'url': 'https://google.com'}
        form = ShortUrlForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        # With malformed url
        form_data = {'url': 'httpse://google.com'}
        form = ShortUrlForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        form_data = {'url': 'google.com'}
        form = ShortUrlForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        form_data = {'url': 'http:/google.com'}
        form = ShortUrlForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
