"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.http import HttpResponse #import HttpResponse

from hr.views import users,view_home

'''
def users(request):
	#return "Heloo firefox"
	#return HttpResponse("Hello firefox")#it will only work after importing HttpResponse
	return HttpResponse("<h1>Hello firefox</h1>")
	#it is not a good practice to handle all html here
	'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_users/',users),#here get_users is link and users is the function
    url(r'^home/',view_home),
]
