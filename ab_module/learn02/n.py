
# 一. 引入:
# 一切都源自于一句话: 一切皆为对象

# 二. 什么是元类
# 元类就是用来实例化产生类的类
# 关系: 元类 --- 实例化 ---> 类(People) --- 实例化 ---> 对象(obj)

# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print('%s:%s' % (self.name, self.age))

# 如何得到对象
# obj = 调用类()
# obj = People('pzyo', 23)

#　如果说类也是对象
# People = 调用类()

# print(type(obj))  # <class '__main__.People'>

# 查看内置的元类:
# 1. type是内置的元类
# 2. 我们用class关键字定义的类以及内置的类都是有元类type实例化产生的
# print(type(People))  # <class 'type'>
# print(type(int))     # <class 'type'>

# 三. class关键字创造类People的步骤
# 类有三大特征：
# 1. 类名
# class_name = "People"
# 2. 类的基类
# class_bases = (object,)
# 3. 执行类体代码拿到类的名称空间
# class_dic = {}
# class_body = """
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# def say(self):
#     print('%s:%s' % (self.name, self.age))
# """
# exec(class_body, {}, class_dic)
# print(class_dic)  # {'__init__': <function __init__ at 0x02BD1540>, 'say': <function say at 0x02BD14F8>}

# 4. 调用元类
# People = type(class_name, class_bases, class_dic)
# print(People)  # <class '__main__.People'>

# 四. 如何自定义元类来控制类的产生

# class Mymeta(type):  # 只有继承了type类的类才是元类
#     #            空对象,"People", (object,), {...}
#     def __init__(self, class_name, class_bases, class_dic):
#         # print('run...')
#         # print(self)
#         # print(x)  # People
#         # print(y)  # ()
#         # print(z)  # {'__module__': '__main__', '__qualname__': 'People', '__init__': <function People.__init__ at 0x030F1588>, 'say': <function People.say at 0x030F1540>}
#         if not class_name.istitle():
#             raise NameError('类名的首字母必须大写')
#         if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
#             raise TypeError('必须有注释, 且注释不能为空')
#
#     #           当前所在类, 调用类时所传入的参数
#     def __new__(cls, *args, **kwargs):
#         # 造Mymeta的对象
#         # print('run111...')
#         # print(cls)    # <class '__main__.Mymeta'>
#         # print(args)   # ('People', (), {'__module__': '__main__', '__qualname__': 'People', '__doc__': '\n    注释\n    ', '__init__': <function People.__init__ at 0x03201618>, 'say': <function People.say at 0x032015D0>})
#         # print(kwargs) # {}
#
#         # return type.__new__(cls, *args, **kwargs)
#         return super().__new__(cls, *args, **kwargs)  # 推荐

# People = Mymeta("People", (object,), {...})
# 调用Mymeta发生的三件事
# 1. 先造一个空对象 => People, 调用Mymeta类内的__new__方法
# 2. 调用Mymeta这个类内的__init__方法, 完成初始化对象的操作
# 3. 返回初始化好的对象

# class People(metaclass=Mymeta):
#     '''
#     注释
#     '''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print('%s:%s' % (self.name, self.age))

# 强调:
# 只要是调用类, 那么会一次调用
# 1. 类内的__new__
# 2. 类内的__init__

# 五. __call__
# class Foo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, *args, **kwargs):
#         print(args)    # (1, 2, 3)
#         print(kwargs)  # {'a': 5, 'b': 6}
#         return 123
#
# obj = Foo(11, 22)
# print(obj)               # 自动调用 obj.__str__
# res = obj(1,2,3,a=5,b=6) # 自动调用 obj.__call__(1,2,3,a=5,b=6)
# print(res)               # 123

# 应用: 如果想让一个对象可以加括号调用, 需要在该对象的类中添加一个方法__call__
# 总结:
# 对象() --> 类内的__call__
# 类() --> 自定义元类内的__call__
# 自定义元类() --> 内置元类的__call__

# 六. 自定义元类控制类的调用 => 类的对象的产生

class Mymeta(type):  # 只有继承了type类的类才是元类
    def __call__(self, *args, **kwargs):
        # print(self)   # <class '__main__.People'>
        # print(args)   # ('pzyo', 23)
        # print(kwargs) # {}

        # 1. Mymeta.__call__函数内会先调用People内的__new__
        people_obj = self.__new__(self)
        # 2. Mymeta.__call__函数内会先调用People内的__init__
        self.__init__(people_obj, *args, **kwargs)
        # 3. Mymeta.__call__函数内会返回一个初始化好的对象
        return people_obj

# 类的产生
# People = Mymeta() => type.__call__  => 干了前面的三件事
# 1. type.__call__函数内会先调用Mymeta内的__new__
# 2. type.__call__函数内会先调用Mymeta内的__init__
# 3. type.__call__函数内会返回一个初始化好的对象
class People(metaclass=Mymeta):
    """注释"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('%s:%s' % (self.name, self.age))

    def __new__(cls, *args, **kwargs):
        # 产生真正的对象
        # return object.__new__(cls)
        return super().__new__(cls, *args, **kwargs)

# 类的调用
obj = People('pzyo', 23)  # => Mymeta.__call__ => 干了三件事
# 1. Mymeta.__call__函数内会先调用People内的__new__
# 2. Mymeta.__call__函数内会先调用People内的__init__
# 3. Mymeta.__call__函数内会返回一个初始化好的对象

print(obj)           # <__main__.People object at 0x03244830>
print(obj.__dict__)  # {'name': 'pzyo', 'age': 23}