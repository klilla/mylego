__author__ = 'kasia'

from django.conf.urls import patterns, url

urlpatterns = patterns('mylego.apps.user_authentication.views',
                       url(r'^login$', 'log_in', name='login'),
                       url(r'^logout$', 'log_out', name='logout'),
                       url(r'^registration$', 'registration', name='registration'),
                       )