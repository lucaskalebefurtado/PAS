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



def index(request):
    return render(request,'index.html')

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			matricula = form.cleaned_data['username']
			senha = form.cleaned_data['password']
			user = authenticate(username=matricula,
			password=senha)

			if user is not None:
				LoginForm(request, user)
				return HttpResponseRedirect('restrita.html')
	else:
		form = LoginForm()
	context_dict = {'form': form}
	return render(request, 'login.html', context=context_dict)




@login_required
def restricted_area(request):
	return render(request, 'restrita.html')

@login_required
def fluxograma(request):
	return render(request,'fluxograma.html')


def cadastro(request):
	if request.method == 'POST':
		form = AlunoForm(request.POST)

		if form.is_valid():
			matricula = form.cleaned_data['username']
			senha = form.cleaned_data['password']
			User.objects.create_user (matricula, password=senha)

			return HttpResponseRedirect('/index')

	else:
		form = AlunoForm()
	context_dict = {'form': form}
	return render(request, 'cadastro.html', context=context_dict)





