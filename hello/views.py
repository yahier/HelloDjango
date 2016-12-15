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
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render


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

#测试参数和异常
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


# 以下方法没有能成功调用
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


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
