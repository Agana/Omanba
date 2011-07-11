from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def loginView(request):
	if request.method == 'POST':

		user = authenticate(username = request.POST['username'],password = request.POST['password'])
		
		if user is not None:
			if user.is_active:
				loglink = 'Logout'
				login(request, user)
				return HttpResponseRedirect('/omanba/articles')
				
			else:
				return HttpResponse('Your username and password do not match!')
				loglink = 'Login'
		else:
			return HttpResponse('Your account is not registered with us!')
	form = LoginForm()
	
	
	return render_to_response('users/login.html', {'form': form,'logged_in': request.user.is_authenticated()})
@csrf_exempt
def logoutView(request):
	logout(request)
	return render_to_response('users/logout.html')

