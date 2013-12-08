from django.conf.urls import patterns, url#include,
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'wetrip.views.home.index', name='home'),
    url(r'^upload$','wetrip.views.upload.upload_image'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',  
        {'document_root': "/home/barney/git/wetrip/wetrip/static"}),
    url(r'^pictures/(?P<path>.*)$','django.views.static.serve',  
        {'document_root': "/home/barney/git/wetrip/wetrip/pictures"}),
    # url(r'^wetrip/', include('wetrip.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
