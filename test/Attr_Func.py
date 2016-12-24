# coding:utf-8

# 属性 方法 特性 修饰 相关

class Generic:
    pass

generic = Generic()
generic.a = 1;
print(generic.a)

# 创建属性后 又删除.像js了。内部用来存储属性值的是用_dict
del generic.a;
print(generic.a)


# 特性是接触到的新概念 待续