from django import forms
from .models import UrlList
import validators


class ShortUrlForm(forms.Form):
    url = forms.CharField(error_messages={'required': 'URL can not be empty'})

    def clean_url(self):
        url = str(self.clean().get('url'))
        if url is None:
            raise forms.ValidationError('URL can not be empty')
        if validators.url(url) is not True:
            raise forms.ValidationError('URL is not valid')
        if UrlList.objects.filter(OriginalUrl=url).count() != 0:
            shortened_url = UrlList.objects.filter(OriginalUrl=url).first()
            raise forms.ValidationError('This url was shortened before: /shorted/' + str(shortened_url.ShortenedUrl))
        return url
