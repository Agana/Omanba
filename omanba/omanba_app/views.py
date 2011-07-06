<<<<<<< HEAD
# Create your views here.
from models import Article,Extras,Gh_Vid,Donate
from django.http import HttpResponds
from django.template import Context,loader
=======
from django.template import Context, loader
from django.http import HttpResponse
from models import Gh_Vid, Donate,Extras, Article
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
>>>>>>> 34fb685c878539a18e830eacc34a76d8712cc3a5

def Article_list(request,Show_Article=False):
	Article_list=Article.objects.all()
	print Article_list
	if Show_Article:
		Show=Article.object.get(pk=id)
		print Show
	a=loader.get_template('omanba_app/list.html')
	c=Contect({'Article_list':Article_list})
def Extra_list(request):
def Extra_details(request):
def Donate_detial(request):
def Index(request):

	
