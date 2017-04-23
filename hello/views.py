# coding:utf-8

from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime
from django.template import loader
from django.views import generic

from models import Choice, Question
from django.shortcuts import get_object_or_404, render
import json
from People import People
from django.utils import timezone


# 返回json数据。并且是查询数据库的结果返回。棒棒的
def getJson(request):
    response_data = {}

    ques = Question.objects.get(id=4)
    response_data['id'] = ques.id
    response_data['message'] = ques.question_text

    # q = Question(question_text="add in views", pub_date=timezone.now())
    # q.save()

    return HttpResponse(json.dumps(response_data), content_type="application/json")


# 将对象当作json返回
def getClassJaon(request):
    return HttpResponse('吃饭啦')


def html(request):
    return render_to_response('test.html')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# 测试参数和异常
def hi(request, num):
    try:
        num = int(num)
    except ValueError:
        raise Http404()
    return HttpResponse("hi " + str(num))


def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# 将数据库数据，查询后，按json格式返回
def query1(request):
    ques = Question.objects.get(id=1)
    response_data = {}
    response_data['yaya'] = ques.question_text
    return HttpResponse(json.dumps(response_data), content_type="application/json")


# 重要的测试
def queryObject(request):
    p = People(12, '北京')
    p.city = 'beijing'
    obj = obj2dict(p)
    return HttpResponse(json.dumps(obj, ensure_ascii=False), content_type="application/json")


def obj2dict(obj):
    if not hasattr(obj, '__dict__'):
        return obj
    res = {}
    for k, v in obj.__dict__.items():
        if k.startswith('-'):
            continue
        if isinstance(v, list):
            ele = [obj2dict(item) for item in v]
        else:
            ele = obj2dict(v)
        res[k] = ele
    return res



# 以下方法没有能成功调用
def gallery(request):
    t = get_template('templates/test.html')
    html = t.render(Context())
    return HttpResponse(html)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'
