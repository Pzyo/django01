
# 反射
# 指的是在程序运行过程中可以 "动态(不见棺材不掉泪)" 获取对象的信息

# 反射的作用

# 比如传入一个对象, 需要用到对象的某个方法或属性, 需要先判断属性或方法是否存在, 需动态获取对象的属性或方法
# 简单说就是想调用某个对象的属性或方法, 但不确定该对象是否有, 所以需要先动态获取, 再进行调用
# class f1:
#     x = 1
#
# def func(obj):
#     if 'x' not in obj.__dict__:  # 非所有对象都能调__dict__
#         return
#     print(obj.x)
#
# func(f1)



# 反射的实现

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s:%s>' % (self.name, self.age))

obj = People('pzyo', 23)

# 假设上部分隐藏, 你看不见

# 实现反射机制的步骤
# 1. 先通过dir, 查看某个对象下可以.出哪些属性
print(dir(obj))

# 2. 可以通过字符串反射到真正的属性(name), 得到属性值
# print(obj.__dict__[dir(obj)[-2]])

# 上面存在的局限性问题是: 1. 非所有对象都有__dict__; 2. name属性不一定对应-2的索引位置

# 四个内置函数使用: 通过字符串来操作属性值
# 1. hasattr()  # 判断某个对象属性的方法是否存在
print(hasattr(obj, 'name')) # True
print(hasattr(obj, 'x'))    # False

# 2. getattr()  # 去获取对象的属性或方法, 如 obj.name
print(getattr(obj, 'name'))  # pzyo

# 3. setattr()  # 赋值属性操作, 如 obj.name = 'tom'
setattr(obj, 'name', 'tom')
print(obj.name)  # tom

# 4. delattr()  # 删除属性, 如 del obj.name
delattr(obj, 'name')
print(hasattr(obj, 'name'))  # False


res1 = getattr(obj, 'say')     # obj.say
res2 = getattr(People, 'say')  # People.say
print(res1)  # <bound method People.say of <__main__.People object at 0x03AB4B50>>
print(res2)  # <function People.say at 0x03AB14F8>

# obj1 = 10
# print(getattr(obj1, 'x', None))  # None
# if hasattr(obj1, 'x'):
#     setattr(obj1, 'x', 111)  # 10.x = 111
# else:
#     pass

class Ftp:
    def put(self):
        print('正在执行上传功能')
    def get(self):
        print('正在执行下载功能')
    def interactive(self):
        method = input('>>>: ').strip()
        if hasattr(self, method):  # 因为不知道用户会输入什么, 所以需要使用反射去判断自己的程序有对应的功能
            getattr(self, method)()
        else:
            print('输入的指令不存在')

obj = Ftp()
obj.interactive()
