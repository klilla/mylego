from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mylego.views.home', name='home'),
                       # url(r'^mylego/', include('mylego.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url(r'^', include("mylego.apps.pages_static.urls")),
                        url(r'^', include("mylego.apps.user_authentication.urls")),
)


