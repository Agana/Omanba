from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'omanba_app.views.index'),
	url(r'^articles/$', 'omanba_app.views.article_list'),
	url(r'^newslist/$', 'omanba_app.views.news_list'),
	url(r'^newsdetail/(?P<id>\d+)/$', 'omanba_app.views.news_detail'),	
	url(r'^sportslist/$', 'omanba_app.views.sports_list'),
	url(r'^lifestylelist/$', 'omanba_app.views.lifestyle_list'),
	url(r'^politicslist/$', 'omanba_app.views.politics_list'),
	url(r'^videolist/$', 'omanba_app.views.gh_vid_list'),
#	url(r'^videodetail/(?P<id>\d+)/$', 'omanba_app.views.video_detail'),
	url(r'^donatelist/$', 'omanba_app.views.donation_list'),
#	url(r'^donatedetail/(?P<id>\d+)/$', 'omanba_app.views.extras_detail'),
	url(r'^extraslist/$', 'omanba_app.views.extras_list'),
#	url(r'^extrasdetail/(?P<id>\d+)/$', 'omanba_app.views.extras_detail'),
)
