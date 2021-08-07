
# 1. 什么是内置方法
# 定义在类内部, 以__开头, 以__结尾的方法
# 特点: 在某种情况下 自动 触发

# 2. 为何用内置方法?
# 为了定制化我们的类or对象

# 3. 如何使用内置方法
# __str__: 在打印对象时会自动触发, 然后将返回值(必须是字符串类型)当做本次打印的结果
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         # print('运行了')
#         return '<%s:%s>' % (self.name, self.age)
#
# obj = People('pzyo', 23)
#
# # obj.__str__()
# print(obj)  # <pzyo:23>
#
# obj1 = int(10)
# print(obj1)  # 10

# __del__: 在清理对象时触发, 会先执行该方法, 再清理
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.x = open('a.py', mode='w')

    def __del__(self):
        # print('run')
        # 发起系统调用, 告诉操作系统回收相关的系统资源
        self.x.close()

obj = People('pzyo', 23)
del obj
print('======>')
