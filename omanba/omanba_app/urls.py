from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'omanba_app.views.index'),
	url(r'^articles/$', 'omanba_app.views.article_list'),
	url(r'^omanba_app/$', 'omanba_app.views.index'),
	url(r'^videolist/$', 'omanba_app.views.gh_vid_list'),
#	url(r'^videodetail(?P<id>\d+)/$', 'omanba_app.views.video_detail'),
	url(r'^donatelist/$', 'omanba_app.views.donation_list'),
#	url(r'^donatedetail(?P<id>\d+)/$', 'omanba_app.views.extras_detail'),
	url(r'^extraslist/$', 'omanba_app.views.extras_list'),
#	url(r'^extrasdetail(?P<id>\d+)/$', 'omanba_app.views.extras_detail'),
)
