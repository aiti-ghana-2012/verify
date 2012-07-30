from django.conf.urls import patterns, include, url
from django.conf import settings
import dj_simple_sms

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'verifyProject.views.home', name='home'),
    # url(r'^verifyProject/', include('verifyProject.foo.urls')),
    url(r'^verify/', include('verify.urls')),
    url(r'^verify/search/(?P<term>.*?)$', 'verify.views.search'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^nimda/', include(admin.site.urls)),
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root' : settings.STATIC_ROOT,
    }),
    
    url(r'^sms/',include(dj_simple_sms.urls))
    
)
