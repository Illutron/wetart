from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    # url(r'^p4w/', include('p4w.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^a/', include(admin.site.urls)),
)


# Static serving
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        (r'^m/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    )
