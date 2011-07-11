from django.template import Context, loader
from django.http import HttpResponse
from models import *
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response




def connect_view(request, limit=15):
	connect=FacebookProfileModel.objects.all()
	return render_to_response('facebook/connect.html', {'connect': connect})

def index(request):
	t = loader.get_template('facebook/index.html')
	c = Context({'connect_view':connect_view})
	return HttpResponse(t.render(c))
	return HttpResponse("Hi there")
