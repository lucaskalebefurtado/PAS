# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request,'myway/index.html')

def login(request):
	return render(request,'myway/login.html')


