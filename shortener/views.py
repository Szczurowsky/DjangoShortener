from django.shortcuts import render, redirect
from random import randint
from .forms import ShortUrlForm
from .models import UrlList


# Create your views here.

def home(request):
    context = {}
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        if not form.is_valid():
            context = {
                'errors': form.errors.values(),
            }
        else:
            short_url = randint(1000000000000000000000000000, 9999999999999999999999999999)
            while UrlList.objects.filter(ShortenedUrl=short_url).count() != 0:
                short_url = randint(1000000000000000000000000000, 9999999999999999999999999999)
            UrlList.objects.create(OriginalUrl=request.POST['url'], ShortenedUrl=short_url)
            context = {
                'errors': form.errors.values(),
                'ShortURL': short_url,
            }
    return render(request, "shortener/home.html", context)


def url_redirect(request, id):
    if UrlList.objects.filter(ShortenedUrl=id).count() != 0:
        found_url = UrlList.objects.filter(ShortenedUrl=id).first()
        return redirect(found_url.OriginalUrl)
    else:
        context = {
            'NotFound': "I'm sorry but we didn't have this URL in our database.",
        }
        return render(request, "shortener/notFound.html", context)


