#coding:utf-8
from django.conf.urls import url

from . import views
from hello.views import *

urlpatterns = [
    url('time/$', current_datetime),
    url('html', index),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    #/eg params/?p1=china&p2=2012  测试参数
    url(r'^params/$', helloParams),
    #eg hi/2 测试后缀参数传递
    url(r'^hi/(.+)/$', hi),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # new style
    #url('^view/$', views.DetailView.as_view(), name='index'),
    #url('^vote/$', vote(1)),
]