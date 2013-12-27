#coding=utf8
from django.conf.urls import patterns, url,include
from django.conf import settings
from django.contrib.auth.views import login,logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('wetrip.views',
    # Examples:
    url(r'^$', 'home.index', name='home'),
    url(r'^delete/$', 'home.delete'),        
    url(r'^upload$','upload.upload_image'),    
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$','django.views.static.serve',  
        {'document_root': settings.STATIC_ROOT}),
    url(r'^travel/(?P<path>.*)$','django.views.static.serve',  
        {'document_root': settings.MEDIA_ROOT}),
    # url(r'^wetrip/', include('wetrip.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',login,{'template_name':'user/login.html'}),#registragiton/login.html
    url(r'^accounts/logout/$',logout,{'template_name':'user/logout.html'}),#registragiton/logout.html
)