
# 装饰器是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象
# 添加新功能的可调用对象

# print(property)  # <class 'property'>

# property是一个装饰器, 是用来绑定给对象的方法伪造成一个数据属性

# 案例一
# class People:
#     """
#     计算成人的BMI体质指数
#     """
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     # 定义函数的原因:
#     # 1. 从bmi的公式上看, bmi是通过触发功能计算得到的
#     # 2. bmi是随着身高、体重变化而变化的, 不是一个固定的值
#     #    说白了, 每次都是需要临时计算得到的
#
#     # 但是bmi听起来更像是一个数据属性, 而非功能
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# obj1 = People('pzyo', 1.7, 75)
# print(obj1.bmi)

# 案例二
# class People:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, val):
#         if type(val) is not str:
#             print('必须传入str类型')
#             return
#         self.__name = val
#
#     def del_name(self):
#         print('不让删除')
#         # del self.__name
#
    # name = property(get_name, set_name, del_name)
#
#
# obj1 = People('pzyo')
# print(obj1.name)
# obj1.name = 'tom'
# print(obj1.name)
# del obj1.name

# 案例三
class People:
    def __init__(self, name):
        self.__name = name

    @property  # name = property(name)
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if type(val) is not str:
            print('必须传入str类型')
            return
        self.__name = val

    @name.deleter
    def name(self):
        print('不让删除')
        # del self.__name


obj1 = People('pzyo')
print(obj1.name)
obj1.name = 'tom'
print(obj1.name)
del obj1.name