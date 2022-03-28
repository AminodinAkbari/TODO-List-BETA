from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
	if request.user.is_authenticated:
		return redirect('/')
	form = Loginforms(request.POST or None)
	register_form = Registerforms(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request ,username = username , password = password)
		if user is not None:
			login(request , user)
			return redirect('/')
	if register_form.is_valid():
		print('register_is valid')
		username = register_form.cleaned_data.get('username')
		password = register_form.cleaned_data.get('password')
		User.objects.create_user(username = username , password = password)
		user = authenticate(request ,username = username , password = password)
		if user is not None:
			login(request , user)
			return redirect('/')

	context = {
	'form':form,
	'register_form':register_form
	}
	return render(request , 'dist/index.html' , context)
