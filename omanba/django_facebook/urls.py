from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('',
	
	url(r'^$', 'django_facebook.views.index'),
	url(r'^connect/$', 'django_facebook.views.connect_view'),
)
