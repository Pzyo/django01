

# 1. 什么是继承
# Ⅰ. 继承是一种创建新类的方式, 新建的类可称为子类或派生类, 父类又可称为基类或超类
#     子类会遗传父类的属性
# Ⅱ. 需要注意的是: python支持多继承
#     在python中, 新建的类可以继承一个或多个父类

class Parent1(object):
    x = 111

class Parent2(object):
    pass

class Sub1(Parent1):  # 单继承
    pass

class Sub2(Parent1, Parent2):  # 多继承
    pass

# print(Sub1.__bases__)  # 查看继承的父类 (<class '__main__.Parent1'>,)
# print(Sub2.__bases__)  # (<class '__main__.Parent1'>, <class '__main__.Parent2'>)

# print(Sub1.x)  # 111

# ps1: 在python2中有经典类与新式类之分
# 新式类: 继承了object类的子类, 以及该子类的子类子子类...
# 经典类: 没有继承object类的子类, 以及该子类的子类子子类...
# """
# python2.7版本代码示例
#
# class Foo:  # 经典类, 以及继承了Foo的子类也叫新式类
#     pass
#
# class Bar(object):  # 新式类, 以及继承了Bar的子类也叫新式类
#     pass
# """

# ps2: 在python3中没有继承任何类的, 那么会默认继承object类, 所以python3中所有的类都是新式类
# print(Parent1.__bases__) # (<class 'object'>,)
# print(Parent2.__bases__) # (<class 'object'>,)

# Ⅲ. python的多继承
#     优点: 子类可以同时遗传多个父类的属性, 最大限度地重用代码
#     缺点:
#           a. 违背人的思维习惯: 继承表达的是一种 什么"是"什么 的关系
#           b. 代码可读性会变差
#           c. 不建议使用多继承, 有可能会引发可恶的菱形问题, 扩展性变差,
#           如果真的涉及到一个子类不可避免地要重用多个父类的属性, 应该使用Mixins


# 2. 为何要用继承: 用来解决类与类之间代码冗余问题

# 3. 如何实现继承
# 示范1: 类与类之间存在冗余问题
# class Student(object):
#     school = 'GDSCHOOL'
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def choose_course(self):
#         print('学生%s 正在选课' % self.name)
#
# class Teacher(object):
#     school = 'GDSCHOOL'
#     def __init__(self, name, age, sex, salary, level):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.salary = salary
#         self.level = level
#
#     def score(self):
#         print('老师%s 正在给学生打分' % self.name)

# 示范2: 基于继承解决类与类之间的冗余问题
class GdPeople(object):
    school = 'GDSCHOOL'
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Student(GdPeople):
    def choose_course(self):
        print('学生%s 正在选课' % self.name)

class Teacher(GdPeople):

    def __init__(self, name, age, sex, salary, level):
        # 指名道姓地跟父类GdPeople要__init__
        GdPeople.__init__(self, name, age, sex)  # 方式1
        # super().__init__(name, age, sex)  # 方式2, super()函数是调用父类(超类)的一个方法, 会自动传入self形参

        self.salary = salary
        self.level = level

    def score(self):
        print('老师%s 正在给学生打分' % self.name)