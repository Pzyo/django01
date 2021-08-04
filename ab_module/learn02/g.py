
# 单继承背景下的属性查找
# 示范一:
# class Foo(object):
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()  # Foo.f2  Bar.f1

# 示范二:
# class Foo(object):
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         Foo.f1(self)  # 调用当前类中的f1
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()  # Foo.f2  Foo.f1

# 示范三:
class Foo(object):
    def __f1(self):  # _Foo_f1
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1()  # self._Foo_f1  # 调用当前类中的f1

class Bar(Foo):
    def f1(self):
        print('Bar.f1')

obj = Bar()
obj.f2()  # Foo.f2  Foo.f1