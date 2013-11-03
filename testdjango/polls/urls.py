__author__ = 'wencc'
from django.conf.urls import patterns
from django.conf.urls import url

from polls import  views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
)
