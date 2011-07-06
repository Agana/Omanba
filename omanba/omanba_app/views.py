<<<<<<< HEAD
# Create your views here.
from models import Article,Extras,Gh_Vid,Donate
from django.http import HttpResponds
from django.template import Context,loader

def Articles(request):
=======
from django.template import Context, loader
from django.http import HttpResponse
from models import Gh_Vid, Donate,Extras
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
>>>>>>> 290c017d9d034ae892d00f3fc8a557fa1730f9db
