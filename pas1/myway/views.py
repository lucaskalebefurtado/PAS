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

def cadastro(request):
	if request.method == 'POST':
		form = AlunoForm(request.POST)
		form.save()
		return HttpResponseRedirect('login')
	else:
		form = AlunoForm()
	context_dict = {'form': form}
	return render(request, 'cadastro.html', context=context_dict)





