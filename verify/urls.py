from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'verify.views.home'),
   )
