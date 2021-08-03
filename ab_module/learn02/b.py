
# 先定义类
# 类是对象相似数据与功能的集合体
# 所以类体中最常见的是变量与函数的定义, 但是其实是可以包含任意其他代码
# 注意: 类体代码是在类定义阶段就会立即执行, 会产生类的名称空间
class Student:
    # 1. 变量的定义
    stu_school = 'GdSchool'
    # 统计实例化的次数
    count = 0

    # 空对象, 'pzyo', 23, 'male'
    def __init__(self, x, y, z):
        Student.count += 1

        self.stu_name = x  # 空对象.stu_name = 'pzyo'
        self.stu_age = y   # 空对象.stu_age = 23
        self.stu_gender = z # 空对象.stu_gender = 'male'

    # 2. 功能的定义
    def tell_stu_info(self):
        print('名字: %s 年龄: %s 性别: %s' % (
            self.stu_name,
            self.stu_age,
            self.stu_gender
        ))

    def set_stu_info(self, x, y, z):
        self.stu_name = x
        self.stu_age = y
        self.stu_gender = z

    def choose(self, course):
        print('正在选课')
        self.course = course

    # print('====>')

# print(Student.__dict__)
# print(Student.__dict__['stu_school'])
# print(Student.__dict__['set_stu_info'])

# 属性访问的语法
# 1、访问数据属性
# print(Student.stu_school)  # 本质: Student.__dict__['stu_school']
# 2、访问函数属性
# print(Student.set_stu_info)  # 本质: Student.__dict__['set_stu_info']
# 3、新增数据属性
# Student.x = 111 # # 本质: Student.__dict__['stu_school'] = 111

# 再调用类产生对象
# stu1_obj = Student()
# stu2_obj = Student()
# stu3_obj = Student()

# print(stu1_obj.__dict__)  # {}
# print(stu2_obj.__dict__)  # {}
# print(stu3_obj.__dict__)  # {}

# 为对象定制自己独有的属性
# 问题1: 代码重复
# 问题2: 属性的查找顺序
# stu1_obj.stu_name = 'pzyo'   # stu1_obj.__dict__['stu_name'] = 'pzyo'
# stu1_obj.stu_age =  23       # stu1_obj.__dict__['stu_age'] =  23
# stu1_obj.stu_gender = 'male' # stu1_obj.__dict__['stu_gender'] = 'male'
# print(stu1_obj.__dict__)     # {'stu_name': 'pzyo', 'stu_age': 23, 'stu_gender': 'male'}

# stu2_obj.stu_name = 'tom'
# stu2_obj.stu_age =  19
# stu2_obj.stu_gender = 'male'
# print(stu2_obj.__dict__)

# stu3_obj.stu_name = 'marry'
# stu3_obj.stu_age =  18
# stu3_obj.stu_gender = 'female'
# print(stu3_obj.__dict__)

# 解决问题1
# 解决方案1:
# def init(obj, x, y, z):
#     obj.stu_name = x
#     obj.stu_age = y
#     obj.stu_gender = z
# init(stu1_obj, 'pzyo', 23, 'male')
# init(stu2_obj, 'tom', 19, 'male')
# init(stu3_obj, 'marry', 18, 'female')

# 解决方案2:
# 调用类的过程又称之为实例化, 发生了三件事
# 1. 先产生一个空对象
# 2. python会自动调用类中的__init__方法然后将空对象以及调用类时括号内传入的参数一同传给__init__方法
# 3. 返回初始化完的对象
# stu1_obj = Student('pzyo', 23, 'male')  # Student.__init__(空对象, 'pzyo', 23, 'male')
# stu2_obj = Student('tom', 19, 'male')
# stu3_obj = Student('marry', 18, 'female')

# print(stu1_obj.__dict__)
# print(stu2_obj.__dict__)
# print(stu3_obj.__dict__)

# 总结__init__方法
# 1. 会在调用类时自动触发执行, 用来为对象初始化自己独有的数据
# 2. __init__内应该存放的是为对象初始化属性的功能, 但是是可以存放任意其他代码,
#    想要在类调用时就立刻执行的代码都可以放到该方法内
# 3. __init__方法必须返回None (但无需直接写return None)


stu1_obj = Student('pzyo', 23, 'male')
stu2_obj = Student('tom', 19, 'male')
stu3_obj = Student('marry', 18, 'female')

# 类中存放的是对象共有的数据与功能
# 一. 类可以访问
# 1. 类的数据属性
# print(Student.stu_school)
# 2. 类的函数属性
# print(Student.tell_stu_info)
# print(Student.set_stu_info)

# print(stu1_obj.count)
# print(stu2_obj.count)
# print(stu3_obj.count)

# 二. 但其实类中的东西是给对象用的
# 1. 类的数据属性是共享给所有对象用的, 大家访问的地址都一样
# print(id(Student.stu_school))
# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
# print(id(stu3_obj.stu_school))

# Student.stu_school = 'GDSCHOOL'  # 类本身改会影响所有对象
# stu1_obj.stu_school = 'GDSCHOOL'   # 对象本身改是赋值, 只会影响自身
# print(Student.stu_school)
# print(stu1_obj.stu_school)
# print(stu2_obj.stu_school)
# print(stu3_obj.stu_school)

# 2. 类的函数属性主要是给对象使用的, 而且是绑定给对象的,
#    虽然所有对象指向的都是相同的功能, 但是绑定到不同的对象就是不同的方法, 内存地址各不相同

# 类调用自己的函数属性必须严格按照函数的用法来
print(Student.tell_stu_info)
print(Student.set_stu_info)

Student.tell_stu_info(stu1_obj)
Student.tell_stu_info(stu2_obj)
Student.tell_stu_info(stu3_obj)

Student.set_stu_info(stu1_obj, 'PZYO', 24, 'MALE')
Student.tell_stu_info(stu1_obj)

# 绑定方法的特殊之处在于: 谁来调用绑定方法就会将谁当做第一个参数自动传入
print(Student.tell_stu_info)  # <function Student.tell_stu_info at 0x02CB1540>
print(stu1_obj.tell_stu_info) # <bound method Student.tell_stu_info of <__main__.Student object at 0x02AE6730>>
print(stu2_obj.tell_stu_info) # <bound method Student.tell_stu_info of <__main__.Student object at 0x02AE6790>>
print(stu3_obj.tell_stu_info) # <bound method Student.tell_stu_info of <__main__.Student object at 0x02CB4B30>>

stu1_obj.tell_stu_info() # tell_stu_info(stu1_obj)
stu2_obj.tell_stu_info()
stu3_obj.tell_stu_info()

stu1_obj.choose('python')
print(stu1_obj.course)

l = [1, 2, 3] # l = list([1, 2, 3])
print(l.append)
print(list.append)

l.append(4)
list.append(l, 5)
print(l)