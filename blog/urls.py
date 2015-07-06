'''
Created on 3 jul. 2015

@author: ed
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
