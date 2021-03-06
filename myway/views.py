# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from myway.models import Cliente
from myway.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import DEFERRED



def index(request):
    return render(request,'index.html')

def cadastro(request):
	if request.method == 'POST':
		form = AlunoForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			senha = form.cleaned_data['password']
	
			
			User.objects.create_user( username=username, 
			password=senha)

			return HttpResponseRedirect('login.html')

	else:
		form = AlunoForm()
	context_dict = {'form': form}
	return render(request, 'cadastro.html', context=context_dict)

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			senha = form.cleaned_data['password']
			user = authenticate(username=username,
			password=senha)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect('telauser')
	else:
		form = LoginForm()
	context_dict = {'form': form}
	return render(request, 'login.html', context=context_dict)



def fluxograma(request):
	return render(request,'fluxograma.html')




@login_required
def restricted_area(request):
	return render(request, 'restrita.html')

@login_required
def telauser(request):
	return render(request, 'telaUsuario.html')

@login_required
def perfil(request):
	return render(request, 'perfil.html')

@login_required
def editarUser (request):
	if request.method == 'POST':
		form = AlunoForm(data=request.POST, instance=request.user)
		if form.is_valid():
			username = form.cleaned_data['username']
			senha = form.cleaned_data['password']

			User.objects.create_user( username=username, 
			password=senha)
			return HttpResponseRedirect('telauser.html')
	else:
		form = AlunoForm()
		context_dict = {'form': form}
		return render (request, 'editarUser.html', context=context_dict)







