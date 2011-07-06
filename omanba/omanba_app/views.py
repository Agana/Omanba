# Create your views here.
from models import Article,Extras,Gh_Vid,Donate
from django.http import HttpResponds
from django.template import Context,loader

def Articles(request):
