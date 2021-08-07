class Mymeta(type):
    n=444

    def __call__(self, *args, **kwargs): #self=<class '__main__.StanfordTeacher'>
        obj=self.__new__(self)
        print(self.__new__ is object.__new__) #True


class Bar(object):
    n=333

    # def __new__(cls, *args, **kwargs):
    #     print('Bar.__new__')

class Foo(Bar):
    n=222

    # def __new__(cls, *args, **kwargs):
    #     print('Foo.__new__')

class StanfordTeacher(Foo,metaclass=Mymeta):
    n=111

    school='Stanford'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s says welcome to the Stanford to learn Python' %self.name)


    # def __new__(cls, *args, **kwargs):
    #     print('StanfordTeacher.__new__')


StanfordTeacher('lili',18) #触发StanfordTeacher的类中的__call__方法的执行，进而执行self.__new__开始查找