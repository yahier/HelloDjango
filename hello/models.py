#coding:utf-8
from django.db import models
#测试发现，文件名不是任意的


class Mysite(models.Model):
    title = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


#可以成功写入英文。但数据提示需要配置这个相关 DEFAULT_INDEX_TABLESPACE
#两个字段都是中文的话，有时成功，有时候不成功
def test():
   book = Book(name='english', author='who')
   book.save()

test()