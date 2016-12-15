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
from django.template import loader
from .models import Question

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello,World</h1")


def ya(request):
    return HttpResponse("hello,yahier")


def gallery(request):
    t = get_template('templates/gallery.html')
    html = t.render(Context())
    return HttpResponse(html)


def html(request):
    return render_to_response('test.html')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hello1(request,num):
    try:
        num = int(num)
    except ValueError:
        raise Http404()
    return HttpResponse("hello,hello1")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))