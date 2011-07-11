from django.template import Context, loader
from django.http import HttpResponse
from models import *
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def article_list(request, limit=15):
	article_list=Article.objects.all()
	type_news = Article(article_type='News')
	type_politics = Article(article_type='Politics')
	type_lifestyle = Article(article_type='Lifestyle')
	type_sports = Article(article_type='Sports')
	t = loader.get_template('omanba/articlelist.html')
	c = Context({'article_list':article_list,'user':str(request.user), 'type_news':type_news, 'type_politics':type_politics, 'type_lifestyle':type_lifestyle, 'type_sports':type_sports})
	return HttpResponse(t.render(c))

# Lists for each article type

def news_list(request, limit=15):
	news_items=Article.objects.filter(article_type='news').order_by('-date_created')
	return render_to_response('omanba/newslist.html', {'news_items': news_items})

def sports_list(request, limit=15):
	sports_items=Article.objects.filter(article_type='sports').order_by('-date_created')
	return render_to_response('omanba/sportslist.html', {'sports_items': sports_items})

def lifestyle_list(request, limit=15):
	lifestyle_items=Article.objects.filter(article_type='lifestyle').order_by('-date_created')
	return render_to_response('omanba/lifestylelist.html', {'lifestyle_items': lifestyle_items})

def politics_list(request, limit=15):
	politics_items=Article.objects.filter(article_type='politics').order_by('-date_created')
	return render_to_response('omanba/politicslist.html', {'politics_items': politics_items})

def gh_vid_list(request, limit=15):
	gh_vid_items=Gh_Vid.objects.all().order_by('-date_added')
	return render_to_response('omanba/videolist.html', {'gh_vid_items': gh_vid_items})

def donation_list(request, limit=15):
	donation_items=Donation.objects.all().order_by('-date_project_added')
	return render_to_response('omanba/donationlist.html', {'donation_items': donation_items})


# Details for each article type

def news_detail(request, id, limit=15):
	news_detail=Article.objects.filter(article_type='news', id=id)
	return render_to_response('omanba/newsdetail.html', {'news_detail': news_detail})

def sports_detail(request, id, limit=15):
	sports_detail=Article.objects.filter(article_type='sports', id=id)
	return render_to_response('omanba/sportsdetail.html', {'sports_detail': sports_detail})

def lifestyle_detail(request, id, limit=15):
	lifestyle_detail=Article.objects.filter(article_type='lifestyle', id=id)
	return render_to_response('omanba/lifestyledetail.html', {'lifestyle_detail': lifestyle_detail})

def politics_detail(request, id, limit=15):
	politics_detail=Article.objects.filter(article_type='politics', id=id)
	return render_to_response('omanba/politicsdetail.html', {'politics_detail': politics_detail})

def gh_vid_detail(request, id, limit=15):
	gh_vid_detail=Gh_Vid.objects.filter(id=id)
	return render_to_response('omanba/videodetail.html', {'gh_vid_detail': gh_vid_detail})

def donation_detail(request, id, limit=15):
	donation_detail=Donation.objects.filter(id=id)
	return render_to_response('omanba/donationdetail.html', {'donation_detail': donation_detail})
#converting the video


# Home Page
def index(request):
	t = loader.get_template('omanba/index.html')
	c = Context({'article_list':article_list,'user':str(request.user)})
	return HttpResponse(t.render(c))
	return HttpResponse("Hi there")
