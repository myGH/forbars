from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from articles.models import Article
from django.utils import timezone
from articles import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<article_id>\d+)/comment/$', views.comment, name='comment'),
    url(r'^(?P<article_id>\d+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<article_id>\d+)/update/$', views.update, name='update'),
    url(r'^(?P<article_id>\d+)/update_article/$', views.update_article, name='update_article'),
    url(r'^add_article/$', views.add_article, name='add_article'),
)
