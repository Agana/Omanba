
# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from models import Gh_Vid, Donate,Extras, Article
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def Article_list(request,Show_Article=False):
	Article_list=Article.objects.all()
	print Article_list
	a=loader.get_template('omanba_app/list.html')
	c=Contect({'Article_list':Article_list})


def Article_detail(request,Show_Article=False):
	if Show_Article:
		Show=Article.object.filter(pk=id)
		print Show
def Extra_list(request):
	Extra_list=Extra.objects.all()
return HttpResponse(t.render(c))


def Extra_details(request):

return HttpResponse(t.render(c))

def Donate_detial(request):
return HttpResponse(t.render(c))


def Index(request):
	t = loader.get_template('omanba/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))
	


	
