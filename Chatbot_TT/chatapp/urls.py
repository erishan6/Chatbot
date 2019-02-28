from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'), # index page
	path('bot/', views.bot, name ='bot'), #chatbot page
]