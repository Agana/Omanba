from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('',
	
	#url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),	
	url(r'^$', 'omanba_app.views.index'),
	url(r'^articles/$', 'omanba_app.views.article_list'),
	url(r'^newslist/$', 'omanba_app.views.news_list'),
	url(r'^newsdetail/(?P<id>\d+)/$', 'omanba_app.views.news_detail'),	
	url(r'^sportslist/$', 'omanba_app.views.sports_list'),
	url(r'^sportsdetail/(?P<id>\d+)/$', 'omanba_app.views.sports_detail'),	
	url(r'^lifestylelist/$', 'omanba_app.views.lifestyle_list'),
	url(r'^lifestyledetail/(?P<id>\d+)/$', 'omanba_app.views.lifestyle_detail'),
	url(r'^politicslist/$', 'omanba_app.views.politics_list'),
	url(r'^politicsdetail/(?P<id>\d+)/$', 'omanba_app.views.politics_detail'),
	url(r'^videolist/$', 'omanba_app.views.gh_vid_list'),
	url(r'^videodetail/(?P<id>\d+)/$', 'omanba_app.views.gh_vid_detail'),
	url(r'^donationlist/$', 'omanba_app.views.donation_list'),
	url(r'^donationdetail/(?P<id>\d+)/$', 'omanba_app.views.donation_detail'),
)
