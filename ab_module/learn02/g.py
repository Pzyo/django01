
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
# class Foo(object):
#     def __f1(self):  # _Foo_f1
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.__f1()  # self._Foo_f1  # 调用当前类中的f1
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()  # Foo.f2  Foo.f1


# 一: 菱形问题介绍与MRO

# class A(object):
#     def test(self):
#         print('from A')
#
#
# class B(A):
#     def test(self):
#         print('from B')
#
#
# class C(A):
#     def test(self):
#         print('from C')
#
#
# class D(B, C):
#     pass
#
# print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# 类以及该类的对象访问属性都是参照该类的mro列表
# 此外跟D继承类的写法有一定关系, D(B, C)与D(C, B)的mro列表是不一样的

# mro列表的三条准则
# 1. 子类会先于父类被检查
# 2. 多个父类会根据它们在列表中的顺序被检查
# 3. 如果对下一个类存在两个合法的选择, 选择第一个父类

# obj = D()
# obj.test()

# 总结: 类相关的属性查找(类名.属性, 该类的对象.属性), 都是参照该类的mro


# 二: 非菱形继承下, 经典类与新式类的属性查找顺序不一样
#     新式类是一个分支一个分支地找下去, 最后才找object
#     而经典类最后不会去找object

# class E:
#     def test(self):
#         print('from E')
#
# class F:
#     def test(self):
#         print('from F')
#
# class B(E):
#     def test(self):
#         print('from B')
#
# class C(F):
#     def test(self):
#         print('from C')
#
# class D:
#     def test(self):
#         print('from D')
#
# class A(B, C, D):
#     def test(self):
#         print('from A')
#
#
# print(A.mro())  # A->B->E->C->F->D->object
# obj = A()
# obj.test()

# 三: 如果多继承是菱形继承, 经典类与新式类的属性查找顺序不一样
#     经典类: 深度优先, 会在检索第一条分支的时候直接条到走到底, 即检索大脑袋(共同的父类)
#     新式类: 广度优先, 会在检索最后一条分支的时候检索大脑

class G:
    def test(self):
        print('from G')

class E(G):
    def test(self):
        print('from E')

class F(G):
    def test(self):
        print('from F')

class B(E):
    def test(self):
        print('from B')

class C(F):
    def test(self):
        print('from C')

class D(G):
    def test(self):
        print('from D')

class A(B, C, D):
    def test(self):
        print('from A')


print(A.mro())
# 检索顺序
# 经典类: A->B->E->G->C->F->D         深度优先
# 新式类: A->B->E->C->F->D->G-object  广度优先

# PS: 经典类只有在python2才会有, 不继承object的类就为经典类; 而python3默认继承object

obj = A()
obj.test()



