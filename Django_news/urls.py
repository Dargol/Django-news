from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', 'news.views.Front'),
    url(r'^addnews/?$', 'news.views.AddNews')
    # Examples:
    # url(r'^$', 'Django_news.views.home', name='home'),
    # url(r'^Django_news/', include('Django_news.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
