# coding:utf-8
from django.conf.urls import url

from views import *


urlpatterns = [
    url('object', queryObject),# 测试输出对象
    url('time/$', current_datetime),
    url('html', queryObject),
    url('query1', query1),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    # eg params/?p1=china&p2=2012  测试参数
    url(r'^params/$', helloParams),
    # eg hi/2 测试后缀参数传递
    url(r'^hi/(.+)/$', hi),
    # ex: /polls/
    url(r'^$', index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
]