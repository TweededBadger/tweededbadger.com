from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from filebrowser.sites import site
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TweededBadger.views.home', name='home'),
    url(r'^$', include('main.urls')),
    url(r'^blog/', include('blog.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
)

print site.storage.location

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() #this serves static files and media files.
    #in case media is not served correctly
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )

