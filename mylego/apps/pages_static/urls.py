__author__ = 'kasia'

from django.conf.urls import patterns, url

urlpatterns = patterns('mylego.apps.pages_static.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^contact$', 'contact', name='contact'),
                       url(r'^construction$', 'construction', name='construction'),
                       )