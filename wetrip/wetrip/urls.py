from django.conf.urls import patterns, url#include,
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'wetrip.views.home.index', name='home'),
    url(r'^home/add_info/$','wetrip.views.home.add_info'),
    url(r'^upload$','wetrip.views.upload.upload_image'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',  
        {'document_root': settings.STATIC_ROOT}),
    url(r'^pictures/(?P<path>.*)$','django.views.static.serve',  
        {'document_root': settings.MEDIA_ROOT}),
    # url(r'^wetrip/', include('wetrip.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
