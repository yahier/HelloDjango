# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.http import Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello,World HERE IS CHINA</h1")

def ya(request):
    return HttpResponse("hello,yahier")

#怎么输出json格式呢
def people(request):
    return HttpResponse("hello,people啊")

def gallery(request):
    t = get_template('gallery.html')
    html = t.render(Context())
    return HttpResponse(html)


def html2(request):
    return render_to_response('gallery.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


