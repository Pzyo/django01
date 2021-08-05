
# 在子类派生的新方法中如何重用父类的功能
# 方式1: 指名道姓调用某一个类下的函数 => 不依赖于继承关系
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def f1(self):
#         print("%s say hello" % self.name)
#
# class Teacher(People):
#     def __init__(self, name, age, sex, level, salary):
#         People.__init__(self, name, age, sex)
#
#         self.level = level
#         self.salary = salary
#
# tech_obj = Teacher('pzyo', 23, 'male', 10, 3000)
# print(tech_obj.__dict__)

# 方式2: super()调用父类提供给自己的方法 => 严格依赖继承关系
#        调用super()会得到一个特殊的对象, 该对象会参照发起属性查找的那个类的mro, 去当前类的父类中找属性
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def f1(self):
#         print("%s say hello" % self.name)
#
# class Teacher(People):
#     def __init__(self, name, age, sex, level, salary):
#         # super(Teacher, self).__init__(name, age, sex)  # python2
#         super().__init__(name, age, sex) # python3写法, 调用的是方法, 自动传入对象
#
#         self.level = level
#         self.salary = salary
#
# print(Teacher.mro())
# tech_obj = Teacher('pzyo', 23, 'male', 10, 3000)
# print(tech_obj.__dict__)


# super()案例
class A:
    def test(self):
        print('from A')
        super().test()  # 参照属性查找发起者的mro, 即C类的mro, 所以会去找B类

class B:
    def test(self):
        print('from B')

class C(A, B):
    pass

obj = C()   # C类是属性查找发起者
obj.test()  # from B