from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('temp/', views.temp, name='temp'),
	path('bot/', views.bot, name ='bot'),
]