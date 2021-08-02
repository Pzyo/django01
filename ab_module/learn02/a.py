
# 学生的数据
stu_name='pzyo'
stu_age=18
stu_gender='male'

# 学生的功能
def tell_info():
    print('名字: %s 年龄: %s 性别: %s'%(stu_name, stu_age, stu_gender))

def set_info(x, y, z):
    global stu_name
    global stu_age
    global stu_gender

    stu_name = x
    stu_age = y
    stu_gender = z