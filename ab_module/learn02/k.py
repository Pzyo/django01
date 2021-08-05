
# 一. 绑定方法: 特殊之处在于将调用者本身当做第一个参数自动传入
#     1. 绑定给对象的方法: 调用者是对象, 自动传入的是对象
#     2. 绑定给类的方法: 调用者是类, 自动传入的是类
#        (使用场景: 提供一种新的造对象的方法)
# class Mysql:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     def func(self):
#         print('%s:%s' % (self.ip, self.port))
#
#     @classmethod  # 将下面的函数装饰成绑定给类的方法
#     def from_conf(cls):
#         print(cls)
#         return cls('127.0.0.1', 3306)  # 可以设置成读取另外的配置文件
#
# # obj1 = Mysql('127.0.0.1', 3306)
#
# obj2 = Mysql.from_conf()

# 二. 非绑定方法 -> 静态方法
#     没有绑定给任何人: 调用者可以是类、对象, 没有自动传参的效果

class Mysql:
    def __init__(self, ip, port):
        self.nid = self.create_id()
        self.ip = ip
        self.port = port

    @staticmethod   # 将下述函数装饰成一个静态方法
    def create_id():
        import uuid
        return uuid.uuid4()

    @classmethod
    def f1(cls):
        pass

    def f2(self):
        pass

obj1 = Mysql('127.0.0.1', 3306)

print(Mysql.create_id)  # <function Mysql.create_id at 0x039723D8>
print(obj1.create_id)   # <function Mysql.create_id at 0x039723D8>
print(Mysql.f1)         # <bound method Mysql.f1 of <class '__main__.Mysql'>>
print(obj1.f2)          # <bound method Mysql.f2 of <__main__.Mysql object at 0x0336C030>>

Mysql.create_id()
obj1.create_id()