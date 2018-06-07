# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def users(request):
	#return "Heloo firefox"
	#return HttpResponse("Hello firefox")#it will only work after importing HttpResponse
	return HttpResponse("<h1>Hello firefox<h1>")

def view_home(request):
	
	# f=open("/home/ERP/hr/templates/home.html")
	# data=f.read()
	# return HttpResponse(data)
	
	return render(request, "home.html")
