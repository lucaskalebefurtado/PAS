# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request,'myway/index.html')

<<<<<<< HEAD
=======
def login(request):
	return render(request,'myway/login.html')
>>>>>>> e1516ee0f15f09b11bb8ede428e6d85734764a71

