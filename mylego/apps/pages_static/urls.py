__author__ = 'kasia'

from django.conf.urls import patterns, url

urlpatterns = patterns('mylego.apps.pages_static.views',
                       url(r'^$', 'index', name='index'),
                       )