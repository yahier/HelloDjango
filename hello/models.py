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



#可以成功写入英文。但数据提示需要配置这个相关 DEFAULT_INDEX_TABLESPACE
#两个字段都是中文的话，有时成功，有时候不成功

#默认还是不执行了
#test()