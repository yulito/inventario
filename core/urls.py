#from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
	path('index', views.index, name='index'),
	path('dispositivo_list', views.dispositivo_list, name='dispositivo_list'),
]	
