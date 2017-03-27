#coding:utf-8
from django.db import models
from django.utils import timezone
import datetime
#测试发现，文件名不是任意的


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


def save():
    q = Question(question_text="who is bingo", pub_date=timezone.now())
    q.save()

#这些打印没有在控制台，而直接打印在了命令行。、而且运行模块时就运行了这个这些方法，单独运行反而没有效果
def query():
    ques = Question.objects.all()
    for q in ques:
        print(q.question_text)

def query1():
    ques = Question.objects.get(id=2)
    print(ques.question_text)









