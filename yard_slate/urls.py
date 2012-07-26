from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from yard_slate import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'yard_slate_app.views.index', name='index'),
    url(r'^create', 'yard_slate_app.views.create', name='create'),
    url(r'^view_slate', 'yard_slate_app.views.view_slate', name='view_slate'),
    url(r'^printable_slate', 'yard_slate_app.views.printable_slate', name='print_slate')
    # url(r'^yard_slate/', include('yard_slate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (r'^slate_images/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root' : settings.MEDIA_ROOT,
                             'show_indexes' : True}))