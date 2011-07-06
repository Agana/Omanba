from django.template import Context, loader
from django.http import HttpResponse
from models import Gh_Vid, Donate,Extras, Article
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def article_list(request, limit=15):
	article_list=Article.objects.all()
	return HttpResponse("You're at news list")

def gh_vid_list(request, limit=15):
	gh_vid_list=Gh_Vid.objects.all()
	return HttpResponse("You're at the video list")

def extras_list(request, limit=15):
	extras_list=Extras.objects.all()
	return HttpResponse("You're at extras list")

def donation_list(request, limit=15):
	donation_list=Donation.objects.all()
	return HttpResponse("You're at the donations list")

def index():
	return HttpResponse("Hi there")
