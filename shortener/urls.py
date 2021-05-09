from django.urls import path
from .views import url_redirect, home

app_name = 'products'
urlpatterns = [
    path('', home, name='Home'),
    path('shorted/<int:id>/', url_redirect, name='redirect'),
]