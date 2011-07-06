from django.template import Context, loader
from django.http import HttpResponse
from models import News, Sports, Lifestyle, Gh_Vid, Donate, Politics, Extras
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def news_list(request, limit=15):
	news_list=News.objects.all()
	HttpResponse("You're at news list")

def index():
	return HttpResponse("Hi there")
