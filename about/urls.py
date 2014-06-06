from django.conf.urls import patterns, url
from about import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tools/', views.tools, name='index'),
    url(r'^cv/', views.cv, name='index'),
    # url(r'^images/', views.images),
    # url(r'^(?P<slug>[\w\-]+)/$', views.post),
)