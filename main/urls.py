from django.conf.urls import patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
