__author__ = 'wencc'
from django.conf.urls import patterns, url

from address_book import views

urlpatterns = patterns('',
                       url(r'^$', views.list_address, name='index'),
)