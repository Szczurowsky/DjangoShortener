from django.db import models
from django.urls import reverse


# Create your models here.
class UrlList(models.Model):
    OriginalUrl = models.CharField(max_length=255)
    ShortenedUrl = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("shortener:redirect", kwargs={"id": self.id})
