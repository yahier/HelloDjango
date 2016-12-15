# coding:utf-8
class Card:
    a = 2
    #构造函数，设置了默认值
    def __init__(self, x=4, y=6):
        self.x = x;
        self.y = y;

    def  haha(self):
        return self.x +self.y

    @classmethod
    def jingtai(self):
        return '静态方法不能访问self的属性'

    # “*”表示这个参数是一个元组参数，“**”表示这个字典参数
    # 这个方法的tuple参数 会把后面的后面的字典参数也当作tuple的部分，怎么弄？
    def foo(self, *tupleArg, **dictArg):
        print "tupleArg=", tupleArg  # ()
        print "dictArg=", dictArg  # []

class NumberCrad(Card):
    def _points(self):
        return int(self.x), int(self.y)

     #  子类甚至可以更改父类方法的classmethod
    def jingtai(self):
        return '父类的   静态方法不能访问self的属性'

card = NumberCrad()
myList = ["my1", "my2"]
myDict = {"name": "Tom", "age": 22}
card.foo(myList, myDict )
print(card.jingtai())
card = NumberCrad(1, 3)
print(card._points())
print('str:'+str(card))
print('repr:'+repr(card))

# 内置方法 str ,repr ，format, hash， bool, bytes




