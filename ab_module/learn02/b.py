
# 先定义类
# 类是对象相似数据与功能的集合体
# 所以类体中最常见的是变量与函数的定义, 但是其实是可以包含任意其他代码
# 注意: 类体代码是在类定义阶段就会立即执行, 会产生类的名称空间
class Student:
    # 1. 变量的定义
    stu_school = 'GdSchool'

    # 2. 功能的定义
    def tell_stu_info(stu_obj):
        print('名字: %s 年龄: %s 性别: %s' % (
            stu_obj['stu_name'],
            stu_obj['stu_age'],
            stu_obj['stu_gender']
        ))

    def set_stu_info(stu_obj, x, y, z):
        stu_obj['stu_name'] = x
        stu_obj['stu_age'] = y
        stu_obj['stu_gender'] = z

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
stu1_obj = Student()
stu2_obj = Student()
stu3_obj = Student()

# print(stu1_obj.__dict__)  # {}
# print(stu2_obj.__dict__)  # {}
# print(stu3_obj.__dict__)  # {}

# 为对象定制自己独有的属性
# 问题1: 代码重复
# 问题2: 属性的查找顺序
stu1_obj.stu_name = 'pzyo'   # stu1_obj.__dict__['stu_name'] = 'pzyo'
stu1_obj.stu_age =  23       # stu1_obj.__dict__['stu_age'] =  23
stu1_obj.stu_gender = 'male' # stu1_obj.__dict__['stu_gender'] = 'male'
print(stu1_obj.__dict__)     # {'stu_name': 'pzyo', 'stu_age': 23, 'stu_gender': 'male'}

stu2_obj.stu_name = 'tom'
stu2_obj.stu_age =  19
stu2_obj.stu_gender = 'male'
print(stu2_obj.__dict__)

stu3_obj.stu_name = 'marry'
stu3_obj.stu_age =  18
stu3_obj.stu_gender = 'female'
print(stu3_obj.__dict__)