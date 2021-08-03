class School:
    school_name = 'GDSCHOOL'

    def __init__(self, nickname, addr):
        self.nickname = nickname
        self.addr = addr
        self.classes = []

    def related_class(self, class_obj):
        self.classes.append(class_obj)

    def tell_class(self):
        print(('%s%s' % (self.school_name, self.nickname)).center(30, '='))
        for class_obj in self.classes:
            class_obj.tell_class()


class Class:
    def __init__(self, name):
        self.name = name
        self.course = None

    def related_course(self, course_obj):
        self.course = course_obj

    def tell_class(self):
        print('班级名: %s' % self.name, end=" ")
        self.course.tell_course()


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_course(self):
        print('< 课程名:%s 周期:%s 价格:%s >' % (self.name, self.period, self.price))


# 创建学区
school_obj1 = School('广州校区', '广州')
school_obj2 = School('佛山校区', '佛山')

# 创建班级
class_obj1 = Class('14期')
class_obj2 = Class('15期')
class_obj3 = Class('29期')

# 创建课程
course_obj1 = Course('python', '6month', 2)
course_obj2 = Course('linux', '6month', 1)
course_obj3 = Course('go', '6month', 3)

# 班级关联课程
class_obj1.related_course(course_obj1)
class_obj2.related_course(course_obj2)
class_obj3.related_course(course_obj3)

# 学区关联班级
school_obj1.related_class(class_obj1)
school_obj1.related_class(class_obj2)
school_obj2.related_class(class_obj3)

# 查看学区
school_obj1.tell_class()
school_obj2.tell_class()
