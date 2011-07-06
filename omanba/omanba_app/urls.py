from models import News, Sports, Lifestyle, Video, Donate, Politics, Extras
from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'omanba_app.views.home'),
	url(r'^newslistlist/$', 'omanba_app.views.news_list'),
	url(r'^newsdetail(?P<id>\d+)/$', 'omanba_app.views.news_detail'),
	url(r'^sportslist/$', 'omanba_app.views.sports_list'),
	url(r'^sportsdetail(?P<id>\d+)/$', 'omanba_app.views.sports_detail'),
	url(r'^lifestlist/$', 'omanba_app.views.lifestyle_list'),
	url(r'^lifestdetail(?P<id>\d+)/$', 'omanba_app.views.lifestyle_detail'),
	url(r'^poiticslist/$', 'omanba_app.views.politics_list'),
	url(r'^politicsdetail(?P<id>\d+)/$', 'omanba_app.views.politics_detail'),
	url(r'^videolist/$', 'omanba_app.views.video_list'),
	url(r'^videodetail(?P<id>\d+)/$', 'omanba_app.views.video_detail'),
	url(r'^donatelist/$', 'omanba_app.views.extras_list'),
	url(r'^donatedetail(?P<id>\d+)/$', 'omanba_app.views.extras_detail'),
	url(r'^extraslist/$', 'omanba_app.views.extras_list'),
	url(r'^extrasdetail(?P<id>\d+)/$', 'omanba_app.views.extras_detail'),
	url(r'^omanba_app/$', 'omanba_app.views.index'),
	
	
	

