# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from myway.models import Aluno
from myway.forms import *


def index(request):
    return render(request,'index.html')

def login(request):
	return render(request,'login.html')

def new(request):
	if request.method == 'POST':
		form = AlunoForm(request.POST)
		form.save()
		return HttpResponseRedirect('new')
	else:
		form = AlunoForm()
	context_dict = {'form': form}
	return render(request, 'new.html', context=context_dict)


def login(request):
	form = LoginForm()
	context_dict = {'form': form}
	return render(request, 'clientes/login.html', context=context_dict)	




