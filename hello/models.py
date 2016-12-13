#coding:utf-8
from django.db import models

#生成表是用新命令 migrations
class Mysite(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    author = models.CharField(max_length=100)
    num = models.IntegerField(max_length=10)