from django.conf.urls import patterns, include, url
from articles.models import Article
from articles import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forbars.views.home', name='home'),
    # url(r'^forbars/', include('forbars.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^article/', include('articles.urls', namespace="articles")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'articles.views.index', name='index'),
    url(r'^page/(?P<pagenum>\d+)/$', 'articles.views.index', name='index'),
)
